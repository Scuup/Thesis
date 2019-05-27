# The main file for Cruise Control and maybe for other controls aswell
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
import sys
import CruiseGui
import os
from serialComThread import serialThreadClass

class MainClass(QMainWindow,CruiseGui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # This is a ref. model
        #self.btnSendCom.clicked.connect(self.btnSendComEvent)

        self.btnVolUp.clicked.connect(self.sendVolUp)
        self.btnVolDown.clicked.connect(self.sendVolDown)
        self.btnCruiseUp.clicked.connect(self.sendCruiseUp)
        self.btnCruiseDown.clicked.connect(self.sendCruiseDown)
        self.btnOpenCan.clicked.connect(self.startCAN)
        self.btnCloseCan.clicked.connect(self.stopCAN)
        
        print("Init Ok")
        
        self.mySerial = serialThreadClass()
        self.mySerial.start()

#This is the ref. function, see above
##def btnSendComEvent(self):
##    self.mySerial.start()
##    self.mySerial.sendSerial()
##    print("Starting the serial read")

    def sendVolUp(self):
        print("I will send the following command to can: Music Volume up")
        self.mySerial.sendSerialMusicUp()
    def sendVolDown(self):
        print("I will send the following command to can: Music Volume down")
        self.mySerial.sendSerialMusicDown()
    def sendCruiseUp(self):
        print("I will send the following command to can: Cruise Speed up")
        self.mySerial.sendSerialCruiseUp()        
    def sendCruiseDown(self):
        print("I will send the following command to can: Cruise Speed Down")
        self.mySerial.sendSerialCruiseDown()
    def startCAN(self):
        print("I will send the following command to can: Start Can")
        self.mySerial.sendSerial()
    def stopCAN(self):
        print("I will send the following command to can: Stop Can")
        self.mySerial.sendSerialStop()
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()
