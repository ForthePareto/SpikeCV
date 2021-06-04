# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import ImageView
import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 660)
        MainWindow.setMaximumSize(QSize(944, 660))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 911, 611))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabBarAutoHide(False)
        self.Filters = QWidget()
        self.Filters.setObjectName(u"Filters")
        self.gridLayoutWidget_2 = QWidget(self.Filters)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 10, 897, 561))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(350, 350))
        self.groupBox_2.setMaximumSize(QSize(350, 350))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(21)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.filterInput = ImageView(self.groupBox_2)
        self.filterInput.setObjectName(u"filterInput")
        self.filterInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filterInput.sizePolicy().hasHeightForWidth())
        self.filterInput.setSizePolicy(sizePolicy1)
        self.filterInput.setMinimumSize(QSize(301, 301))
        self.filterInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(350, 350))
        self.groupBox_4.setMaximumSize(QSize(350, 350))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.filterOutput = ImageView(self.groupBox_4)
        self.filterOutput.setObjectName(u"filterOutput")
        self.filterOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.filterOutput.sizePolicy().hasHeightForWidth())
        self.filterOutput.setSizePolicy(sizePolicy1)
        self.filterOutput.setMinimumSize(QSize(301, 301))
        self.filterOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout.addWidget(self.groupBox_4)


        self.gridLayout_10.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filterApply_btn = QPushButton(self.gridLayoutWidget_2)
        self.filterApply_btn.setObjectName(u"filterApply_btn")
        self.filterApply_btn.setMinimumSize(QSize(0, 51))
        self.filterApply_btn.setMaximumSize(QSize(201, 16777215))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(17)
        self.filterApply_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.filterApply_btn)


        self.gridLayout_10.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_10, 1, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.noiseGroup = QGroupBox(self.gridLayoutWidget_2)
        self.noiseGroup.setObjectName(u"noiseGroup")
        sizePolicy.setHeightForWidth(self.noiseGroup.sizePolicy().hasHeightForWidth())
        self.noiseGroup.setSizePolicy(sizePolicy)
        self.noiseGroup.setMinimumSize(QSize(151, 101))
        self.noiseGroup.setMaximumSize(QSize(151, 101))
        self.verticalLayoutWidget = QWidget(self.noiseGroup)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 111, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.noiseUniform_check = QCheckBox(self.verticalLayoutWidget)
        self.noiseUniform_check.setObjectName(u"noiseUniform_check")

        self.verticalLayout.addWidget(self.noiseUniform_check)

        self.noiseGaussian_check = QCheckBox(self.verticalLayoutWidget)
        self.noiseGaussian_check.setObjectName(u"noiseGaussian_check")

        self.verticalLayout.addWidget(self.noiseGaussian_check)

        self.noiseSAP_check = QCheckBox(self.verticalLayoutWidget)
        self.noiseSAP_check.setObjectName(u"noiseSAP_check")

        self.verticalLayout.addWidget(self.noiseSAP_check)


        self.gridLayout_3.addWidget(self.noiseGroup, 5, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.filterInputName = QLabel(self.gridLayoutWidget_2)
        self.filterInputName.setObjectName(u"filterInputName")

        self.verticalLayout_8.addWidget(self.filterInputName)

        self.filterInputSize = QLabel(self.gridLayoutWidget_2)
        self.filterInputSize.setObjectName(u"filterInputSize")

        self.verticalLayout_8.addWidget(self.filterInputSize)


        self.gridLayout_3.addLayout(self.verticalLayout_8, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 14, 0, 1, 1)

        self.verticalSpacer3 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer3, 4, 0, 1, 1)

        self.freqDomainGroup = QGroupBox(self.gridLayoutWidget_2)
        self.freqDomainGroup.setObjectName(u"freqDomainGroup")
        self.freqDomainGroup.setMinimumSize(QSize(151, 101))
        self.verticalLayoutWidget_5 = QWidget(self.freqDomainGroup)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 131, 71))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.filterLowPass_btn = QRadioButton(self.verticalLayoutWidget_5)
        self.filterLowPass_btn.setObjectName(u"filterLowPass_btn")

        self.verticalLayout_12.addWidget(self.filterLowPass_btn)

        self.filterhighPass_btn = QRadioButton(self.verticalLayoutWidget_5)
        self.filterhighPass_btn.setObjectName(u"filterhighPass_btn")

        self.verticalLayout_12.addWidget(self.filterhighPass_btn)


        self.gridLayout_3.addWidget(self.freqDomainGroup, 11, 0, 1, 1)

        self.verticalSpacer6 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer6, 10, 0, 1, 1)

        self.verticalSpacer2 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer2, 2, 0, 1, 1)

        self.verticalSpacer4 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer4, 7, 0, 1, 1)

        self.filterLoader = QPushButton(self.gridLayoutWidget_2)
        self.filterLoader.setObjectName(u"filterLoader")
        sizePolicy.setHeightForWidth(self.filterLoader.sizePolicy().hasHeightForWidth())
        self.filterLoader.setSizePolicy(sizePolicy)
        self.filterLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_3.addWidget(self.filterLoader, 1, 0, 1, 1)

        self.spatialDomainFiltersGroup = QGroupBox(self.gridLayoutWidget_2)
        self.spatialDomainFiltersGroup.setObjectName(u"spatialDomainFiltersGroup")
        self.spatialDomainFiltersGroup.setMinimumSize(QSize(151, 221))
        self.verticalLayoutWidget_4 = QWidget(self.spatialDomainFiltersGroup)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 15, 131, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lpfGroup = QGroupBox(self.verticalLayoutWidget_4)
        self.lpfGroup.setObjectName(u"lpfGroup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lpfGroup.sizePolicy().hasHeightForWidth())
        self.lpfGroup.setSizePolicy(sizePolicy2)
        self.lpfGroup.setMinimumSize(QSize(0, 0))
        self.lpfGroup.setMaximumSize(QSize(131, 101))
        self.lpfGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.lpfGroup)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 111, 71))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.filtersAverage_check = QRadioButton(self.verticalLayoutWidget_2)
        self.filtersAverage_check.setObjectName(u"filtersAverage_check")

        self.verticalLayout_3.addWidget(self.filtersAverage_check)

        self.filtersGaussian_check = QRadioButton(self.verticalLayoutWidget_2)
        self.filtersGaussian_check.setObjectName(u"filtersGaussian_check")

        self.verticalLayout_3.addWidget(self.filtersGaussian_check)

        self.filtersMedian_check = QRadioButton(self.verticalLayoutWidget_2)
        self.filtersMedian_check.setObjectName(u"filtersMedian_check")

        self.verticalLayout_3.addWidget(self.filtersMedian_check)


        self.verticalLayout_2.addWidget(self.lpfGroup)

        self.verticalSpacer5 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer5)

        self.egdeGroup = QGroupBox(self.verticalLayoutWidget_4)
        self.egdeGroup.setObjectName(u"egdeGroup")
        self.egdeGroup.setMinimumSize(QSize(0, 0))
        self.egdeGroup.setMaximumSize(QSize(131, 91))
        self.egdeGroup.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_3 = QWidget(self.egdeGroup)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 114, 65))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.edgeSobel_check = QRadioButton(self.verticalLayoutWidget_3)
        self.edgeSobel_check.setObjectName(u"edgeSobel_check")

        self.verticalLayout_4.addWidget(self.edgeSobel_check)

        self.edgeRoberts_check = QRadioButton(self.verticalLayoutWidget_3)
        self.edgeRoberts_check.setObjectName(u"edgeRoberts_check")

        self.verticalLayout_4.addWidget(self.edgeRoberts_check)

        self.edgePrewitt_check = QRadioButton(self.verticalLayoutWidget_3)
        self.edgePrewitt_check.setObjectName(u"edgePrewitt_check")

        self.verticalLayout_4.addWidget(self.edgePrewitt_check)


        self.verticalLayout_2.addWidget(self.egdeGroup)


        self.gridLayout_3.addWidget(self.spatialDomainFiltersGroup, 8, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Filters, QString())
        self.Histograms = QWidget()
        self.Histograms.setObjectName(u"Histograms")
        self.gridLayoutWidget_3 = QWidget(self.Histograms)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, 9, 881, 571))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_6 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(261, 271))
        self.groupBox_6.setMaximumSize(QSize(261, 271))
        self.histOutput = ImageView(self.groupBox_6)
        self.histOutput.setObjectName(u"histOutput")
        self.histOutput.setGeometry(QRect(10, 20, 241, 241))
        self.histOutput.setMinimumSize(QSize(241, 241))
        self.histOutput.setMaximumSize(QSize(241, 241))

        self.gridLayout_7.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_19, 2, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMinimumSize(QSize(29, 271))
        self.groupBox_5.setMaximumSize(QSize(261, 271))
        self.histInput = ImageView(self.groupBox_5)
        self.histInput.setObjectName(u"histInput")
        self.histInput.setGeometry(QRect(10, 20, 241, 241))
        self.histInput.setMinimumSize(QSize(241, 241))
        self.histInput.setMaximumSize(QSize(241, 241))

        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(261, 271))
        self.groupBox_8.setMaximumSize(QSize(261, 271))
        self.histOutputGraph = PlotWidget(self.groupBox_8)
        self.histOutputGraph.setObjectName(u"histOutputGraph")
        self.histOutputGraph.setGeometry(QRect(10, 20, 241, 241))
        self.histOutputGraph.setMinimumSize(QSize(241, 241))
        self.histOutputGraph.setMaximumSize(QSize(241, 241))

        self.gridLayout_7.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(261, 271))
        self.groupBox_7.setMaximumSize(QSize(261, 271))
        self.histInputGraph = PlotWidget(self.groupBox_7)
        self.histInputGraph.setObjectName(u"histInputGraph")
        self.histInputGraph.setGeometry(QRect(10, 20, 241, 241))
        self.histInputGraph.setMinimumSize(QSize(241, 241))
        self.histInputGraph.setMaximumSize(QSize(241, 241))

        self.gridLayout_7.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_20, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer_5 = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.histLoader = QPushButton(self.gridLayoutWidget_3)
        self.histLoader.setObjectName(u"histLoader")
        sizePolicy.setHeightForWidth(self.histLoader.sizePolicy().hasHeightForWidth())
        self.histLoader.setSizePolicy(sizePolicy)
        self.histLoader.setMaximumSize(QSize(151, 51))

        self.verticalLayout_5.addWidget(self.histLoader)

        self.verticalSpacer_15 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_15)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.histInputName = QLabel(self.gridLayoutWidget_3)
        self.histInputName.setObjectName(u"histInputName")

        self.verticalLayout_9.addWidget(self.histInputName)

        self.histInputSize = QLabel(self.gridLayoutWidget_3)
        self.histInputSize.setObjectName(u"histInputSize")

        self.verticalLayout_9.addWidget(self.histInputSize)


        self.verticalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalSpacer_6 = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.groupBox_10 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(151, 121))
        self.groupBox_10.setMaximumSize(QSize(151, 16777215))
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_10)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 131, 91))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.histEqualCheck = QRadioButton(self.verticalLayoutWidget_6)
        self.histEqualCheck.setObjectName(u"histEqualCheck")

        self.verticalLayout_13.addWidget(self.histEqualCheck)

        self.histNormCheck = QRadioButton(self.verticalLayoutWidget_6)
        self.histNormCheck.setObjectName(u"histNormCheck")

        self.verticalLayout_13.addWidget(self.histNormCheck)

        self.histGTCheck = QRadioButton(self.verticalLayoutWidget_6)
        self.histGTCheck.setObjectName(u"histGTCheck")

        self.verticalLayout_13.addWidget(self.histGTCheck)


        self.verticalLayout_5.addWidget(self.groupBox_10)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.histApply_btn = QPushButton(self.gridLayoutWidget_3)
        self.histApply_btn.setObjectName(u"histApply_btn")

        self.verticalLayout_5.addWidget(self.histApply_btn)

        self.verticalSpacer_9 = QSpacerItem(5, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.tabWidget.addTab(self.Histograms, QString())
        self.Hybrid = QWidget()
        self.Hybrid.setObjectName(u"Hybrid")
        self.gridLayoutWidget_6 = QWidget(self.Hybrid)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(9, 9, 881, 571))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(451, 451))
        self.groupBox.setMaximumSize(QSize(451, 451))
        self.hybridImg = ImageView(self.groupBox)
        self.hybridImg.setObjectName(u"hybridImg")
        self.hybridImg.setGeometry(QRect(20, 30, 401, 401))
        self.hybridImg.setMinimumSize(QSize(401, 401))
        self.hybridImg.setMaximumSize(QSize(401, 401))

        self.gridLayout_11.addWidget(self.groupBox, 0, 2, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.gridLayoutWidget_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(251, 261))
        self.groupBox_3.setMaximumSize(QSize(261, 271))
        self.hybridA = ImageView(self.groupBox_3)
        self.hybridA.setObjectName(u"hybridA")
        self.hybridA.setGeometry(QRect(10, 20, 231, 231))
        self.hybridA.setMinimumSize(QSize(231, 231))
        self.hybridA.setMaximumSize(QSize(231, 231))

        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.groupBox_9 = QGroupBox(self.gridLayoutWidget_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(251, 261))
        self.hybridB = ImageView(self.groupBox_9)
        self.hybridB.setObjectName(u"hybridB")
        self.hybridB.setGeometry(QRect(10, 20, 231, 231))
        self.hybridB.setMinimumSize(QSize(231, 231))
        self.hybridB.setMaximumSize(QSize(231, 231))

        self.verticalLayout_7.addWidget(self.groupBox_9)


        self.gridLayout_11.addLayout(self.verticalLayout_7, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_11, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_10 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.hybridLoaderA = QPushButton(self.gridLayoutWidget_6)
        self.hybridLoaderA.setObjectName(u"hybridLoaderA")

        self.verticalLayout_6.addWidget(self.hybridLoaderA)

        self.verticalSpacer_16 = QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.hybridInputAName = QLabel(self.gridLayoutWidget_6)
        self.hybridInputAName.setObjectName(u"hybridInputAName")

        self.verticalLayout_10.addWidget(self.hybridInputAName)

        self.hybridInputASize = QLabel(self.gridLayoutWidget_6)
        self.hybridInputASize.setObjectName(u"hybridInputASize")

        self.verticalLayout_10.addWidget(self.hybridInputASize)


        self.verticalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalSpacer_11 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)

        self.hybridLoaderB = QPushButton(self.gridLayoutWidget_6)
        self.hybridLoaderB.setObjectName(u"hybridLoaderB")

        self.verticalLayout_6.addWidget(self.hybridLoaderB)

        self.verticalSpacer_17 = QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_17)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.hybridInputBName = QLabel(self.gridLayoutWidget_6)
        self.hybridInputBName.setObjectName(u"hybridInputBName")

        self.verticalLayout_11.addWidget(self.hybridInputBName)

        self.hybridInputBSize = QLabel(self.gridLayoutWidget_6)
        self.hybridInputBSize.setObjectName(u"hybridInputBSize")

        self.verticalLayout_11.addWidget(self.hybridInputBSize)


        self.verticalLayout_6.addLayout(self.verticalLayout_11)

        self.verticalSpacer_12 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)

        self.mergeBtn = QPushButton(self.gridLayoutWidget_6)
        self.mergeBtn.setObjectName(u"mergeBtn")

        self.verticalLayout_6.addWidget(self.mergeBtn)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_14)


        self.gridLayout_9.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.tabWidget.addTab(self.Hybrid, QString())
        self.Hough = QWidget()
        self.Hough.setObjectName(u"Hough")
        self.gridLayoutWidget_5 = QWidget(self.Hough)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 897, 561))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_14, 1, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_15, 1, 3, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_14 = QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(350, 350))
        self.groupBox_14.setMaximumSize(QSize(350, 350))
        self.groupBox_14.setFont(font)
        self.groupBox_14.setAlignment(Qt.AlignCenter)
        self.groupBox_14.setFlat(False)
        self.houghInput = ImageView(self.groupBox_14)
        self.houghInput.setObjectName(u"houghInput")
        self.houghInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.houghInput.sizePolicy().hasHeightForWidth())
        self.houghInput.setSizePolicy(sizePolicy1)
        self.houghInput.setMinimumSize(QSize(301, 301))
        self.houghInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_7.addWidget(self.groupBox_14)

        self.horizontalSpacer_16 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.groupBox_15 = QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy1.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy1)
        self.groupBox_15.setMinimumSize(QSize(350, 350))
        self.groupBox_15.setMaximumSize(QSize(350, 350))
        self.groupBox_15.setFont(font)
        self.groupBox_15.setAlignment(Qt.AlignCenter)
        self.houghOutput = ImageView(self.groupBox_15)
        self.houghOutput.setObjectName(u"houghOutput")
        self.houghOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.houghOutput.sizePolicy().hasHeightForWidth())
        self.houghOutput.setSizePolicy(sizePolicy1)
        self.houghOutput.setMinimumSize(QSize(301, 301))
        self.houghOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_7.addWidget(self.groupBox_15)


        self.gridLayout_16.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_16.addItem(self.verticalSpacer_24, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.houghApply_btn = QPushButton(self.gridLayoutWidget_5)
        self.houghApply_btn.setObjectName(u"houghApply_btn")
        self.houghApply_btn.setMinimumSize(QSize(0, 51))
        self.houghApply_btn.setMaximumSize(QSize(201, 16777215))
        self.houghApply_btn.setFont(font1)

        self.horizontalLayout_8.addWidget(self.houghApply_btn)


        self.gridLayout_16.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 1, 2, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalSpacer_25 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer_25, 0, 0, 1, 1)

        self.verticalSpacer3_3 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer3_3, 4, 0, 1, 1)

        self.verticalSpacer2_4 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer2_4, 2, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_26, 10, 0, 1, 1)

        self.freqDomainGroup_3 = QGroupBox(self.gridLayoutWidget_5)
        self.freqDomainGroup_3.setObjectName(u"freqDomainGroup_3")
        self.freqDomainGroup_3.setMinimumSize(QSize(151, 101))
        self.verticalLayoutWidget_13 = QWidget(self.freqDomainGroup_3)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(10, 20, 131, 71))
        self.verticalLayout_23 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.houghLines_btn = QRadioButton(self.verticalLayoutWidget_13)
        self.houghLines_btn.setObjectName(u"houghLines_btn")

        self.verticalLayout_23.addWidget(self.houghLines_btn)

        self.houghCircles_btn = QRadioButton(self.verticalLayoutWidget_13)
        self.houghCircles_btn.setObjectName(u"houghCircles_btn")

        self.verticalLayout_23.addWidget(self.houghCircles_btn)


        self.gridLayout_17.addWidget(self.freqDomainGroup_3, 7, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.houghInputName = QLabel(self.gridLayoutWidget_5)
        self.houghInputName.setObjectName(u"houghInputName")

        self.verticalLayout_22.addWidget(self.houghInputName)

        self.houghInputSize = QLabel(self.gridLayoutWidget_5)
        self.houghInputSize.setObjectName(u"houghInputSize")

        self.verticalLayout_22.addWidget(self.houghInputSize)


        self.gridLayout_17.addLayout(self.verticalLayout_22, 3, 0, 1, 1)

        self.houghLoader = QPushButton(self.gridLayoutWidget_5)
        self.houghLoader.setObjectName(u"houghLoader")
        sizePolicy.setHeightForWidth(self.houghLoader.sizePolicy().hasHeightForWidth())
        self.houghLoader.setSizePolicy(sizePolicy)
        self.houghLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_17.addWidget(self.houghLoader, 1, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_17, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Hough, QString())
        self.Contour = QWidget()
        self.Contour.setObjectName(u"Contour")
        self.gridLayoutWidget_4 = QWidget(self.Contour)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(6, 10, 891, 567))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.contourApply_btn = QPushButton(self.gridLayoutWidget_4)
        self.contourApply_btn.setObjectName(u"contourApply_btn")
        self.contourApply_btn.setMinimumSize(QSize(0, 51))
        self.contourApply_btn.setMaximumSize(QSize(201, 16777215))
        self.contourApply_btn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.contourApply_btn)


        self.gridLayout_12.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_12 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.groupBox_12.setMinimumSize(QSize(500, 450))
        self.groupBox_12.setMaximumSize(QSize(500, 450))
        self.groupBox_12.setFont(font)
        self.groupBox_12.setAlignment(Qt.AlignCenter)
        self.contourWidget = QWidget(self.groupBox_12)
        self.contourWidget.setObjectName(u"contourWidget")
        self.contourWidget.setGeometry(QRect(10, 30, 481, 401))

        self.horizontalLayout_2.addWidget(self.groupBox_12)


        self.gridLayout_12.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_13, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_12, 1, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_18 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_18, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.contourInputName = QLabel(self.gridLayoutWidget_4)
        self.contourInputName.setObjectName(u"contourInputName")
        self.contourInputName.setEnabled(False)

        self.verticalLayout_15.addWidget(self.contourInputName)

        self.contourInputSize = QLabel(self.gridLayoutWidget_4)
        self.contourInputSize.setObjectName(u"contourInputSize")
        self.contourInputSize.setEnabled(False)

        self.verticalLayout_15.addWidget(self.contourInputSize)


        self.gridLayout_6.addLayout(self.verticalLayout_15, 3, 0, 1, 1)

        self.contourLoader = QPushButton(self.gridLayoutWidget_4)
        self.contourLoader.setObjectName(u"contourLoader")
        self.contourLoader.setEnabled(False)
        sizePolicy.setHeightForWidth(self.contourLoader.sizePolicy().hasHeightForWidth())
        self.contourLoader.setSizePolicy(sizePolicy)
        self.contourLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_6.addWidget(self.contourLoader, 1, 0, 1, 1)

        self.verticalSpacer2_2 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_6.addItem(self.verticalSpacer2_2, 2, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Contour, QString())
        self.Corners = QWidget()
        self.Corners.setObjectName(u"Corners")
        self.gridLayoutWidget_7 = QWidget(self.Corners)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 897, 561))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_17, 1, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_18, 1, 3, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_16 = QGroupBox(self.gridLayoutWidget_7)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(350, 350))
        self.groupBox_16.setMaximumSize(QSize(350, 350))
        self.groupBox_16.setFont(font)
        self.groupBox_16.setAlignment(Qt.AlignCenter)
        self.groupBox_16.setFlat(False)
        self.cornersInput = ImageView(self.groupBox_16)
        self.cornersInput.setObjectName(u"cornersInput")
        self.cornersInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.cornersInput.sizePolicy().hasHeightForWidth())
        self.cornersInput.setSizePolicy(sizePolicy1)
        self.cornersInput.setMinimumSize(QSize(301, 301))
        self.cornersInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_9.addWidget(self.groupBox_16)

        self.horizontalSpacer_19 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.groupBox_17 = QGroupBox(self.gridLayoutWidget_7)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy1.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy1)
        self.groupBox_17.setMinimumSize(QSize(350, 350))
        self.groupBox_17.setMaximumSize(QSize(350, 350))
        self.groupBox_17.setFont(font)
        self.groupBox_17.setAlignment(Qt.AlignCenter)
        self.cornersOutput = ImageView(self.groupBox_17)
        self.cornersOutput.setObjectName(u"cornersOutput")
        self.cornersOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.cornersOutput.sizePolicy().hasHeightForWidth())
        self.cornersOutput.setSizePolicy(sizePolicy1)
        self.cornersOutput.setMinimumSize(QSize(301, 301))
        self.cornersOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_9.addWidget(self.groupBox_17)


        self.gridLayout_19.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_19.addItem(self.verticalSpacer_27, 2, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cornersApply_btn = QPushButton(self.gridLayoutWidget_7)
        self.cornersApply_btn.setObjectName(u"cornersApply_btn")
        self.cornersApply_btn.setMinimumSize(QSize(0, 51))
        self.cornersApply_btn.setMaximumSize(QSize(201, 16777215))
        self.cornersApply_btn.setFont(font1)

        self.horizontalLayout_10.addWidget(self.cornersApply_btn)


        self.gridLayout_19.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_19, 1, 2, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalSpacer_29 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_29, 8, 0, 1, 1)

        self.verticalSpacer2_5 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_20.addItem(self.verticalSpacer2_5, 2, 0, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_20.addItem(self.verticalSpacer_28, 0, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.cornersInputName = QLabel(self.gridLayoutWidget_7)
        self.cornersInputName.setObjectName(u"cornersInputName")

        self.verticalLayout_24.addWidget(self.cornersInputName)

        self.cornersInputSize = QLabel(self.gridLayoutWidget_7)
        self.cornersInputSize.setObjectName(u"cornersInputSize")

        self.verticalLayout_24.addWidget(self.cornersInputSize)


        self.gridLayout_20.addLayout(self.verticalLayout_24, 3, 0, 1, 1)

        self.cornersLoader = QPushButton(self.gridLayoutWidget_7)
        self.cornersLoader.setObjectName(u"cornersLoader")
        sizePolicy.setHeightForWidth(self.cornersLoader.sizePolicy().hasHeightForWidth())
        self.cornersLoader.setSizePolicy(sizePolicy)
        self.cornersLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_20.addWidget(self.cornersLoader, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_20, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Corners, QString())
        self.SIFT = QWidget()
        self.SIFT.setObjectName(u"SIFT")
        self.gridLayoutWidget_8 = QWidget(self.SIFT)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 10, 897, 561))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_20, 1, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_21, 1, 3, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_19 = QGroupBox(self.gridLayoutWidget_8)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(350, 350))
        self.groupBox_19.setMaximumSize(QSize(350, 350))
        self.groupBox_19.setFont(font)
        self.groupBox_19.setAlignment(Qt.AlignCenter)
        self.groupBox_19.setFlat(False)
        self.siftInput = ImageView(self.groupBox_19)
        self.siftInput.setObjectName(u"siftInput")
        self.siftInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.siftInput.sizePolicy().hasHeightForWidth())
        self.siftInput.setSizePolicy(sizePolicy1)
        self.siftInput.setMinimumSize(QSize(301, 301))
        self.siftInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_11.addWidget(self.groupBox_19)

        self.horizontalSpacer_22 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)

        self.groupBox_20 = QGroupBox(self.gridLayoutWidget_8)
        self.groupBox_20.setObjectName(u"groupBox_20")
        sizePolicy1.setHeightForWidth(self.groupBox_20.sizePolicy().hasHeightForWidth())
        self.groupBox_20.setSizePolicy(sizePolicy1)
        self.groupBox_20.setMinimumSize(QSize(350, 350))
        self.groupBox_20.setMaximumSize(QSize(350, 350))
        self.groupBox_20.setFont(font)
        self.groupBox_20.setAlignment(Qt.AlignCenter)
        self.siftOutput = ImageView(self.groupBox_20)
        self.siftOutput.setObjectName(u"siftOutput")
        self.siftOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.siftOutput.sizePolicy().hasHeightForWidth())
        self.siftOutput.setSizePolicy(sizePolicy1)
        self.siftOutput.setMinimumSize(QSize(301, 301))
        self.siftOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_11.addWidget(self.groupBox_20)


        self.gridLayout_22.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_22.addItem(self.verticalSpacer_34, 2, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.siftApply_btn = QPushButton(self.gridLayoutWidget_8)
        self.siftApply_btn.setObjectName(u"siftApply_btn")
        self.siftApply_btn.setMinimumSize(QSize(0, 51))
        self.siftApply_btn.setMaximumSize(QSize(201, 16777215))
        self.siftApply_btn.setFont(font1)

        self.horizontalLayout_12.addWidget(self.siftApply_btn)


        self.gridLayout_22.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_22, 1, 2, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalSpacer_35 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_35, 8, 0, 1, 1)

        self.verticalSpacer2_6 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_23.addItem(self.verticalSpacer2_6, 2, 0, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_23.addItem(self.verticalSpacer_36, 0, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.siftInputName = QLabel(self.gridLayoutWidget_8)
        self.siftInputName.setObjectName(u"siftInputName")

        self.verticalLayout_25.addWidget(self.siftInputName)

        self.siftInputSize = QLabel(self.gridLayoutWidget_8)
        self.siftInputSize.setObjectName(u"siftInputSize")

        self.verticalLayout_25.addWidget(self.siftInputSize)


        self.gridLayout_23.addLayout(self.verticalLayout_25, 3, 0, 1, 1)

        self.siftLoader = QPushButton(self.gridLayoutWidget_8)
        self.siftLoader.setObjectName(u"siftLoader")
        sizePolicy.setHeightForWidth(self.siftLoader.sizePolicy().hasHeightForWidth())
        self.siftLoader.setSizePolicy(sizePolicy)
        self.siftLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_23.addWidget(self.siftLoader, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_23, 1, 0, 1, 1)

        self.tabWidget.addTab(self.SIFT, QString())
        self.Matching = QWidget()
        self.Matching.setObjectName(u"Matching")
        self.gridLayoutWidget_9 = QWidget(self.Matching)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 10, 881, 571))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_23 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalSpacer_24 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_24, 0, 1, 1, 1)

        self.groupBox_21 = QGroupBox(self.gridLayoutWidget_9)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(451, 451))
        self.groupBox_21.setMaximumSize(QSize(451, 451))
        self.matchingImg = ImageView(self.groupBox_21)
        self.matchingImg.setObjectName(u"matchingImg")
        self.matchingImg.setGeometry(QRect(20, 30, 401, 401))
        self.matchingImg.setMinimumSize(QSize(401, 401))
        self.matchingImg.setMaximumSize(QSize(401, 401))

        self.gridLayout_25.addWidget(self.groupBox_21, 0, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_22 = QGroupBox(self.gridLayoutWidget_9)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(251, 261))
        self.groupBox_22.setMaximumSize(QSize(261, 271))
        self.matchingA = ImageView(self.groupBox_22)
        self.matchingA.setObjectName(u"matchingA")
        self.matchingA.setGeometry(QRect(10, 20, 231, 231))
        self.matchingA.setMinimumSize(QSize(231, 231))
        self.matchingA.setMaximumSize(QSize(231, 231))

        self.verticalLayout_19.addWidget(self.groupBox_22)

        self.verticalSpacer_37 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_19.addItem(self.verticalSpacer_37)

        self.groupBox_23 = QGroupBox(self.gridLayoutWidget_9)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(251, 261))
        self.matchingB = ImageView(self.groupBox_23)
        self.matchingB.setObjectName(u"matchingB")
        self.matchingB.setGeometry(QRect(10, 20, 231, 231))
        self.matchingB.setMinimumSize(QSize(231, 231))
        self.matchingB.setMaximumSize(QSize(231, 231))

        self.verticalLayout_19.addWidget(self.groupBox_23)


        self.gridLayout_25.addLayout(self.verticalLayout_19, 0, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_25, 0, 2, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_38 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer_38)

        self.matchingLoaderA = QPushButton(self.gridLayoutWidget_9)
        self.matchingLoaderA.setObjectName(u"matchingLoaderA")

        self.verticalLayout_20.addWidget(self.matchingLoaderA)

        self.verticalSpacer_39 = QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer_39)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.matchingInputAName = QLabel(self.gridLayoutWidget_9)
        self.matchingInputAName.setObjectName(u"matchingInputAName")

        self.verticalLayout_21.addWidget(self.matchingInputAName)

        self.matchingInputASize = QLabel(self.gridLayoutWidget_9)
        self.matchingInputASize.setObjectName(u"matchingInputASize")

        self.verticalLayout_21.addWidget(self.matchingInputASize)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)

        self.verticalSpacer_40 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer_40)

        self.matchingLoaderB = QPushButton(self.gridLayoutWidget_9)
        self.matchingLoaderB.setObjectName(u"matchingLoaderB")

        self.verticalLayout_20.addWidget(self.matchingLoaderB)

        self.verticalSpacer_41 = QSpacerItem(1, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer_41)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.matchingInputBName = QLabel(self.gridLayoutWidget_9)
        self.matchingInputBName.setObjectName(u"matchingInputBName")

        self.verticalLayout_26.addWidget(self.matchingInputBName)

        self.matchingInputBSize = QLabel(self.gridLayoutWidget_9)
        self.matchingInputBSize.setObjectName(u"matchingInputBSize")

        self.verticalLayout_26.addWidget(self.matchingInputBSize)


        self.verticalLayout_20.addLayout(self.verticalLayout_26)

        self.verticalSpacer_42 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self.verticalSpacer_42)

        self.matchingApply_Btn = QPushButton(self.gridLayoutWidget_9)
        self.matchingApply_Btn.setObjectName(u"matchingApply_Btn")

        self.verticalLayout_20.addWidget(self.matchingApply_Btn)

        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_43)


        self.gridLayout_24.addLayout(self.verticalLayout_20, 0, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_25, 0, 3, 1, 1)

        self.tabWidget.addTab(self.Matching, QString())
        self.Thresholding = QWidget()
        self.Thresholding.setObjectName(u"Thresholding")
        self.gridLayoutWidget_10 = QWidget(self.Thresholding)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 10, 897, 570))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_11 = QGroupBox(self.gridLayoutWidget_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(350, 350))
        self.groupBox_11.setMaximumSize(QSize(350, 350))
        self.groupBox_11.setFont(font)
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.groupBox_11.setFlat(False)
        self.threshInput = ImageView(self.groupBox_11)
        self.threshInput.setObjectName(u"threshInput")
        self.threshInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.threshInput.sizePolicy().hasHeightForWidth())
        self.threshInput.setSizePolicy(sizePolicy1)
        self.threshInput.setMinimumSize(QSize(301, 301))
        self.threshInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_5.addWidget(self.groupBox_11)

        self.horizontalSpacer_13 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.groupBox_13 = QGroupBox(self.gridLayoutWidget_10)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.groupBox_13.setMinimumSize(QSize(350, 350))
        self.groupBox_13.setMaximumSize(QSize(350, 350))
        self.groupBox_13.setFont(font)
        self.groupBox_13.setAlignment(Qt.AlignCenter)
        self.threshOutput = ImageView(self.groupBox_13)
        self.threshOutput.setObjectName(u"threshOutput")
        self.threshOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.threshOutput.sizePolicy().hasHeightForWidth())
        self.threshOutput.setSizePolicy(sizePolicy1)
        self.threshOutput.setMinimumSize(QSize(301, 301))
        self.threshOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_5.addWidget(self.groupBox_13)


        self.gridLayout_13.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_13.addItem(self.verticalSpacer_21, 2, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.threshApply_btn = QPushButton(self.gridLayoutWidget_10)
        self.threshApply_btn.setObjectName(u"threshApply_btn")
        self.threshApply_btn.setMinimumSize(QSize(0, 51))
        self.threshApply_btn.setMaximumSize(QSize(201, 16777215))
        self.threshApply_btn.setFont(font1)

        self.horizontalLayout_6.addWidget(self.threshApply_btn)


        self.gridLayout_13.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_13, 1, 2, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.threshInputName = QLabel(self.gridLayoutWidget_10)
        self.threshInputName.setObjectName(u"threshInputName")

        self.verticalLayout_16.addWidget(self.threshInputName)

        self.threshInputSize = QLabel(self.gridLayoutWidget_10)
        self.threshInputSize.setObjectName(u"threshInputSize")

        self.verticalLayout_16.addWidget(self.threshInputSize)


        self.gridLayout_14.addLayout(self.verticalLayout_16, 3, 0, 1, 1)

        self.verticalSpacer3_2 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_14.addItem(self.verticalSpacer3_2, 4, 0, 1, 1)

        self.threshCombo = QComboBox(self.gridLayoutWidget_10)
        self.threshCombo.addItem(QString())
        self.threshCombo.addItem(QString())
        self.threshCombo.addItem(QString())
        self.threshCombo.setObjectName(u"threshCombo")

        self.gridLayout_14.addWidget(self.threshCombo, 5, 0, 1, 1)

        self.freqDomainGroup_2 = QGroupBox(self.gridLayoutWidget_10)
        self.freqDomainGroup_2.setObjectName(u"freqDomainGroup_2")
        self.freqDomainGroup_2.setMinimumSize(QSize(151, 121))
        self.verticalLayoutWidget_8 = QWidget(self.freqDomainGroup_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 20, 131, 91))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.threshGlobal_btn = QRadioButton(self.verticalLayoutWidget_8)
        self.threshGlobal_btn.setObjectName(u"threshGlobal_btn")

        self.verticalLayout_17.addWidget(self.threshGlobal_btn)

        self.threshLocal_btn = QRadioButton(self.verticalLayoutWidget_8)
        self.threshLocal_btn.setObjectName(u"threshLocal_btn")

        self.verticalLayout_17.addWidget(self.threshLocal_btn)

        self.threshTextEdit = QTextEdit(self.verticalLayoutWidget_8)
        self.threshTextEdit.setObjectName(u"threshTextEdit")
        self.threshTextEdit.setEnabled(False)
        self.threshTextEdit.setMaximumSize(QSize(16777215, 31))
        self.threshTextEdit.setAutoFormatting(QTextEdit.AutoNone)
        self.threshTextEdit.setReadOnly(False)
        self.threshTextEdit.setOverwriteMode(True)

        self.verticalLayout_17.addWidget(self.threshTextEdit)


        self.gridLayout_14.addWidget(self.freqDomainGroup_2, 9, 0, 1, 1)

        self.verticalSpacer2_3 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_14.addItem(self.verticalSpacer2_3, 2, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_14.addItem(self.verticalSpacer_22, 0, 0, 1, 1)

        self.verticalSpacer6_2 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_14.addItem(self.verticalSpacer6_2, 8, 0, 1, 1)

        self.threshLoader = QPushButton(self.gridLayoutWidget_10)
        self.threshLoader.setObjectName(u"threshLoader")
        sizePolicy.setHeightForWidth(self.threshLoader.sizePolicy().hasHeightForWidth())
        self.threshLoader.setSizePolicy(sizePolicy)
        self.threshLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_14.addWidget(self.threshLoader, 1, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_23, 12, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_14, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Thresholding, QString())
        self.Segmentaion = QWidget()
        self.Segmentaion.setObjectName(u"Segmentaion")
        self.gridLayoutWidget_11 = QWidget(self.Segmentaion)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(0, 10, 897, 561))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_26 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_26, 1, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_27, 1, 3, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_18 = QGroupBox(self.gridLayoutWidget_11)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMinimumSize(QSize(350, 350))
        self.groupBox_18.setMaximumSize(QSize(350, 350))
        self.groupBox_18.setFont(font)
        self.groupBox_18.setAlignment(Qt.AlignCenter)
        self.groupBox_18.setFlat(False)
        self.segInput = ImageView(self.groupBox_18)
        self.segInput.setObjectName(u"segInput")
        self.segInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.segInput.sizePolicy().hasHeightForWidth())
        self.segInput.setSizePolicy(sizePolicy1)
        self.segInput.setMinimumSize(QSize(301, 301))
        self.segInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_13.addWidget(self.groupBox_18)

        self.horizontalSpacer_28 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_28)

        self.groupBox_24 = QGroupBox(self.gridLayoutWidget_11)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy1.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy1)
        self.groupBox_24.setMinimumSize(QSize(350, 350))
        self.groupBox_24.setMaximumSize(QSize(350, 350))
        self.groupBox_24.setFont(font)
        self.groupBox_24.setAlignment(Qt.AlignCenter)
        self.segOutput = ImageView(self.groupBox_24)
        self.segOutput.setObjectName(u"segOutput")
        self.segOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.segOutput.sizePolicy().hasHeightForWidth())
        self.segOutput.setSizePolicy(sizePolicy1)
        self.segOutput.setMinimumSize(QSize(301, 301))
        self.segOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_13.addWidget(self.groupBox_24)


        self.gridLayout_27.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_27.addItem(self.verticalSpacer_30, 2, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.segApply_btn = QPushButton(self.gridLayoutWidget_11)
        self.segApply_btn.setObjectName(u"segApply_btn")
        self.segApply_btn.setMinimumSize(QSize(0, 51))
        self.segApply_btn.setMaximumSize(QSize(201, 16777215))
        self.segApply_btn.setFont(font1)

        self.horizontalLayout_14.addWidget(self.segApply_btn)


        self.gridLayout_27.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_27, 1, 2, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.verticalSpacer2_7 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_28.addItem(self.verticalSpacer2_7, 2, 0, 1, 1)

        self.verticalSpacer6_3 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_28.addItem(self.verticalSpacer6_3, 6, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_28.addItem(self.verticalSpacer_31, 0, 0, 1, 1)

        self.segLoader = QPushButton(self.gridLayoutWidget_11)
        self.segLoader.setObjectName(u"segLoader")
        sizePolicy.setHeightForWidth(self.segLoader.sizePolicy().hasHeightForWidth())
        self.segLoader.setSizePolicy(sizePolicy)
        self.segLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_28.addWidget(self.segLoader, 1, 0, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.segInputName = QLabel(self.gridLayoutWidget_11)
        self.segInputName.setObjectName(u"segInputName")

        self.verticalLayout_30.addWidget(self.segInputName)

        self.segInputSize = QLabel(self.gridLayoutWidget_11)
        self.segInputSize.setObjectName(u"segInputSize")

        self.verticalLayout_30.addWidget(self.segInputSize)


        self.gridLayout_28.addLayout(self.verticalLayout_30, 3, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_28.addItem(self.verticalSpacer_32, 10, 0, 1, 1)

        self.freqDomainGroup_4 = QGroupBox(self.gridLayoutWidget_11)
        self.freqDomainGroup_4.setObjectName(u"freqDomainGroup_4")
        self.freqDomainGroup_4.setMinimumSize(QSize(151, 145))
        self.verticalLayoutWidget_14 = QWidget(self.freqDomainGroup_4)
        self.verticalLayoutWidget_14.setObjectName(u"verticalLayoutWidget_14")
        self.verticalLayoutWidget_14.setGeometry(QRect(10, 20, 131, 121))
        self.verticalLayout_31 = QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.segKMeans_btn = QRadioButton(self.verticalLayoutWidget_14)
        self.segKMeans_btn.setObjectName(u"segKMeans_btn")

        self.verticalLayout_31.addWidget(self.segKMeans_btn)

        self.segRegionGrowing_btn = QRadioButton(self.verticalLayoutWidget_14)
        self.segRegionGrowing_btn.setObjectName(u"segRegionGrowing_btn")

        self.verticalLayout_31.addWidget(self.segRegionGrowing_btn)

        self.segAgglomerative_btn = QRadioButton(self.verticalLayoutWidget_14)
        self.segAgglomerative_btn.setObjectName(u"segAgglomerative_btn")

        self.verticalLayout_31.addWidget(self.segAgglomerative_btn)

        self.segMeanShift_btn = QRadioButton(self.verticalLayoutWidget_14)
        self.segMeanShift_btn.setObjectName(u"segMeanShift_btn")

        self.verticalLayout_31.addWidget(self.segMeanShift_btn)


        self.gridLayout_28.addWidget(self.freqDomainGroup_4, 7, 0, 3, 1)


        self.gridLayout_26.addLayout(self.gridLayout_28, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Segmentaion, QString())
        self.faceDet_tab = QWidget()
        self.faceDet_tab.setObjectName(u"faceDet_tab")
        self.gridLayoutWidget_12 = QWidget(self.faceDet_tab)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(10, 10, 897, 570))
        self.gridLayout_29 = QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_29, 1, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_30, 1, 3, 1, 1)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_25 = QGroupBox(self.gridLayoutWidget_12)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(350, 350))
        self.groupBox_25.setMaximumSize(QSize(350, 350))
        self.groupBox_25.setFont(font)
        self.groupBox_25.setAlignment(Qt.AlignCenter)
        self.groupBox_25.setFlat(False)
        self.faceDetInput = ImageView(self.groupBox_25)
        self.faceDetInput.setObjectName(u"faceDetInput")
        self.faceDetInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.faceDetInput.sizePolicy().hasHeightForWidth())
        self.faceDetInput.setSizePolicy(sizePolicy1)
        self.faceDetInput.setMinimumSize(QSize(301, 301))
        self.faceDetInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_15.addWidget(self.groupBox_25)

        self.horizontalSpacer_31 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_31)

        self.groupBox_26 = QGroupBox(self.gridLayoutWidget_12)
        self.groupBox_26.setObjectName(u"groupBox_26")
        sizePolicy1.setHeightForWidth(self.groupBox_26.sizePolicy().hasHeightForWidth())
        self.groupBox_26.setSizePolicy(sizePolicy1)
        self.groupBox_26.setMinimumSize(QSize(350, 350))
        self.groupBox_26.setMaximumSize(QSize(350, 350))
        self.groupBox_26.setFont(font)
        self.groupBox_26.setAlignment(Qt.AlignCenter)
        self.faceDetOutput = ImageView(self.groupBox_26)
        self.faceDetOutput.setObjectName(u"faceDetOutput")
        self.faceDetOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.faceDetOutput.sizePolicy().hasHeightForWidth())
        self.faceDetOutput.setSizePolicy(sizePolicy1)
        self.faceDetOutput.setMinimumSize(QSize(301, 301))
        self.faceDetOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_15.addWidget(self.groupBox_26)


        self.gridLayout_30.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_30.addItem(self.verticalSpacer_33, 2, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.faceDetDetect_btn = QPushButton(self.gridLayoutWidget_12)
        self.faceDetDetect_btn.setObjectName(u"faceDetDetect_btn")
        self.faceDetDetect_btn.setMinimumSize(QSize(0, 51))
        self.faceDetDetect_btn.setMaximumSize(QSize(201, 16777215))
        self.faceDetDetect_btn.setFont(font1)

        self.horizontalLayout_16.addWidget(self.faceDetDetect_btn)


        self.gridLayout_30.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_30, 1, 2, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.freqDomainGroup_5 = QGroupBox(self.gridLayoutWidget_12)
        self.freqDomainGroup_5.setObjectName(u"freqDomainGroup_5")
        self.freqDomainGroup_5.setEnabled(True)
        self.freqDomainGroup_5.setMinimumSize(QSize(151, 141))
        self.verticalLayoutWidget_9 = QWidget(self.freqDomainGroup_5)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(3, 20, 151, 113))
        self.verticalLayout_27 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label = QLabel(self.verticalLayoutWidget_9)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(71, 31))

        self.horizontalLayout_19.addWidget(self.label)

        self.faceDetmenuScaleFactor_textEdit = QTextEdit(self.verticalLayoutWidget_9)
        self.faceDetmenuScaleFactor_textEdit.setObjectName(u"faceDetmenuScaleFactor_textEdit")
        self.faceDetmenuScaleFactor_textEdit.setMaximumSize(QSize(61, 23))

        self.horizontalLayout_19.addWidget(self.faceDetmenuScaleFactor_textEdit)


        self.verticalLayout_27.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_2 = QLabel(self.verticalLayoutWidget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(71, 31))

        self.horizontalLayout_20.addWidget(self.label_2)

        self.faceDetmenuMinNei_textEdit = QTextEdit(self.verticalLayoutWidget_9)
        self.faceDetmenuMinNei_textEdit.setObjectName(u"faceDetmenuMinNei_textEdit")
        self.faceDetmenuMinNei_textEdit.setMaximumSize(QSize(61, 23))

        self.horizontalLayout_20.addWidget(self.faceDetmenuMinNei_textEdit)


        self.verticalLayout_27.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_3 = QLabel(self.verticalLayoutWidget_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(71, 31))

        self.horizontalLayout_21.addWidget(self.label_3)

        self.faceDetmenuminSize_textEdit = QTextEdit(self.verticalLayoutWidget_9)
        self.faceDetmenuminSize_textEdit.setObjectName(u"faceDetmenuminSize_textEdit")
        self.faceDetmenuminSize_textEdit.setMaximumSize(QSize(61, 23))

        self.horizontalLayout_21.addWidget(self.faceDetmenuminSize_textEdit)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.gridLayout_31.addWidget(self.freqDomainGroup_5, 7, 0, 1, 1)

        self.faceDetmenu_verticalSpacer_2 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_31.addItem(self.faceDetmenu_verticalSpacer_2, 2, 0, 1, 1)

        self.faceDetmenu_verticalSpacer_1 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_31.addItem(self.faceDetmenu_verticalSpacer_1, 0, 0, 1, 1)

        self.faceDetLoader = QPushButton(self.gridLayoutWidget_12)
        self.faceDetLoader.setObjectName(u"faceDetLoader")
        sizePolicy.setHeightForWidth(self.faceDetLoader.sizePolicy().hasHeightForWidth())
        self.faceDetLoader.setSizePolicy(sizePolicy)
        self.faceDetLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_31.addWidget(self.faceDetLoader, 1, 0, 1, 1)

        self.faceDetmenu_verticalSpacer_4 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.faceDetmenu_verticalSpacer_4, 10, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.faceDetInputName = QLabel(self.gridLayoutWidget_12)
        self.faceDetInputName.setObjectName(u"faceDetInputName")

        self.verticalLayout_18.addWidget(self.faceDetInputName)

        self.faceDetInputSize = QLabel(self.gridLayoutWidget_12)
        self.faceDetInputSize.setObjectName(u"faceDetInputSize")

        self.verticalLayout_18.addWidget(self.faceDetInputSize)


        self.gridLayout_31.addLayout(self.verticalLayout_18, 3, 0, 1, 1)

        self.faceDetmenu_verticalSpacer_3 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_31.addItem(self.faceDetmenu_verticalSpacer_3, 4, 0, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_31, 1, 0, 1, 1)

        self.tabWidget.addTab(self.faceDet_tab, QString())
        self.faceRecog_tab = QWidget()
        self.faceRecog_tab.setObjectName(u"faceRecog_tab")
        self.gridLayoutWidget_13 = QWidget(self.faceRecog_tab)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 10, 897, 570))
        self.gridLayout_32 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_33, 1, 3, 1, 1)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.groupBox_27 = QGroupBox(self.gridLayoutWidget_13)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(350, 350))
        self.groupBox_27.setMaximumSize(QSize(350, 350))
        self.groupBox_27.setFont(font)
        self.groupBox_27.setAlignment(Qt.AlignCenter)
        self.groupBox_27.setFlat(False)
        self.faceRecInput = ImageView(self.groupBox_27)
        self.faceRecInput.setObjectName(u"faceRecInput")
        self.faceRecInput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.faceRecInput.sizePolicy().hasHeightForWidth())
        self.faceRecInput.setSizePolicy(sizePolicy1)
        self.faceRecInput.setMinimumSize(QSize(301, 301))
        self.faceRecInput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_17.addWidget(self.groupBox_27)

        self.horizontalSpacer_34 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_34)

        self.groupBox_28 = QGroupBox(self.gridLayoutWidget_13)
        self.groupBox_28.setObjectName(u"groupBox_28")
        sizePolicy1.setHeightForWidth(self.groupBox_28.sizePolicy().hasHeightForWidth())
        self.groupBox_28.setSizePolicy(sizePolicy1)
        self.groupBox_28.setMinimumSize(QSize(350, 350))
        self.groupBox_28.setMaximumSize(QSize(350, 350))
        self.groupBox_28.setFont(font)
        self.groupBox_28.setAlignment(Qt.AlignCenter)
        self.faceRecOutput = ImageView(self.groupBox_28)
        self.faceRecOutput.setObjectName(u"faceRecOutput")
        self.faceRecOutput.setGeometry(QRect(30, 40, 301, 301))
        sizePolicy1.setHeightForWidth(self.faceRecOutput.sizePolicy().hasHeightForWidth())
        self.faceRecOutput.setSizePolicy(sizePolicy1)
        self.faceRecOutput.setMinimumSize(QSize(301, 301))
        self.faceRecOutput.setMaximumSize(QSize(301, 301))

        self.horizontalLayout_17.addWidget(self.groupBox_28)


        self.gridLayout_33.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_33.addItem(self.verticalSpacer_46, 2, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.faceRecMatch_btn = QPushButton(self.gridLayoutWidget_13)
        self.faceRecMatch_btn.setObjectName(u"faceRecMatch_btn")
        self.faceRecMatch_btn.setMinimumSize(QSize(0, 51))
        self.faceRecMatch_btn.setMaximumSize(QSize(201, 16777215))
        self.faceRecMatch_btn.setFont(font1)

        self.horizontalLayout_18.addWidget(self.faceRecMatch_btn)


        self.gridLayout_33.addLayout(self.horizontalLayout_18, 1, 1, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_33, 1, 2, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(5, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_32, 1, 1, 1, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.faceRecLoader = QPushButton(self.gridLayoutWidget_13)
        self.faceRecLoader.setObjectName(u"faceRecLoader")
        sizePolicy.setHeightForWidth(self.faceRecLoader.sizePolicy().hasHeightForWidth())
        self.faceRecLoader.setSizePolicy(sizePolicy)
        self.faceRecLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_34.addWidget(self.faceRecLoader, 14, 0, 1, 1)

        self.menu_verticalSpacer_2 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_2, 2, 0, 1, 1)

        self.menu_verticalSpacer_3 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_3, 7, 0, 1, 1)

        self.faceRecmenu_verticalLayout_3 = QVBoxLayout()
        self.faceRecmenu_verticalLayout_3.setObjectName(u"faceRecmenu_verticalLayout_3")
        self.faceRecInputName = QLabel(self.gridLayoutWidget_13)
        self.faceRecInputName.setObjectName(u"faceRecInputName")

        self.faceRecmenu_verticalLayout_3.addWidget(self.faceRecInputName)

        self.faceRecInputSize = QLabel(self.gridLayoutWidget_13)
        self.faceRecInputSize.setObjectName(u"faceRecInputSize")

        self.faceRecmenu_verticalLayout_3.addWidget(self.faceRecInputSize)


        self.gridLayout_34.addLayout(self.faceRecmenu_verticalLayout_3, 16, 0, 1, 1)

        self.menu_verticalSpacer_6 = QSpacerItem(17, 17, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_6, 13, 0, 1, 1)

        self.menu_verticalSpacer_7 = QSpacerItem(1, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_7, 15, 0, 1, 1)

        self.faceRecmenu_verticalLayout_2 = QVBoxLayout()
        self.faceRecmenu_verticalLayout_2.setObjectName(u"faceRecmenu_verticalLayout_2")

        self.gridLayout_34.addLayout(self.faceRecmenu_verticalLayout_2, 10, 0, 1, 1)

        self.menu_verticalSpacer_1 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_1, 0, 0, 1, 1)

        self.faceRecmenu_verticalLayout_1 = QVBoxLayout()
        self.faceRecmenu_verticalLayout_1.setObjectName(u"faceRecmenu_verticalLayout_1")
        self.faceRec_trainDSInputName = QLabel(self.gridLayoutWidget_13)
        self.faceRec_trainDSInputName.setObjectName(u"faceRec_trainDSInputName")

        self.faceRecmenu_verticalLayout_1.addWidget(self.faceRec_trainDSInputName)

        self.faceRec_trainDSImages = QLabel(self.gridLayoutWidget_13)
        self.faceRec_trainDSImages.setObjectName(u"faceRec_trainDSImages")

        self.faceRecmenu_verticalLayout_1.addWidget(self.faceRec_trainDSImages)


        self.gridLayout_34.addLayout(self.faceRecmenu_verticalLayout_1, 6, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget_13)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_34.addWidget(self.line, 12, 0, 1, 1)

        self.faceRec_trainDSLoader = QPushButton(self.gridLayoutWidget_13)
        self.faceRec_trainDSLoader.setObjectName(u"faceRec_trainDSLoader")
        sizePolicy.setHeightForWidth(self.faceRec_trainDSLoader.sizePolicy().hasHeightForWidth())
        self.faceRec_trainDSLoader.setSizePolicy(sizePolicy)
        self.faceRec_trainDSLoader.setMaximumSize(QSize(151, 51))

        self.gridLayout_34.addWidget(self.faceRec_trainDSLoader, 1, 0, 1, 1)

        self.menu_verticalSpacer_9 = QSpacerItem(1, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_34.addItem(self.menu_verticalSpacer_9, 21, 0, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_34, 1, 0, 1, 1)

        self.tabWidget.addTab(self.faceRecog_tab, QString())

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Manipulator", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.filterApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.noiseGroup.setTitle(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.noiseUniform_check.setText(QCoreApplication.translate("MainWindow", u"Uniform", None))
        self.noiseGaussian_check.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.noiseSAP_check.setText(QCoreApplication.translate("MainWindow", u"Salt And Pepper", None))
        self.filterInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.filterInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.freqDomainGroup.setTitle(QCoreApplication.translate("MainWindow", u"Frequency Domain Filters", None))
        self.filterLowPass_btn.setText(QCoreApplication.translate("MainWindow", u"Low Pass", None))
        self.filterhighPass_btn.setText(QCoreApplication.translate("MainWindow", u"High pass", None))
        self.filterLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.spatialDomainFiltersGroup.setTitle(QCoreApplication.translate("MainWindow", u"Spatial Domain Filters", None))
        self.lpfGroup.setTitle(QCoreApplication.translate("MainWindow", u"Low Pass Filters", None))
        self.filtersAverage_check.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.filtersGaussian_check.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.filtersMedian_check.setText(QCoreApplication.translate("MainWindow", u"Median", None))
        self.egdeGroup.setTitle(QCoreApplication.translate("MainWindow", u"Edge Detection", None))
        self.edgeSobel_check.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.edgeRoberts_check.setText(QCoreApplication.translate("MainWindow", u"Roberts", None))
        self.edgePrewitt_check.setText(QCoreApplication.translate("MainWindow", u"Prewitt and Canny", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Filters), QCoreApplication.translate("MainWindow", u"Filters", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Output Histogram", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Input Histogram", None))
        self.histLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.histInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.histInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.histEqualCheck.setText(QCoreApplication.translate("MainWindow", u"Equalize Image", None))
        self.histNormCheck.setText(QCoreApplication.translate("MainWindow", u"Normalize Image", None))
        self.histGTCheck.setText(QCoreApplication.translate("MainWindow", u"Global Thresholding", None))
        self.histApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Histograms), QCoreApplication.translate("MainWindow", u"Histograms", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Hybrid Image", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Image A", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Image B", None))
        self.hybridLoaderA.setText(QCoreApplication.translate("MainWindow", u"Load Image A", None))
        self.hybridInputAName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.hybridInputASize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.hybridLoaderB.setText(QCoreApplication.translate("MainWindow", u"Load Image B", None))
        self.hybridInputBName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.hybridInputBSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.mergeBtn.setText(QCoreApplication.translate("MainWindow", u"Make Hybrid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hybrid), QCoreApplication.translate("MainWindow", u"Hybrid", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.houghApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.freqDomainGroup_3.setTitle(QCoreApplication.translate("MainWindow", u"Hough", None))
        self.houghLines_btn.setText(QCoreApplication.translate("MainWindow", u"Lines", None))
        self.houghCircles_btn.setText(QCoreApplication.translate("MainWindow", u"Circles", None))
        self.houghInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.houghInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.houghLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hough), QCoreApplication.translate("MainWindow", u"Hough", None))
        self.contourApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.contourInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.contourInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.contourLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Contour), QCoreApplication.translate("MainWindow", u"Contour", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.cornersApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cornersInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.cornersInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.cornersLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Corners), QCoreApplication.translate("MainWindow", u"Corners", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.siftApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.siftInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.siftInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.siftLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SIFT), QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Hybrid Image", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Image A", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Image B", None))
        self.matchingLoaderA.setText(QCoreApplication.translate("MainWindow", u"Load Image A", None))
        self.matchingInputAName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.matchingInputASize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.matchingLoaderB.setText(QCoreApplication.translate("MainWindow", u"Load Image B", None))
        self.matchingInputBName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.matchingInputBSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.matchingApply_Btn.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Matching), QCoreApplication.translate("MainWindow", u"Matching", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.threshApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.threshInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.threshInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.threshCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Optimal", None))
        self.threshCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Otsu", None))
        self.threshCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Spectral", None))

        self.freqDomainGroup_2.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.threshGlobal_btn.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.threshLocal_btn.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.threshTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.threshTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Block Size", None))
        self.threshLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Thresholding), QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.segApply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.segLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.segInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.segInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.freqDomainGroup_4.setTitle(QCoreApplication.translate("MainWindow", u"Segmenation Method", None))
        self.segKMeans_btn.setText(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.segRegionGrowing_btn.setText(QCoreApplication.translate("MainWindow", u"Region Growing", None))
        self.segAgglomerative_btn.setText(QCoreApplication.translate("MainWindow", u"Agglomerative", None))
        self.segMeanShift_btn.setText(QCoreApplication.translate("MainWindow", u"Mean Shift", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Segmentaion), QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.faceDetDetect_btn.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.freqDomainGroup_5.setTitle(QCoreApplication.translate("MainWindow", u"Presets", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Scale Factor:", None))
        self.faceDetmenuScaleFactor_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Min Neighbors:", None))
        self.faceDetmenuMinNei_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Min Size:", None))
        self.faceDetmenuminSize_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"25", None))
        self.faceDetLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.faceDetInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.faceDetInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.faceDet_tab), QCoreApplication.translate("MainWindow", u"Face Detection", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Image Match", None))
        self.faceRecMatch_btn.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.faceRecLoader.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.faceRecInputName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.faceRecInputSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.faceRec_trainDSInputName.setText(QCoreApplication.translate("MainWindow", u"DS Name:", None))
        self.faceRec_trainDSImages.setText(QCoreApplication.translate("MainWindow", u"Images:", None))
        self.faceRec_trainDSLoader.setText(QCoreApplication.translate("MainWindow", u"Load Training Dataset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.faceRecog_tab), QCoreApplication.translate("MainWindow", u"Face Recognition", None))
    # retranslateUi

