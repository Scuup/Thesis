#This could be the msg parses file
#from picamera import PiCamera
import picamera
from PyQt5.QtCore import pyqtSignal,QThread
import datetime as dt

#camera.start_preview(fullscreen=False,window=(100,100,400,600))
class cameraThreadClass(QThread):
    #timeNow = pyqtSignal(str)
    def __init__(self, parent = None):
        super(cameraThreadClass,self).__init__(parent)
        #self.camera = PiCamera()
        self.camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
    def run(self):
        #self.camera.start_preview(fullscreen=False,window=(100,100,400,600))
        while True:
            #cameraTime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            self.camera.annotate_background = picamera.Color('black')
            self.camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            #self.camera.start_preview(fullscreen=False,window=(100,100,400,600))
            #cameraTimestr = str(cameraTime)
            #self.start.emit(cameraTime)
            #self.timeNow.emit(cameraTime)
            
            
        
    def startPreview(self):
        #self.camera.start_preview(fullscreen=False,window=(100,100,400,600))
        self.camera.start_preview(fullscreen=False,window=(100,100,400,600))
        #start = dt.datetime.now()
        self.camera.annotate_background = picamera.Color('black')
        #cameraVar = True
        #self.camera.annotate_text = self.start
        #while True:
        #   self.camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        
    def stopPreview(self):
        self.camera.stop_preview()

    def startRecord(self):
        self.camera.start_recording('/home/pi/Desktop/Python_Projects/Simple_Gui/Videos/VidBuf.h264')
    def stopRecord(self):
        self.camera.stop_recording()
