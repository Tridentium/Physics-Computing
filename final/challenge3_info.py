# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'challenge3_info.ui'
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 15, 811, 114))
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 150, 951, 531))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.frame.raise_()
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
        self.challengeTitleLabel.setText(_translate("MainWindow", "Challenge 3: \"Low Ball\" and \"High Ball\" Trajectories Info"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "This model calculates the \"low ball\" and \"high ball\" trajectories to a target fixed position (X,Y), using the quadratic formula (on the equation used to calculate Y) to calculate the launch angle. This graph also calculates and displays the trajectory with the lowest launch speed that reaches the target.\n"
"\n"
"Output information is rounded to 5 decimal places where necessary."))
