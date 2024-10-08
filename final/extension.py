# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge10.ui'
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
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 1081))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(720, 160, 271, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inputLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.setSpacing(5)
        self.inputLayout.setObjectName("inputLayout")
        self.textModeCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
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
        self.launchSpeedLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
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
        font.setPointSize(10)
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
        self.orbitTimeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.orbitTimeLabel.setFont(font)
        self.orbitTimeLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.orbitTimeLabel.setObjectName("orbitTimeLabel")
        self.inputLayout.addWidget(self.orbitTimeLabel)
        self.orbitTimeSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.orbitTimeSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.orbitTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.orbitTimeSlider.setObjectName("orbitTimeSlider")
        self.inputLayout.addWidget(self.orbitTimeSlider)
        self.orbitTimeSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.orbitTimeSliderLabel.setFont(font)
        self.orbitTimeSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.orbitTimeSliderLabel.setText("")
        self.orbitTimeSliderLabel.setObjectName("orbitTimeSliderLabel")
        self.inputLayout.addWidget(self.orbitTimeSliderLabel)
        self.orbitTimeLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.orbitTimeLineEdit.setFont(font)
        self.orbitTimeLineEdit.setObjectName("orbitTimeLineEdit")
        self.inputLayout.addWidget(self.orbitTimeLineEdit)
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
        self.orbitRadiusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.orbitRadiusLabel.setFont(font)
        self.orbitRadiusLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.orbitRadiusLabel.setObjectName("orbitRadiusLabel")
        self.inputLayout.addWidget(self.orbitRadiusLabel)
        self.orbitRadiusSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.orbitRadiusSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.orbitRadiusSlider.setOrientation(QtCore.Qt.Horizontal)
        self.orbitRadiusSlider.setObjectName("orbitRadiusSlider")
        self.inputLayout.addWidget(self.orbitRadiusSlider)
        self.orbitRadiusSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.orbitRadiusSliderLabel.setFont(font)
        self.orbitRadiusSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.orbitRadiusSliderLabel.setText("")
        self.orbitRadiusSliderLabel.setObjectName("orbitRadiusSliderLabel")
        self.inputLayout.addWidget(self.orbitRadiusSliderLabel)
        self.orbitRadiusLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.orbitRadiusLineEdit.setFont(font)
        self.orbitRadiusLineEdit.setObjectName("orbitRadiusLineEdit")
        self.inputLayout.addWidget(self.orbitRadiusLineEdit)
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
        self.massLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.massLabel.setFont(font)
        self.massLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.massLabel.setObjectName("massLabel")
        self.inputLayout.addWidget(self.massLabel)
        self.setEarthMassButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.setEarthMassButton.setFont(font)
        self.setEarthMassButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 4px;\n"
"    background-color:#b1defa;\n"
"}")
        self.setEarthMassButton.setObjectName("setEarthMassButton")
        self.inputLayout.addWidget(self.setEarthMassButton)
        self.massSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.massSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.massSlider.setOrientation(QtCore.Qt.Horizontal)
        self.massSlider.setObjectName("massSlider")
        self.inputLayout.addWidget(self.massSlider)
        self.massSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.massSliderLabel.setFont(font)
        self.massSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.massSliderLabel.setText("")
        self.massSliderLabel.setObjectName("massSliderLabel")
        self.inputLayout.addWidget(self.massSliderLabel)
        self.massLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.massLineEdit.setFont(font)
        self.massLineEdit.setObjectName("massLineEdit")
        self.inputLayout.addWidget(self.massLineEdit)
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
        self.planetRadiusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.planetRadiusLabel.setFont(font)
        self.planetRadiusLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.planetRadiusLabel.setObjectName("planetRadiusLabel")
        self.inputLayout.addWidget(self.planetRadiusLabel)
        self.setEarthRadiusButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.setEarthRadiusButton.setFont(font)
        self.setEarthRadiusButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 4px;\n"
