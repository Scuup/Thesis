#This will contain the data parse section from the serial to the actual GUI

# Import the serial thread to this file aswell
from serialComThread import serialThreadClass
from PyQt5.QtCore import pyqtSignal,QThread
import time
i=0
rawData =[]




    
        
while i==0:
    mySerial = serialThreadClass()
    mySerial.msg.connect(rawData.append) #pipe location
    mySerial.start()
    mySerial.sendSerial()
    time.sleep(5)  
    print(rawData)

        




##class dataParser():
##    def __init__(self):
##        super().__init__()
##        self.mySerial = serialThreadClass()
##        self.mySerial.msg.connect(self.rawData.append)
##        print("teset")
##        self.mySerial.start()
##    def rawData(self):
##        pass
##    def parsedData(self):
##        pass
##    def bug(self):
##        while True:
##            if i < 1:
##                self.mySerial.sendSerial()
##                print("yet another")
##                i+=1
##            print("another test")
##            print(rawData)

        
#This is for debugging purposes
#if __name__ =='__main__':
  
##    while True:
##        if i < 10:
##            print("another test")
##            print(rawData)
##            i +=1
##def bug():
##    i=0
##    while True:
##        if i < 1:
##            #self.mySerial.sendSerial()
##            print("yet another")
##            i+=1
##        print("another test")
##        print(rawData)
##bug()

