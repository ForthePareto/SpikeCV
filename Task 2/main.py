import sys

import cv2
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget

import GUI
from ActiveContour import greedySnake as snake
from Filters import Filter, gray
from imageModel import ImageModel as IM
from ImgUtils import ImgUtils as IU
from Noises import Noise


class matplotWidget(QWidget):
    def __init__(self,parent=None):
        super(matplotWidget,self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure(figsize=(8, 8), dpi=100)
   
        # this is the Canvas Widget that 
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)

        self.layoutvertical = QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)



class ApplicationWindow(GUI.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(ApplicationWindow, self).setupUi(mainWindow)

        self.init_widget()
        self.initContainers()
        self.Init()
        self.disableViewerControls()
        self.switchControls(True)
        self.initBtns()

    def init_widget(self):
        self.matplot = matplotWidget()
        self.layoutvertical = QVBoxLayout(self.contourWidget)
        self.layoutvertical.addWidget(self.matplot)


    def initContainers(self):
        self.Viewers = [
            self.filterInput, self.filterOutput, self.histInput,
            self.histOutput, self.hybridA, self.hybridB, self.hybridImg,
            self.houghInput, self.houghOutput
        ]

        self.Loaders = [
            self.filterLoader,
            self.histLoader,
            self.hybridLoaderA,
            self.hybridLoaderB,
            self.houghLoader
        ]

        self.filterChecks = [
            self.noiseUniform_check,
            self.noiseGaussian_check,
            self.noiseSAP_check,
            self.filtersAverage_check,
            self.filtersGaussian_check,
            self.filtersMedian_check,
            self.edgeSobel_check,
            self.edgeRoberts_check,
            self.edgePrewitt_check,
            self.filterLowPass_btn,
            self.filterhighPass_btn
        ]
        self.histogramChecks = [
            self.histEqualCheck,
            self.histNormCheck, 
            self.histGTCheck
        ]
        self.houghChecks = [
            self.houghLines_btn,
            self.houghCircles_btn
        ]

    def initBtns(self):
        self.filterLoader.clicked.connect(lambda: self.Disp(0))
        self.filterApply_btn.clicked.connect(lambda: self.filter())

        self.Loaders[1].clicked.connect(lambda: self.Disp(2))
        self.histApply_btn.clicked.connect(lambda: self.histFunctions())

        self.Loaders[2].clicked.connect(lambda: self.Disp(4))
        self.Loaders[3].clicked.connect(lambda: self.Disp(5))
        self.mergeBtn.clicked.connect(lambda: self.makeHybrid())

        self.Loaders[4].clicked.connect(lambda: self.Disp(7))
        self.houghApply_btn.clicked.connect(lambda: self.applyHough())

        self.contourApply_btn.clicked.connect(lambda: self.plot())

    def initChecks(self):
        pass

    def Init(self):
        self.ImgUp = [False, False, False, False, False, False, False]
        self.filterImg = IM("imgs\Waiting.png")
        self.filteredImg = IM("imgs\Waiting.png")
        self.histImg = IM("imgs\Waiting.png")
        self.hybridImgA = IM("imgs\Waiting.png")
        self.hybridImgB = IM("imgs\Waiting.png")
        self.hybridImgRes = IM("imgs\Waiting.png")
        self.houghIn = IM("imgs\Waiting.png")
        self.houghOut = IM("imgs\Waiting.png")
        self.Imgs = [self.filterImg, self.filteredImg, self.histImg,
                    self.hybridImgA, self.hybridImgB,self.hybridImgRes,
                    self.houghIn, self.houghOut]

    def disableViewerControls(self):
        i = 0

        while (i < len(self.Viewers)):
            self.Viewers[i].ui.histogram.hide()
            self.Viewers[i].ui.roiBtn.hide()
            self.Viewers[i].ui.roiPlot.hide()
            self.Viewers[i].ui.menuBtn.hide()
            self.Viewers[i].getView().setAspectLocked(False)
            self.Viewers[i].view.setAspectLocked(False)
            i += 1

    def switchControls(self,state):
        self.noiseGroup.setDisabled(state)
        self.egdeGroup.setDisabled(state)
        self.lpfGroup.setDisabled(state)

    def getImage(self, i):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.filePath, self.format = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Load Image",
            "",
            "Images (*.png *.xpm *.jpg);;",
            options=QtWidgets.QFileDialog.DontUseNativeDialog,
        )
        print("filepath is >>>>>", self.filePath)
        if self.filePath == "":
            pass
        else:
            self.Imgs[i] = IM(self.filePath)
            if str(type(self.Imgs[i].imgByte)) == "<class 'NoneType'>":
                self.ImgUp[i] = False
            else:
                self.ImgUp[i] = True

    def Disp(self, i):
        if i > 3:
            self.getImage(i - 1)

            if self.ImgUp[i-1]:
                print(self.Imgs[i-1].imgByte.shape)
                self.Viewers[i].setImage(self.Imgs[i-1].imgByte.T)
                self.Viewers[i].ui.roiPlot.hide()
                self.switchControls(False)

        else:
            self.getImage(i)

            if self.ImgUp[i]:
                print(self.Imgs[i].imgByte.shape[1])
                self.Viewers[i].setImage(self.Imgs[i].imgByte.T)
                self.Viewers[i].ui.roiPlot.hide()
                if i == 0:
                    self.switchControls(False)
                elif i == 2:
                    self.histogram()

    def filter(self):
        self.Imgs[1].imgByte = self.Imgs[0].imgByte
        self.Imgs[1].imgByte = IM.gray(self.Imgs[1].imgByte)
        if (self.filterChecks[0].isChecked()):
            self.Imgs[1].imgByte = Noise.uniform(self.Imgs[1].imgByte)
        if (self.filterChecks[1].isChecked()):
            self.Imgs[1].imgByte = Noise.gaussian(self.Imgs[1].imgByte)
        if (self.filterChecks[2].isChecked()):
            self.Imgs[1].imgByte = Noise.salt_pepper(self.Imgs[1].imgByte)
        if (self.filterChecks[3].isChecked()):
            self.Imgs[1].imgByte = Filter.average(self.Imgs[1].imgByte)
        if (self.filterChecks[4].isChecked()):
            self.Imgs[1].imgByte = Filter.gaussian(self.Imgs[1].imgByte)
        if (self.filterChecks[5].isChecked()):
            self.Imgs[1].imgByte = Filter.median(self.Imgs[1].imgByte)
        if (self.filterChecks[6].isChecked()):
            self.Imgs[1].imgByte = Filter.sobel(self.Imgs[1].imgByte)
        if (self.filterChecks[7].isChecked()):
            self.Imgs[1].imgByte = Filter.canny(self.Imgs[1].imgByte)
        if (self.filterChecks[8].isChecked()):
            self.Imgs[1].imgByte = Filter.prewitt(self.Imgs[1].imgByte)
        if (self.filterChecks[9].isChecked()):
            self.Imgs[1].imgByte = Filter.low_pass_frequency(self.Imgs[1].imgByte)
        if (self.filterChecks[10].isChecked()):
            self.Imgs[1].imgByte = Filter.high_pass_frequency(self.Imgs[1].imgByte)

        self.Viewers[1].setImage(self.Imgs[1].imgByte.T)
        self.Viewers[1].ui.roiPlot.hide()

    def histogram(self):
        if self.ImgUp[2]:
            histogram, bin_edges = np.histogram(self.Imgs[2].imgByte,
                                                bins=self.Imgs[2].imgWidth,
                                                range=(self.Imgs[2].imgByte.min(),
                                                       self.Imgs[2].imgByte.max()))
            print(histogram)
            self.histInputGraph.plot(bin_edges[:-1], histogram)
    
    def histFunctions(self):
        res = self.Imgs[2].imgByte
        if (self.histogramChecks[0].isChecked()):
            res = IU.histogramEqualization(self.Imgs[2].imgByte)
        elif (self.histogramChecks[1].isChecked()):
            res = self.normalize(self.Imgs[2].imgByte,0,255)
        elif (self.histogramChecks[2].isChecked()):
            res = IU.globalThresholding(self.Imgs[2].imgByte, 150)
            
        self.Viewers[3].setImage(res.T)
        self.Viewers[3].ui.roiPlot.hide()
        histogram, bin_edges = np.histogram(res,
                                                bins=res.shape[1],
                                                range=(res.min(),
                                                       res.max()))
        print(histogram)
        self.histOutputGraph.plot(bin_edges[:-1], histogram)

    def normalize(self,frame: np.ndarray, newMin: float, newMax: float):
        newFrame = np.copy(frame)
        mini = frame.min()
        maxi = frame.max()
        newFrame = (newFrame - mini) * ((newMax - newMin) / (maxi - mini)) + newMin

        return newFrame.astype(np.uint8)

    def makeHybrid(self):
        self.Imgs[5].imgByte = IU.hybrid(self.Imgs[3].imgByte, self.Imgs[4].imgByte)
        self.Viewers[6].setImage(self.Imgs[5].imgByte.T)
        self.Viewers[6].ui.roiPlot.hide()

    def applyHough(self):
        if(self.ImgUp[6] == True):
            res = self.Imgs[6].imgByte
            self.Viewers[8].setImage(Filter.canny_superImpose(res).T)
            self.Viewers[8].ui.roiPlot.hide()

            if (self.houghChecks[0].isChecked()):
                res = Filter.lines_superImpose(res)
            elif (self.houghChecks[1].isChecked()):
                res = Filter.circles_superImpose(res)

            self.Viewers[8].setImage(res.T)
            self.Viewers[8].ui.roiPlot.hide()
    
    def plot(self):
        im = cv2.imread('imgs\mri.png')
        im = gray(im)

        points = snake._pointsOnCircle((290, 440), 125, 30)

        self.activeContour(im, points)

        """ self.matplot.axis.clear()
        self.matplot.axis.imshow(im, cmap=cm.Greys_r)
        #self.matplot.canvas.pause(0.01)
        self.matplot.canvas.draw() """
    
    def dispPlot(self,image,points):
        self.matplot.axis.clear()
        for s in points:
                self.matplot.axis.plot(s[0],s[1],'g.',markersize=10.0)
        self.matplot.axis.imshow(image, cmap=cm.Greys_r)
        self.matplot.canvas.draw()
        
        return

    def activeContour(self, image, points):
        """
        Iterate the contour until the energy reaches an equilibrium
        """
        energy_matrix = np.zeros( (10000 - 1, 9, 9), dtype=np.float32)
        position_matrix = np.zeros( (10000 - 1, 9, 9, 2), dtype=np.int32 )
        neighbors = np.array([[i, j] for i in range(-1, 2) for j in range(-1, 2)])
        min_final_energy_prev = float("inf")
        
        counter = 0
        smooth_factor = 15 
        iterations = 30
        gradient_image = snake._gradientImage(image)
        smooth_image = cv2.GaussianBlur(gradient_image, (smooth_factor, smooth_factor),0)
        self.dispPlot(image, points)

        while True:
            counter += 1
            if not (counter % iterations):
                iterations += 1
                if smooth_factor > 4:
                    smooth_factor -= 4            
                smooth_image = cv2.GaussianBlur(gradient_image, (smooth_factor, smooth_factor),0)
                print("Deblur step, smooth factor now: ", smooth_factor)
            
            self.dispPlot(smooth_image, points)
            min_final_energy = snake._iterateContour(image, smooth_image, points, energy_matrix, position_matrix, neighbors)
            
            if (min_final_energy == min_final_energy_prev) or smooth_factor < 4:
                print ("Min energy reached at ", min_final_energy)
                print ("Final smooth factor ", smooth_factor)
                self.dispPlot(image, points)
                break
            else:
                min_final_energy_prev = min_final_energy
            
            QtWidgets.QApplication.processEvents()



def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
