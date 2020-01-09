
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
from .HandDetection import HandDetection as HD

class DetectSomething:
  def __init__(self):
    self.mode = int(input("1. Take Image Mode\n2. Detection Mode\nOption: "))
    if self.mode == 1:
      self.lenList, self.path = self.checkFolder()
    elif self.mode == 2:
      self.lenList = self.path = None
      self.hd = HD()
    else:
      exit(self)
    print(self.lenList)
    print(self.path)
    self.cameraOn()

  def toBlackWhite(self,frame):
    r,g,b = cv.split(frame)
    t = r * 0.299 + g * 0.587 + b * 0.114
    return cv.merge((t,t,t))

  def edgeDetection(self,frame):
    k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    return cv.filter2D(frame,0,k)

  def checkFolder(self):
    l = 0
    e = False # Exist
    path = "D:\\file_cua_a_Duc\\datafortrain"#\\hand"
    print("List dir already existed:")
    listdir = os.listdir(path)
    # in ra các thư mục trong folder datafortrain
    for name in listdir:
      print(name)
    dirname = input("Which dir do you choose? Or you can create a new one: ").lower()
    path = f"{path}\\{dirname}"
    if not os.path.exists(path):
      os.mkdir(path)
    else:
      l = len(os.listdir(path))
    return (l,path)

  def processing(self, frame):
    if self.mode == 1: # 1 là chế độ chụp ảnh
      if cv.waitKey(0) == 27:
        exit(self)
      elif cv.waitKey(0) == ord("c"):
        if self.lenList < 750:
          cv.imwrite(f"{self.path}\\{os.path.basename(self.path)}{self.lenList}.jpg",frame)
          self.lenList += 1
        else:
          print("Can't take more image in folder")
    else:
      if cv.waitKey(0) == 27:
        exit(self)
      else:
        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        predict = self.hd.predict(frame.reshape(1,200,200,1))
        # print(predict)
        if predict[0][0] >= 0.8:
          print("Hand detected")
        else:
          print("No hand")

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
    while isOn:
      ret, frame = cap.read()
      if not ret:
        print("Something went wrong, can't receive frames !")
        break
      cv.rectangle(frame,(fx,fy),(tx,ty),(255,0,0))
      pFrame = frame[fy:ty,fx:tx]
      # pFrame = self.toBlackWhite(pFrame)
      pFrame = self.edgeDetection(pFrame)
      frame[fy:ty,fx:tx] = pFrame
      cv.imshow('frame',frame)
      pFrame = cv.resize(pFrame,(200,200))
      self.processing(pFrame)
        

# nếu chạy file này thì chạy cái nào trước - giống main
if __name__ == "__main__": 
  d = DetectSomething()