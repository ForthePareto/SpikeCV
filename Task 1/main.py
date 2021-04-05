import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

import GUI
from imageModel import ImageModel as IM
from Noises import Noise
from Filters import Filter


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
            self.histOutput, self.histInputGraph, self.histOutputGraph,
            self.hybridA, self.hybridB, self.hybridImg
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
        self.filterLoader.clicked.connect(lambda: self.filterDisp(0))
        self.filterApply_btn.clicked.connect(lambda: self.filter())
    
    def initChecks(self):
        pass

    def Init(self):
        self.ImgUp = [False, False, False, False]
        self.filterImg = IM("Waiting.png")
        self.filteredImg = IM("Waiting.png")
        self.histImg = IM("Waiting.png")
        self.hybridImaA = IM("Waiting.png")
        self.hybridImaB = IM("Waiting.png")
        self.Imgs = [self.filterImg, self.filteredImg, self.histImg, self.hybridImaA, self.hybridImaB]

    def disableViewerControls(self):
        i = 0
        while (i < 9):
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

    def filterDisp(self, i):
        self.getImage(i)

        if self.ImgUp[i]:
            print(self.Imgs[i].imgByte.shape)
            self.Viewers[i].setImage(self.Imgs[i].imgByte.T)
            self.switchControls(False)

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
        
            




def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()