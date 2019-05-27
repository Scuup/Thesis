#This could be the msg parses file
from picamera import PiCamera
from PyQt5.QtCore import pyqtSignal,QThread

#camera.start_preview(fullscreen=False,window=(100,100,400,600))
class cameraThreadClass(QThread):

    def starPreview(self):
        camera.start_preview(fullscreen=False,window=(100,100,400,600))
