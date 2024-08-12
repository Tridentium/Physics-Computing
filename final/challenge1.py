# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge1.ui'
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 160, 241, 541))
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
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.label_3.setObjectName("label_3")
        self.inputLayout.addWidget(self.label_3)
        self.launchAngleSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.launchAngleSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid #3256a8;\n"
"height: 8px;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #85c8f2, stop: 1 #1293e3);}\n"
"\n"
"QSlider::handle:horizontal {border: 1px solid #3256a8;\n"
"background: #073191;\n"
"width: 10px;\n"
"height: 10px;\n"
"border-radius: 5px;}")
        self.launchAngleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.launchAngleSlider.setObjectName("launchAngleSlider")
        self.inputLayout.addWidget(self.launchAngleSlider)
        self.launchAngleSliderLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(10)
        self.launchAngleSliderLabel.setFont(font)
        self.launchAngleSliderLabel.setStyleSheet("QLabel {background-color: #a1e4ff;}")
        self.launchAngleSliderLabel.setText("")
        self.launchAngleSliderLabel.setObjectName("launchAngleSliderLabel")
        self.inputLayout.addWidget(self.launchAngleSliderLabel)
        self.launchAngleLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.launchAngleLineEdit.setFont(font)
        self.launchAngleLineEdit.setObjectName("launchAngleLineEdit")
        self.inputLayout.addWidget(self.launchAngleLineEdit)
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
        self.inputLayout.setStretch(2, 1)
        self.inputLayout.setStretch(3, 1)
        self.inputLayout.setStretch(7, 1)
        self.inputLayout.setStretch(8, 2)
        self.inputLayout.setStretch(12, 1)
        self.inputLayout.setStretch(14, 1)
        self.inputLayout.setStretch(18, 1)
        self.inputLayout.setStretch(19, 1)
        self.inputLayout.setStretch(23, 1)
        self.inputLayout.setStretch(24, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 150, 691, 561))
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
        self.listWidget.setGeometry(QtCore.QRect(740, 150, 261, 561))
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
        self.listWidget.raise_()
        self.backButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.infoButton.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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
        self.launchSpeedLabel.setText(_translate("MainWindow", "Launch Speed /ms⁻¹"))
        self.launchSpeedLineEdit.setPlaceholderText(_translate("MainWindow", "Enter launch speed here"))
        self.label_3.setText(_translate("MainWindow", "Launch Angle /°"))
        self.launchAngleLineEdit.setPlaceholderText(_translate("MainWindow", "Enter launch angle here"))
        self.label_4.setText(_translate("MainWindow", "g /ms⁻²"))
        self.setgButton.setText(_translate("MainWindow", "Click to set g to 9.81ms⁻²"))
        self.gLineEdit.setPlaceholderText(_translate("MainWindow", "Enter g here"))
        self.label_5.setText(_translate("MainWindow", "Launch Height /m"))
        self.launchHeightLineEdit.setPlaceholderText(_translate("MainWindow", "Enter launch height here"))
        self.label_6.setText(_translate("MainWindow", "Time Step /ms"))
        self.timeStepLineEdit.setPlaceholderText(_translate("MainWindow", "Enter time step here"))
        self.infoButton.setText(_translate("MainWindow", "Info"))
        self.challengeTitleLabel.setText(_translate("MainWindow", "Challenge 1: Simple Model"))