"    background-color:#b1defa;\n"
"}")
        self.setEarthRadiusButton.setObjectName("setEarthRadiusButton")
        self.inputLayout.addWidget(self.setEarthRadiusButton)
        self.planetRadiusSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.planetRadiusSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.planetRadiusSlider.setOrientation(QtCore.Qt.Horizontal)
        self.planetRadiusSlider.setObjectName("planetRadiusSlider")
        self.inputLayout.addWidget(self.planetRadiusSlider)
        self.planetRadiusSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.planetRadiusSliderLabel.setFont(font)
        self.planetRadiusSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.planetRadiusSliderLabel.setText("")
        self.planetRadiusSliderLabel.setObjectName("planetRadiusSliderLabel")
        self.inputLayout.addWidget(self.planetRadiusSliderLabel)
        self.planetRadiusLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.planetRadiusLineEdit.setFont(font)
        self.planetRadiusLineEdit.setObjectName("planetRadiusLineEdit")
        self.inputLayout.addWidget(self.planetRadiusLineEdit)
        self.Line5_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line5_3.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line5_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line5_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line5_3.setObjectName("Line5_3")
        self.inputLayout.addWidget(self.Line5_3)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
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
        font.setPointSize(10)
        self.timeStepLineEdit.setFont(font)
        self.timeStepLineEdit.setObjectName("timeStepLineEdit")
        self.inputLayout.addWidget(self.timeStepLineEdit)
        self.Line5_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line5_2.setStyleSheet("QFrame {\n"
"    background-color: #838285;\n"
"    min-height:1px;\n"
"    max-height:1px;\n"
"}")
        self.Line5_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line5_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line5_2.setObjectName("Line5_2")
        self.inputLayout.addWidget(self.Line5_2)
        self.maxSimLengthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.maxSimLengthLabel.setFont(font)
        self.maxSimLengthLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.maxSimLengthLabel.setObjectName("maxSimLengthLabel")
        self.inputLayout.addWidget(self.maxSimLengthLabel)
        self.maxSimLengthSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.maxSimLengthSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.maxSimLengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxSimLengthSlider.setObjectName("maxSimLengthSlider")
        self.inputLayout.addWidget(self.maxSimLengthSlider)
        self.maxSimLengthSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.maxSimLengthSliderLabel.setFont(font)
        self.maxSimLengthSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.maxSimLengthSliderLabel.setText("")
        self.maxSimLengthSliderLabel.setObjectName("maxSimLengthSliderLabel")
        self.inputLayout.addWidget(self.maxSimLengthSliderLabel)
        self.maxSimLengthLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maxSimLengthLineEdit.setFont(font)
        self.maxSimLengthLineEdit.setObjectName("maxSimLengthLineEdit")
        self.inputLayout.addWidget(self.maxSimLengthLineEdit)
        self.inputLayout.setStretch(2, 1)
        self.inputLayout.setStretch(3, 1)
        self.inputLayout.setStretch(7, 1)
        self.inputLayout.setStretch(8, 2)
        self.inputLayout.setStretch(12, 1)
        self.inputLayout.setStretch(13, 1)
        self.inputLayout.setStretch(17, 1)
        self.inputLayout.setStretch(19, 1)
        self.inputLayout.setStretch(30, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 150, 661, 541))
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
        self.listWidget.setGeometry(QtCore.QRect(710, 150, 291, 581))
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
        font.setPointSize(22)
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
        self.analyticsListWidget.setGeometry(QtCore.QRect(30, 700, 661, 31))
        self.analyticsListWidget.setStyleSheet("QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #a1e4ff;\n"
"}")
        self.analyticsListWidget.setObjectName("analyticsListWidget")
        self.simEndCauseLabel = QtWidgets.QLabel(self.frame)
        self.simEndCauseLabel.setGeometry(QtCore.QRect(40, 704, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.simEndCauseLabel.setFont(font)
        self.simEndCauseLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.simEndCauseLabel.setObjectName("simEndCauseLabel")
        self.listWidget.raise_()
        self.backButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.infoButton.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.analyticsListWidget.raise_()
        self.simEndCauseLabel.raise_()
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
        self.launchSpeedLabel.setText(_translate("MainWindow", "Satellite Launch Speed /kmh⁻¹"))
        self.launchSpeedLineEdit.setPlaceholderText(_translate("MainWindow", "Enter satellite launch speed here"))
        self.orbitTimeLabel.setText(_translate("MainWindow", "Satellite Orbit Time /mins"))
        self.orbitTimeLineEdit.setPlaceholderText(_translate("MainWindow", "Enter satellite orbit time here"))
        self.orbitRadiusLabel.setText(_translate("MainWindow", "Satellite Orbit Radius /km"))
        self.orbitRadiusLineEdit.setPlaceholderText(_translate("MainWindow", "Enter satellite orbit radius here"))
        self.massLabel.setText(_translate("MainWindow", "Planet Mass /kg"))
        self.setEarthMassButton.setText(_translate("MainWindow", "Set planet mass to Earth\'s"))
        self.massLineEdit.setPlaceholderText(_translate("MainWindow", "Enter planet mass here"))
        self.planetRadiusLabel.setText(_translate("MainWindow", "Planet Radius /km"))
        self.setEarthRadiusButton.setText(_translate("MainWindow", "Set planet radius to Earth\'s"))
        self.planetRadiusLineEdit.setPlaceholderText(_translate("MainWindow", "Enter planet radius here"))
        self.label_6.setText(_translate("MainWindow", "Time Step /s"))
        self.timeStepLineEdit.setPlaceholderText(_translate("MainWindow", "Enter time step here"))
        self.maxSimLengthLabel.setText(_translate("MainWindow", "Max Simulation Length /s"))
        self.maxSimLengthLineEdit.setPlaceholderText(_translate("MainWindow", "Enter max simulation length"))
        self.infoButton.setText(_translate("MainWindow", "Info"))
        self.challengeTitleLabel.setText(_translate("MainWindow", "Extension: Satellite Orbitting a Spherical Planet"))
        self.simEndCauseLabel.setText(_translate("MainWindow", "Simulation End Cause:"))
