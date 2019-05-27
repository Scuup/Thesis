from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt
import sys
import guiMain
import os
from serialComThread import serialThreadClass
from cameraThread import cameraThreadClass

class MainClass(QMainWindow,guiMain.Ui_MainWindow):
    #this is what was taken away,gui.Ui_MainWindow
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnSendCom.clicked.connect(self.btnSendComEvent)
        self.btnStop.clicked.connect(self.btnStopComEvent)
        self.btnCameraPre.clicked.connect(self.btnCameraStartPre)
        self.btnCameraPreStop.clicked.connect(self.btnCameraStopPre)
        self.btnSaveLog.clicked.connect(self.saveToText)
        self.btnSpeedTest.clicked.connect(self.btnSpeedTestCom)
        self.mySerial = serialThreadClass()
        self.mySerial.start()
        self.mySerial.msg.connect(self.textRec.append)
        
        #THIS WORKS!!! Appends the ID var with this
##        self.storeID =[]
##        self.mySerial.msg.connect(self.storeID.append)


        
        self.checkParse.stateChanged.connect(self.testingthisout)

        
        self.myCamera = cameraThreadClass()
        #self.myCamera.timeNow.connect(self.textTime.append)
        #self.mySerial.start()
        #self.mySerial.start()
        self.myCamera.start()

        self.parserID1 = 0
        
        

        
    def btnSendComEvent(self):
         # Start the serial Thread
##        self.mySerial.msg.connect(self.textRec.append) #pipe location
        #self.mySerial.start()
        self.mySerial.sendSerial()
        print("Starting the serial read")
        #self.myCamera.startPreview()
        #self.myCamera.startRecord()
        self.myCamera.startPreview()
        self.myCamera.startRecord()

        
    def btnStopComEvent(self):
        self.mySerial.sendSerialStop()
        #self.mySerial.msg.disconnect(self.textRec.append)
        print("Stopping the serial read")
        #self.myCamera.stopPreview()
        #self.myCamera.stopRecord()
        self.myCamera.stopPreview()
        self.myCamera.stopRecord()

    def btnCameraStartPre(self):
        #self.myCamera.start()
        self.myCamera.startPreview()
        #self.myCamera.start()
        self.myCamera.startRecord()
        print("camera on")

    def btnCameraStopPre(self):
        #self.myCamera.start()
        
        self.myCamera.stopPreview()
        #self.myCamera.threadactive = False()
        #self.myCamera.stop()
        self.myCamera.stopRecord()
        print("camera off")
        
    def saveToText(self):
        text=self.textRec.toPlainText()+self.textTime.toPlainText()
        fileSaveName = self.lineEditFileName.text()
        #text=self.textRec.toPlainText() + self.textTime.toPlainText()

        print(fileSaveName)
        with open('/home/pi/Desktop/Python_Projects/Simple_Gui/Logs/{}.txt'.format(fileSaveName),'w') as f:
            f.write(text)
        print("saved to file")
        f.close()

        path = '/home/pi/Desktop/Python_Projects/Simple_Gui/Videos/'
        os.rename('{}VidBuf.h264'.format(path),'{}{}.h264'.format(path,fileSaveName))

    def btnSpeedTestCom(self):
        self.mySerial.sendSerialSpeed()

    def testingthisout(self, state):
        if state == Qt.Checked:
            print("Checked")
##            parserID1 = 1
##            print(parserID1)
##            #self.mySerial.parseID1ON()
##            #print(self.storeID)
##            self.storeID =[]
##            #self.mySerial.msg.connect(self.storeID.append)
##            #self.parseTestVar.emit(parserID1)
            self.mySerial.testVar=self.lineEditID.text()
            self.lineEditID.setEnabled(False)
            
        else:
            print("Unchecked")
##            parserID1 = 0
##            print(parserID1)
##            #self.mySerial.parseID1OFF()
##            print(self.storeID)
            self.mySerial.testVar='0'
            self.lineEditID.setEnabled(True)

#This could be the way but dont know how yet...
    def dataChangedfunc(self,msg):
        self.mySerial.msg.connect(self.textRec.append)        


if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()
    

        
