# This is for serial init and also takes care of the
#   send and receive functions

#This could be done so that there is no need for the Qthreading
import serial
import time
from PyQt5.QtCore import pyqtSignal,QThread




class serialThreadClass(QThread):
    msg = pyqtSignal(str)
    listRawData=[None]*11
    
    def __init__(self, parent = None):
        super(serialThreadClass,self).__init__(parent)
        self.serport = serial.Serial()
        self.serport.baudrate = 115200
        self.serport.port ='/dev/ttyUSB0'
        self.serport.open()
        self.parseID1 = str('0')
        self.testVar = str('0')
        
    def run(self):
        while True:
            
            while self.serport.inWaiting() == 0:
                pass
            
            try:
                data = self.serport.readline().strip()
                data = str(data)
                listRawData=[None]*11
                listRawData = data.split(',')
                listRawDataSplit = str(listRawData)
                
                if self.testVar == listRawData[1]:
                    self.msg.emit(data) # pipe
                elif self.testVar == '0':
                    self.msg.emit(data)
                #self.msg.emit(data)



                    
#                self.msg.emit(data)
                
                #THIS WORKS!!! Appends the ID var with this / Just emit D1
##                D1 = listRawData[8]
##                D2 = listRawData[3]
##                self.msg.emit(D1,D2)
                # THIS WORKS for the data parse by ID!!!!
                #if listRawData[8] == '2' and self.parseID1 == '1':
                #self.msg.emit(listRawData) # pipe
                #try:
                 #   if listRawData[8] == '2':
                        #self.msg.emit(listRawData) # pipe
                ##except:
                 #   pass
            except:
                pass

            

            
# The arduino "firmware" has the following functions as of now:
    # a = Send raw data
    # b = Stop all
    # c = Set speed 500
    # d = Set speed 125
    # e = Test speed from functional can bus
    
    def sendSerial(self):
        self.serport.flush()
        time.sleep(1)
        self.serport.write(b'c')
##        time.sleep(1)
##        self.serport.write(b'a')

    def sendSerialStop(self):
        self.serport.flush()
        self.serport.write(b'b')
        self.serport.flush()

    def sendSerialMusicUp(self):
        self.serport.flush()
        self.serport.write(b'h')
        self.serport.flush()

        
    def sendSerialMusicDown(self):
        self.serport.flush()
        self.serport.write(b'i')
        self.serport.flush()

    def sendSerialCruiseUp(self):
        self.serport.flush()
        self.serport.write(b'f')
        self.serport.flush()

    def sendSerialCruiseDown(self):
        self.serport.flush()
        self.serport.write(b'g')
        self.serport.flush()
        
        
#if __name__ =='__main__':
 #   serialThreadClass
 #This can be used for degub purposes importing wont change the name to main
 #running this alone will change to the main....
