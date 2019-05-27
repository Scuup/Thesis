#Parser testing continued

from PyQt5.QtCore import pyqtSignal,QThread
from serialComThread import serialThreadClass

class serialDataParser(QThread):
    data=[None]*11
    def __init__(self, parent = None):
        super(serialDataParser,self).__init__(parent)
        #super().__init()
        self.mySerial = serialThreadClass()
        self.mySerial.msg.connect(self.data.append)
        self.mySerial.start()
        
##    def run(self):
##        while True:
##            data = self.serport.readline().strip()
##            data = str(data)
##            listRawData = data.split(',')
##            self.msg.emit(str(listRawData[0:10])) # pipe
##            self.mySerial = serialThreadClass()
##            self.mySerial.msg.connect(self.data.append)
##            self.mySerial.start()
            
##    def send(self):
##        self.mySerial.sendSerial()

#This is for debugging purposes
            
if __name__ =='__main__':
    i=0
    while True:
        if i == 0:
            data=[""]
            mySerial = serialThreadClass()
            mySerial.sendSerial()
            mySerial.start()
            mySerial.msg.connect(data.append)
            i+=1
        print(i)
        print(serialDataParser.data)
