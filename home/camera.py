from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np

class LiveWebCam(object):
	def __init__(self):
		self.url = cv2.VideoCapture("http://25.109.170.250:8080/video")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (540, 380), interpolation = cv2.INTER_LINEAR) 
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
