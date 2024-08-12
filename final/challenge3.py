# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #ccfcff\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(30, 20, 131, 101))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid;\n"
"    border-radius: 8px;\n"
"    background-color: #a1e4ff;\n"
"}")
        self.backButton.setCheckable(True)
        self.backButton.setObjectName("backButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 160, 241, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inputLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.setSpacing(5)
        self.inputLayout.setObjectName("inputLayout")
        self.textModeCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        self.textModeCheckBox.setFont(font)
        self.textModeCheckBox.setObjectName("textModeCheckBox")
        self.inputLayout.addWidget(self.textModeCheckBox)
        self.Line1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line1.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line1.setObjectName("Line1")
        self.inputLayout.addWidget(self.Line1)
        self.XLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.XLabel.setFont(font)
        self.XLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.XLabel.setObjectName("XLabel")
        self.inputLayout.addWidget(self.XLabel)
        self.XSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.XSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.XSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XSlider.setObjectName("XSlider")
        self.inputLayout.addWidget(self.XSlider)
        self.XSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.XSliderLabel.setFont(font)
        self.XSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.XSliderLabel.setText("")
        self.XSliderLabel.setObjectName("XSliderLabel")
        self.inputLayout.addWidget(self.XSliderLabel)
        self.XLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.XLineEdit.setFont(font)
        self.XLineEdit.setObjectName("XLineEdit")
        self.inputLayout.addWidget(self.XLineEdit)
        self.Line3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line3.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line3.setObjectName("Line3")
        self.inputLayout.addWidget(self.Line3)
        self.YLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.YLabel.setFont(font)
        self.YLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.YLabel.setObjectName("YLabel")
        self.inputLayout.addWidget(self.YLabel)
        self.YSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.YSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.YSlider.setOrientation(QtCore.Qt.Horizontal)
        self.YSlider.setObjectName("YSlider")
        self.inputLayout.addWidget(self.YSlider)
        self.YSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.YSliderLabel.setFont(font)
        self.YSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.YSliderLabel.setText("")
        self.YSliderLabel.setObjectName("YSliderLabel")
        self.inputLayout.addWidget(self.YSliderLabel)
        self.YLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YLineEdit.setFont(font)
        self.YLineEdit.setObjectName("YLineEdit")
        self.inputLayout.addWidget(self.YLineEdit)
        self.Line3_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line3_2.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line3_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line3_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line3_2.setObjectName("Line3_2")
        self.inputLayout.addWidget(self.Line3_2)
        self.launchSpeedLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.launchSpeedLabel.setFont(font)
        self.launchSpeedLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.launchSpeedLabel.setObjectName("launchSpeedLabel")
        self.inputLayout.addWidget(self.launchSpeedLabel)
        self.launchSpeedSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.launchSpeedSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.launchSpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.launchSpeedSlider.setObjectName("launchSpeedSlider")
        self.inputLayout.addWidget(self.launchSpeedSlider)
        self.launchSpeedSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.launchSpeedSliderLabel.setFont(font)
        self.launchSpeedSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.launchSpeedSliderLabel.setText("")
        self.launchSpeedSliderLabel.setObjectName("launchSpeedSliderLabel")
        self.inputLayout.addWidget(self.launchSpeedSliderLabel)
        self.launchSpeedLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.launchSpeedLineEdit.setFont(font)
        self.launchSpeedLineEdit.setInputMask("")
        self.launchSpeedLineEdit.setObjectName("launchSpeedLineEdit")
        self.inputLayout.addWidget(self.launchSpeedLineEdit)
        self.Line2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line2.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line2.setObjectName("Line2")
        self.inputLayout.addWidget(self.Line2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.label_4.setObjectName("label_4")
        self.inputLayout.addWidget(self.label_4)
        self.setgButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.setgButton.setFont(font)
        self.setgButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 4px;\n"
"    background-color:#b1defa;\n"
"}")
        self.setgButton.setObjectName("setgButton")
        self.inputLayout.addWidget(self.setgButton)
        self.gSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.gSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.gSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gSlider.setObjectName("gSlider")
        self.inputLayout.addWidget(self.gSlider)
        self.gSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.gSliderLabel.setFont(font)
        self.gSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.gSliderLabel.setText("")
        self.gSliderLabel.setObjectName("gSliderLabel")
        self.inputLayout.addWidget(self.gSliderLabel)
        self.gLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gLineEdit.setFont(font)
        self.gLineEdit.setObjectName("gLineEdit")
        self.inputLayout.addWidget(self.gLineEdit)
        self.Line4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line4.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line4.setObjectName("Line4")
        self.inputLayout.addWidget(self.Line4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.label_5.setObjectName("label_5")
        self.inputLayout.addWidget(self.label_5)
        self.launchHeightSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.launchHeightSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.launchHeightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.launchHeightSlider.setObjectName("launchHeightSlider")
        self.inputLayout.addWidget(self.launchHeightSlider)
        self.launchHeightSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.launchHeightSliderLabel.setFont(font)
        self.launchHeightSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.launchHeightSliderLabel.setText("")
        self.launchHeightSliderLabel.setObjectName("launchHeightSliderLabel")
        self.inputLayout.addWidget(self.launchHeightSliderLabel)
        self.launchHeightLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.launchHeightLineEdit.setFont(font)
        self.launchHeightLineEdit.setObjectName("launchHeightLineEdit")
        self.inputLayout.addWidget(self.launchHeightLineEdit)
        self.Line5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line5.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line5.setObjectName("Line5")
        self.inputLayout.addWidget(self.Line5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.label_6.setObjectName("label_6")
        self.inputLayout.addWidget(self.label_6)
        self.timeStepSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.timeStepSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.timeStepSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeStepSlider.setObjectName("timeStepSlider")
        self.inputLayout.addWidget(self.timeStepSlider)
        self.timeStepSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.timeStepSliderLabel.setFont(font)
        self.timeStepSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.timeStepSliderLabel.setText("")
        self.timeStepSliderLabel.setObjectName("timeStepSliderLabel")
        self.inputLayout.addWidget(self.timeStepSliderLabel)
        self.timeStepLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeStepLineEdit.setFont(font)
        self.timeStepLineEdit.setObjectName("timeStepLineEdit")
        self.inputLayout.addWidget(self.timeStepLineEdit)
        self.inputLayout.setStretch(17, 1)
        self.inputLayout.setStretch(19, 1)
        self.inputLayout.setStretch(23, 1)
        self.inputLayout.setStretch(24, 1)
        self.inputLayout.setStretch(28, 1)
        self.inputLayout.setStretch(29, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 150, 691, 441))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.graphLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.graphLayout.setContentsMargins(0, 0, 0, 0)
        self.graphLayout.setObjectName("graphLayout")
        self.infoButton = QtWidgets.QPushButton(self.frame)
        self.infoButton.setGeometry(QtCore.QRect(870, 20, 131, 101))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(24)
        self.infoButton.setFont(font)
        self.infoButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid;\n"
"    border-radius: 8px;\n"
"    background-color: #a1e4ff;\n"
"}")
        self.infoButton.setCheckable(True)
        self.infoButton.setObjectName("infoButton")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(740, 150, 261, 581))
        self.listWidget.setStyleSheet("QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #a1e4ff;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 10, 671, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.challengeTitleLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.challengeTitleLabel.setFont(font)
        self.challengeTitleLabel.setAutoFillBackground(False)
        self.challengeTitleLabel.setStyleSheet("QLabel {\n"
"    border: 2px solid;\n"
"    border-radius: 8px;\n"
"    background-color: #73d7ff;\n"
"}")
        self.challengeTitleLabel.setScaledContents(True)
        self.challengeTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.challengeTitleLabel.setWordWrap(True)
        self.challengeTitleLabel.setObjectName("challengeTitleLabel")
        self.verticalLayout_2.addWidget(self.challengeTitleLabel)
        self.analyticsListWidget = QtWidgets.QListWidget(self.frame)
        self.analyticsListWidget.setGeometry(QtCore.QRect(30, 600, 691, 131))
        self.analyticsListWidget.setStyleSheet("QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #a1e4ff;\n"
"}")
        self.analyticsListWidget.setObjectName("analyticsListWidget")
        self.minLaunchSpeedLabel = QtWidgets.QLabel(self.frame)
        self.minLaunchSpeedLabel.setGeometry(QtCore.QRect(40, 610, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.minLaunchSpeedLabel.setFont(font)
        self.minLaunchSpeedLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.minLaunchSpeedLabel.setObjectName("minLaunchSpeedLabel")
        self.minSpeedAngleLabelRad = QtWidgets.QLabel(self.frame)
        self.minSpeedAngleLabelRad.setGeometry(QtCore.QRect(40, 640, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.minSpeedAngleLabelRad.setFont(font)
        self.minSpeedAngleLabelRad.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.minSpeedAngleLabelRad.setObjectName("minSpeedAngleLabelRad")
        self.projFlightTime = QtWidgets.QLabel(self.frame)
        self.projFlightTime.setGeometry(QtCore.QRect(40, 700, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.projFlightTime.setFont(font)
        self.projFlightTime.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.projFlightTime.setObjectName("projFlightTime")
        self.highAngleRad = QtWidgets.QLabel(self.frame)
        self.highAngleRad.setGeometry(QtCore.QRect(330, 640, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.highAngleRad.setFont(font)
        self.highAngleRad.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.highAngleRad.setObjectName("highAngleRad")
        self.minSpeedAngleLabelDeg = QtWidgets.QLabel(self.frame)
        self.minSpeedAngleLabelDeg.setGeometry(QtCore.QRect(40, 670, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.minSpeedAngleLabelDeg.setFont(font)
        self.minSpeedAngleLabelDeg.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.minSpeedAngleLabelDeg.setObjectName("minSpeedAngleLabelDeg")
        self.highAngleDeg = QtWidgets.QLabel(self.frame)
        self.highAngleDeg.setGeometry(QtCore.QRect(330, 670, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.highAngleDeg.setFont(font)
        self.highAngleDeg.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.highAngleDeg.setObjectName("highAngleDeg")
        self.highFlightTime = QtWidgets.QLabel(self.frame)
        self.highFlightTime.setGeometry(QtCore.QRect(330, 700, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.highFlightTime.setFont(font)
        self.highFlightTime.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.highFlightTime.setObjectName("highFlightTime")
        self.lowFlightTime = QtWidgets.QLabel(self.frame)
        self.lowFlightTime.setGeometry(QtCore.QRect(530, 700, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lowFlightTime.setFont(font)
        self.lowFlightTime.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.lowFlightTime.setObjectName("lowFlightTime")
        self.lowAngleDeg = QtWidgets.QLabel(self.frame)
        self.lowAngleDeg.setGeometry(QtCore.QRect(530, 670, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lowAngleDeg.setFont(font)
        self.lowAngleDeg.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.lowAngleDeg.setObjectName("lowAngleDeg")
        self.lowAngleRad = QtWidgets.QLabel(self.frame)
        self.lowAngleRad.setGeometry(QtCore.QRect(530, 640, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lowAngleRad.setFont(font)
        self.lowAngleRad.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.lowAngleRad.setObjectName("lowAngleRad")
        self.highBallLabel = QtWidgets.QLabel(self.frame)
        self.highBallLabel.setGeometry(QtCore.QRect(370, 610, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.highBallLabel.setFont(font)
        self.highBallLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.highBallLabel.setObjectName("highBallLabel")
        self.lowBallLabel = QtWidgets.QLabel(self.frame)
        self.lowBallLabel.setGeometry(QtCore.QRect(580, 610, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lowBallLabel.setFont(font)
        self.lowBallLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.lowBallLabel.setObjectName("lowBallLabel")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(310, 610, 3, 111))
        self.line.setStyleSheet("QFrame {background-color:  #838285; max-width: 1px; min-width:1px;}")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(510, 610, 3, 111))
        self.line_2.setStyleSheet("QFrame {background-color:  #838285; max-width: 1px; min-width:1px;}")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listWidget.raise_()
        self.backButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.infoButton.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.analyticsListWidget.raise_()
        self.minLaunchSpeedLabel.raise_()
        self.minSpeedAngleLabelRad.raise_()
        self.projFlightTime.raise_()
        self.highAngleRad.raise_()
        self.minSpeedAngleLabelDeg.raise_()
        self.highAngleDeg.raise_()
        self.highFlightTime.raise_()
        self.lowFlightTime.raise_()
        self.lowAngleDeg.raise_()
        self.lowAngleRad.raise_()
        self.highBallLabel.raise_()
        self.lowBallLabel.raise_()
        self.line.raise_()
        self.line_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.textModeCheckBox.setText(_translate("MainWindow", "Manual Text Input"))
        self.XLabel.setText(_translate("MainWindow", "X of Target /m"))
        self.XLineEdit.setPlaceholderText(_translate("MainWindow", "Enter X of target here"))
        self.YLabel.setText(_translate("MainWindow", "Y of Target /m"))
        self.YLineEdit.setPlaceholderText(_translate("MainWindow", "Enter Y of target here"))
        self.launchSpeedLabel.setText(_translate("MainWindow", "Launch Speed /ms⁻¹"))
        self.launchSpeedLineEdit.setPlaceholderText(_translate("MainWindow", "Enter launch speed here"))
        self.label_4.setText(_translate("MainWindow", "g /ms⁻²"))
        self.setgButton.setText(_translate("MainWindow", "Click to set g to 9.81ms⁻²"))
        self.gLineEdit.setPlaceholderText(_translate("MainWindow", "Enter g here"))
        self.label_5.setText(_translate("MainWindow", "Launch Height /m"))
        self.launchHeightLineEdit.setPlaceholderText(_translate("MainWindow", "Enter launch height here"))
        self.label_6.setText(_translate("MainWindow", "Time Step /ms"))
        self.timeStepLineEdit.setPlaceholderText(_translate("MainWindow", "Enter time step here"))
        self.infoButton.setText(_translate("MainWindow", "Info"))
        self.challengeTitleLabel.setText(_translate("MainWindow", "Challenge 3: \"Low Ball\" and\n"
"\"High Ball\" Trajectories"))
        self.minLaunchSpeedLabel.setText(_translate("MainWindow", "Min Launch Speed /ms⁻¹:"))
        self.minSpeedAngleLabelRad.setText(_translate("MainWindow", "Min Speed Angle /rad:"))
        self.projFlightTime.setText(_translate("MainWindow", "Time of Flight /s:"))
        self.highAngleRad.setText(_translate("MainWindow", "Angle /rad:"))
        self.minSpeedAngleLabelDeg.setText(_translate("MainWindow", "Min Speed Angle /°:"))
        self.highAngleDeg.setText(_translate("MainWindow", "Angle /°:"))
        self.highFlightTime.setText(_translate("MainWindow", "Flight Time /s:"))
        self.lowFlightTime.setText(_translate("MainWindow", "Flight Time /s:"))
        self.lowAngleDeg.setText(_translate("MainWindow", "Angle /°:"))
        self.lowAngleRad.setText(_translate("MainWindow", "Angle /rad:"))
        self.highBallLabel.setText(_translate("MainWindow", "High Ball"))
        self.lowBallLabel.setText(_translate("MainWindow", "Low Ball"))
