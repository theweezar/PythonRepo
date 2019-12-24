import cv2 as cv
import os
import numpy as np

class ImageProcessing:
  def __init__(self ,imgLink):
    self.img = cv.imread(imgLink)
    self.height = len(self.img)
    self.width = len(self.img[0])
    self.r = np.array(self.img[:,:,0])
    self.g = np.array(self.img[:,:,1])
    self.b = np.array(self.img[:,:,2])

  def toBlackWhite(self):
    t = self.r * 0.299 + self.g * 0.587 + self.b * 0.114
    self.r = self.g = self.b = t
  
  def toYellow(self):
    self.b[:,:] = 255
  
  def saveImage(self ,imgName = ''):
    afterImg = np.hstack((self.r.reshape((-1,1)),self.g.reshape((-1,1)),self.b.reshape((-1,1))))
    afterImg = afterImg.reshape((self.height,self.width,3))
    # print(f"After img data: \n{afterImg}\n")
    cv.imwrite(imgName, afterImg)
    

img = ImageProcessing('pic.jpg')
# img.toBlackWhite()
img.toYellow()
img.saveImage('pic_rw.jpg')