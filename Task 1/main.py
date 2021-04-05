import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import GUI
from imageModel import ImageModel as IM
from Noises import Noise
from Filters import Filter
from ImgUtils import ImgUtils as IU


class ApplicationWindow(GUI.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(ApplicationWindow, self).setupUi(mainWindow)

        self.initContainers()
        self.Init()
        self.disableViewerControls()
        self.switchControls(True)
        self.initBtns()

    def initContainers(self):
        self.Viewers = [
            self.filterInput, self.filterOutput, self.histInput,
            self.histOutput, self.hybridA, self.hybridB, self.hybridImg
        ]

        self.Loaders = [
            self.filterLoader,
            self.histLoader,
            self.hybridLoaderA,
            self.hybridLoaderB
        ]

        self.Checks = [
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

    def initBtns(self):
        self.filterLoader.clicked.connect(lambda: self.Disp(0))
        self.filterApply_btn.clicked.connect(lambda: self.filter())

        self.Loaders[1].clicked.connect(lambda: self.Disp(2))

        self.Loaders[2].clicked.connect(lambda: self.Disp(4))
        self.Loaders[3].clicked.connect(lambda: self.Disp(5))
        self.mergeBtn.clicked.connect(lambda: self.makeHybrid())


    def initChecks(self):
        pass

    def Init(self):
        self.ImgUp = [False, False, False, False, False]
        self.filterImg = IM("Waiting.png")
        self.filteredImg = IM("Waiting.png")
        self.histImg = IM("Waiting.png")
        self.hybridImgA = IM("Waiting.png")
        self.hybridImgB = IM("Waiting.png")
        self.hybridImgRes = IM("Waiting.png")
        self.Imgs = [self.filterImg, self.filteredImg, self.histImg, self.hybridImgA, self.hybridImgB,self.hybridImgRes]

    def disableViewerControls(self):
        i = 0
        while (i < 7):
            self.Viewers[i].ui.histogram.hide()
            self.Viewers[i].ui.roiBtn.hide()
            self.Viewers[i].ui.roiPlot.hide()
            self.Viewers[i].ui.menuBtn.hide()
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
        if i == 6 or i == 7:
            self.getImage(i - 1)

            if self.ImgUp[i-1]:
                print(self.Imgs[i-1].imgByte.shape)
                self.Viewers[i].setImage(self.Imgs[i-1].imgByte.T)
                self.switchControls(False)

        else:
            self.getImage(i)

            if self.ImgUp[i]:
                print(self.Imgs[i].imgByte.shape[1])
                self.Viewers[i].setImage(self.Imgs[i].imgByte.T)
                if i == 0:
                    self.switchControls(False)
                elif i == 2:
                    self.histogram()

    def filter(self):
        self.Imgs[1].imgByte = self.Imgs[0].imgByte
        self.Imgs[1].imgByte = IM.gray(self.Imgs[1].imgByte)
        if (self.Checks[0].isChecked()):
            self.Imgs[1].imgByte = Noise.uniform(self.Imgs[1].imgByte)
        if (self.Checks[1].isChecked()):
            self.Imgs[1].imgByte = Noise.gaussian(self.Imgs[1].imgByte)
        if (self.Checks[2].isChecked()):
            self.Imgs[1].imgByte = Noise.salt_pepper(self.Imgs[1].imgByte)
        if (self.Checks[3].isChecked()):
            self.Imgs[1].imgByte = Filter.average(self.Imgs[1].imgByte)
        if (self.Checks[4].isChecked()):
            self.Imgs[1].imgByte = Filter.gaussian(self.Imgs[1].imgByte)
        if (self.Checks[5].isChecked()):
            self.Imgs[1].imgByte = Filter.median(self.Imgs[1].imgByte)
        if (self.Checks[6].isChecked()):
            self.Imgs[1].imgByte = Filter.sobel(self.Imgs[1].imgByte)
        if (self.Checks[7].isChecked()):
            self.Imgs[1].imgByte = Filter.canny(self.Imgs[1].imgByte)
        if (self.Checks[8].isChecked()):
            self.Imgs[1].imgByte = Filter.prewitt(self.Imgs[1].imgByte)
        if (self.Checks[9].isChecked()):
            self.Imgs[1].imgByte = Filter.low_pass_frequency(self.Imgs[1].imgByte)
        if (self.Checks[10].isChecked()):
            self.Imgs[1].imgByte = Filter.high_pass_frequency(self.Imgs[1].imgByte)

        self.Viewers[1].setImage(self.Imgs[1].imgByte.T)

    def histogram(self):
        if self.ImgUp[2]:
            histogram, bin_edges = np.histogram(self.Imgs[2].imgByte,
                                                bins=self.Imgs[2].imgWidth,
                                                range=(self.Imgs[2].imgByte.min(),
                                                       self.Imgs[2].imgByte.max()))
            print(histogram)
            self.histInputGraph.plot(bin_edges[:-1],histogram)

    def makeHybrid(self):
        self.Imgs[5].imgByte = IU.hybrid(self.Imgs[3].imgByte, self.Imgs[4].imgByte)
        self.Viewers[6].setImage(self.Imgs[5].imgByte.T)




def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
