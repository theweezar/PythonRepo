import cv2 as cv
import numpy as np 
import os

def nothing(x):
  pass

class ColorDT:
  def __init__(self):
    cv.namedWindow("track")
    cv.createTrackbar("lH","track",0,255,nothing)
    cv.createTrackbar("lS","track",0,255,nothing)
    cv.createTrackbar("lV","track",0,255,nothing)
    cv.createTrackbar("hH","track",0,255,nothing)
    cv.createTrackbar("hS","track",0,255,nothing)
    cv.createTrackbar("hV","track",0,255,nothing)
    self.cameraOn()

  def cameraOn(self):
    cap = cv.VideoCapture(0)
    isOn = True
    fx = 50
    fy = 100
    dist = 150 #distance
    # Kiểm tra camera
    if not cap.isOpened:
      isOn = False
      print("Can't opened camera")
    else:
      ret, frame = cap.read()
      if not ret:
        isOn = False
        print("Something went wrong, can't receive frames !")
    # Ghi hình
    while isOn:
      ret, frame = cap.read()
      if not ret:
        print("Something went wrong, can't receive frames !")
        break
      # đảo lật hình qua trái để cho giống camera trước
      frame = frame[:,::-1]
      cv.setMouseCallback("Camera",self.mouseClickPixel,param=frame)
      # vẽ cái khung hình chữ nhật có viền màu xanh
      # cv.rectangle(frame,(fx,fy),(fx + dist,fy + dist),(255,0,0),thickness=2)
      # tách cái khung hình bên trong cái hình chữ nhật đó ra để xử lý
      # pFrame = frame[fy:fy+dist,fx:fx+dist]
      pFrame = frame
      pFrame = self.detect(pFrame)
      # print(f"pFrame: \n{pFrame.shape}")
      # show camera
      cv.imshow("Camera",frame)
      cv.imshow("pFrame",pFrame)
      if cv.waitKey(1) == 27:
        break

  def skinColor(self):
    return (np.array([0,20,60]), np.array([20,255,255])) # lower, upper

  def detect(self,frame):
    # frame[0,:]
    # k = 1/9 * np.array([[1,1,1],[1,1,1],[1,1,1]])
    # frame = cv.filter2D(frame,0,k)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lowerColor = np.array([cv.getTrackbarPos('lH',"track"),
                          cv.getTrackbarPos('lS',"track"),
                          cv.getTrackbarPos('lV',"track")])
    upperColor = np.array([cv.getTrackbarPos('hH',"track"),
                          cv.getTrackbarPos('hS',"track"),
                          cv.getTrackbarPos('hV',"track")])
    lowerColor, upperColor = self.skinColor()
    mask = cv.inRange(hsv,lowerColor,upperColor)
    res = cv.bitwise_and(frame,frame,mask=mask)
    return res

  def mouseClickPixel(self,event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONUP:
      px = param[y,x]
      print(f'BGR: {px}')
    else:
      pass



def main():
  c = ColorDT()
  return


if __name__ == "__main__":
  main()