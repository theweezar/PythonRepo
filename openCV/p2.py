
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

class DetectSomething:
  def __init__(self):
    self.cameraOn()

  def toBlackWhite(self,frame):
    r,g,b = cv.split(frame)
    t = r * 0.299 + g * 0.587 + b * 0.114
    return cv.merge((t,t,t))

  def edgeDetection(self,frame):
    k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    return cv.filter2D(frame,0,k)

  def cameraOn(self):
    # frame shape [480,640,3]
    cap = cv.VideoCapture(0)
    isOn = True
    fx = fy = 0
    tx = ty = 0
    # ==================================
    if not cap.isOpened:
      isOn = False
      print("Can't opened camera")
    else:
      ret, frame = cap.read()
      if not ret:
        isOn = False
        print("Something went wrong, can't receive frames !")
      else:
        fy = int(frame.shape[0] / 4)
        fx = int(frame.shape[1] / 4)
        ty = int(frame.shape[0] - fy)
        tx = int(frame.shape[1] - fx)
    # ==================================
    a = 0
    path = "hand"
    if not os.path.exists(path):
      os.mkdir(path)
    else:
      a = len(os.listdir(path))
      print(a)
    # ==================================
    while isOn:
      ret, frame = cap.read()
      if not ret:
        print("Something went wrong, can't receive frames !")
        break
      cv.rectangle(frame,(fx,fy),(tx,ty),(255,0,0))
      pFrame = frame[fy:ty,fx:tx]
      # pFrame = self.toBlackWhite(pFrame)
      # pFrame = self.edgeDetection(pFrame)
      # frame[fy:ty,fx:tx] = pFrame
      cv.imshow('frame',frame)
      if cv.waitKey() == 27:
        break
      elif cv.waitKey() == 32:
        cv.imwrite(f"hand\\hand{a}.jpg",pFrame)
        a += 1


d = DetectSomething()