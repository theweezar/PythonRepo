import cv2 as cv
import numpy as np

def nothing(x):
  pass

class colorPK:
  def __init__(self):
    cv.namedWindow('image')
    # create trackbars for color change
    # RGB
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    # HSV
    cv.createTrackbar('H','image',0,255,nothing)
    cv.createTrackbar('S','image',0,255,nothing)
    cv.createTrackbar('V','image',0,255,nothing)
    cv.createTrackbar('HSV', 'image',0,1,nothing)
    self.run()

  def run(self):
    img = np.zeros((300,512,3), np.uint8)
    while True:
      cv.imshow('image',img)
      k = cv.waitKey(1) & 0xFF
      if k == 27:
        break

      # get current positions of four trackbars

      cMode = cv.getTrackbarPos('HSV','image')
      if cMode == 0:
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        img[:] = [b,g,r]
      elif cMode == 1:
        h = cv.getTrackbarPos('H','image')
        s = cv.getTrackbarPos('S','image')
        v = cv.getTrackbarPos('V','image')
        img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        img[:] = [h,s,v]


if __name__ == "__main__":
  c = colorPK()