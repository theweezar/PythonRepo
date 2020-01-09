import cv2 as cv
import numpy as np 
import os 

class ColorDT:
  def __init__(self):
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
      # vẽ cái khung hình chữ nhật có viền màu xanh
      cv.rectangle(frame,(fx,fy),(fx + dist,fy + dist),(255,0,0),thickness=2)
      # tách cái khung hình bên trong cái hình chữ nhật đó ra để xử lý
      pFrame = frame[fy:fy+dist,fx:fx+dist]
      pFrame = self.detect(pFrame)
      print(f"pFrame: \n{pFrame}")
      # show camera
      cv.imshow("Camera",frame)
      cv.imshow("pFrame",pFrame)
      if cv.waitKey(1) == 27:
        break

  def detect(self,frame):
    # k = 1/9 * np.array([[1,1,1],[1,1,1],[1,1,1]])
    # frame = cv.filter2D(frame,0,k)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lowerColor = np.array([18,33,132])
    upperColor = np.array([112,126,83])
    mask = cv.inRange(hsv,lowerColor,upperColor)
    res = cv.bitwise_and(frame,frame,mask=mask)
    return mask




def main():
  c = ColorDT()
  return


if __name__ == "__main__":
  main()