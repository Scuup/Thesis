# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiMain.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSendCom = QtWidgets.QPushButton(self.centralwidget)
        self.btnSendCom.setGeometry(QtCore.QRect(10, 100, 151, 121))
        self.btnSendCom.setObjectName("btnSendCom")
        self.lineEditID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditID.setGeometry(QtCore.QRect(470, 0, 111, 29))
        self.lineEditID.setObjectName("lineEditID")
        self.textRec = QtWidgets.QTextEdit(self.centralwidget)
        self.textRec.setGeometry(QtCore.QRect(170, 100, 441, 301))
        self.textRec.setObjectName("textRec")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(10, 230, 151, 111))
        self.btnStop.setObjectName("btnStop")
        self.btnCameraPre = QtWidgets.QPushButton(self.centralwidget)
        self.btnCameraPre.setGeometry(QtCore.QRect(10, 50, 141, 29))
        self.btnCameraPre.setObjectName("btnCameraPre")
        self.btnCameraPreStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnCameraPreStop.setGeometry(QtCore.QRect(170, 50, 121, 29))
        self.btnCameraPreStop.setObjectName("btnCameraPreStop")
        self.btnSaveLog = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveLog.setGeometry(QtCore.QRect(290, 390, 91, 29))
        self.btnSaveLog.setObjectName("btnSaveLog")
        self.btnSpeedTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnSpeedTest.setGeometry(QtCore.QRect(10, 390, 91, 29))
        self.btnSpeedTest.setObjectName("btnSpeedTest")
        self.checkParse = QtWidgets.QCheckBox(self.centralwidget)
        self.checkParse.setGeometry(QtCore.QRect(440, 40, 95, 27))
        self.checkParse.setObjectName("checkParse")
        self.IDlabel = QtWidgets.QLabel(self.centralwidget)
        self.IDlabel.setGeometry(QtCore.QRect(440, 0, 21, 21))
        self.IDlabel.setObjectName("IDlabel")
        self.textTime = QtWidgets.QTextEdit(self.centralwidget)
        self.textTime.setGeometry(QtCore.QRect(10, 430, 291, 70))
        self.textTime.setObjectName("textTime")
        self.lineEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFileName.setGeometry(QtCore.QRect(170, 390, 113, 29))
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.labelFileName = QtWidgets.QLabel(self.centralwidget)
        self.labelFileName.setGeometry(QtCore.QRect(110, 390, 81, 21))
        self.labelFileName.setObjectName("labelFileName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 20))
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
        self.btnSendCom.setText(_translate("MainWindow", "Send a c"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.btnCameraPre.setText(_translate("MainWindow", "Camera Preview"))
        self.btnCameraPreStop.setText(_translate("MainWindow", "Camera Stop"))
        self.btnSaveLog.setText(_translate("MainWindow", "Save"))
        self.btnSpeedTest.setText(_translate("MainWindow", "Speed Test"))
        self.checkParse.setText(_translate("MainWindow", "Parse ID"))
        self.IDlabel.setText(_translate("MainWindow", "ID:"))
        self.labelFileName.setText(_translate("MainWindow", "File Name:"))

