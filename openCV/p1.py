import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessing:
  def __init__(self ,imgLink):
    # Original Image - hình gốc
    self.img = cv.imread(imgLink)
    # Result Image - hình kết quả 
    self.rsImg = self.img
    # Size of matrix - kích thước ma trận
    self.height = len(self.img)
    self.width = len(self.img[0])
    # Original RGB channel - channel RGB gốc
    self.oR = np.array(self.img[:,:,0])
    self.oG = np.array(self.img[:,:,1])
    self.oB = np.array(self.img[:,:,2])
    # Calculated RGB channel - channel RGB sau khi được tính toán
    self.cR = self.oR
    self.cG = self.oG
    self.cB = self.oB

  def reset(self):
    # print('After Reset:\n')
    self.cR = self.oR
    self.cG = self.oG
    self.cB = self.oB
    self.rsImg = self.img
    # print(self.cRGB)

  def toBlackWhite(self):
    t = self.cR * 0.299 + self.cG * 0.587 + self.cB * 0.114
    self.cR = self.cG = self.cB = t
    self.setResultImage()
  
  def toYellow(self):
    self.cB[:,:] = 255 / 2
    self.setResultImage()

  def edgeDetection(self):
    k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    result = cv.filter2D(self.img,0,k)
    self.setResultImage(rsImg = result)

  def setResultImage(self, rsImg = None):
    if rsImg is None:
      afterImg = np.hstack((self.cR.reshape((-1,1)),
                          self.cG.reshape((-1,1)),
                          self.cB.reshape((-1,1))))
      afterImg = afterImg.reshape((self.height,self.width,3))
      self.rsImg = afterImg
    else:
      self.rsImg = rsImg
  
  def saveImage(self ,imgName = 'output.jpg'):
    # Tên mặc định của hình là output.jpg
    cv.imwrite(imgName, self.rsImg)

  
    

img = ImageProcessing('pic.jpg')
# img.toBlackWhite()
# img.saveImage('pic_rw_1.jpg')
# img.reset()
# img.toYellow()
# img.saveImage('pic_rw_2.jpg')
# img.reset()
img.edgeDetection()
img.saveImage('kernel.jpg')