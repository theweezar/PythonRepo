import cv2 as cv
import numpy as np 
import os
# https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
def nothing(x):
  pass

class ColorDT:
  def __init__(self,opt):
    # Option
    self.opt = opt 
    if opt == 1:
      cv.namedWindow("track")
      cv.createTrackbar("lH","track",0,179,nothing)
      cv.createTrackbar("lS","track",0,255,nothing)
      cv.createTrackbar("lV","track",0,255,nothing)
      cv.createTrackbar("hH","track",0,179,nothing)
      cv.createTrackbar("hS","track",0,255,nothing)
      cv.createTrackbar("hV","track",0,255,nothing)
    self.cameraOn()

  def cameraOn(self):
    cap = cv.VideoCapture(0)
    isOn = True
    fx = 50
    fy = 100
    dist = 150 #distance
    background = None
    # Kiểm tra camera
    if not cap.isOpened:
      isOn = False
      print("Can't opened camera")
    else:
      ret, frame = cap.read()
      if not ret:
        isOn = False
        print("Something went wrong, can't receive frames !")
    
    # ghi hình backgroud để trong loop là vì lúc camera bắt đầu, nó cần thời gian để lấy nét
    print("Capturing backgroud.....")
    for i in range(0,100): 
      ret, background = cap.read()
      if not ret:
        print("Something went wrong, can't receive frames !")
        isOn = False
        break

    # Ghi hình - bắt đầu
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
      pFrame = self.detect(pFrame,background=background)
      # print(f"pFrame: \n{pFrame.shape}")
      # show camera
      cv.imshow("Camera",frame)
      cv.imshow("pFrame",pFrame)
      if cv.waitKey(1) == 27:
        break

  def skinColor(self):
    return (np.array([0,48,80]), 
            np.array([20,255,255])) # lower, upper

  def redColorLower(Self):
    return (np.array([0,120,70]),
            np.array([10,255,255]))

  def redColorUpper(self):
    return (np.array([160,120,70]),
            np.array([180,255,255]))

  def blueColor(self):
    return (np.array([110,50,50]),
            np.array([130,255,255]))

  def customColor(self):
    return (np.array([cv.getTrackbarPos('lH',"track"),
                      cv.getTrackbarPos('lS',"track"),
                      cv.getTrackbarPos('lV',"track")]),
            np.array([cv.getTrackbarPos('hH',"track"),
                      cv.getTrackbarPos('hS',"track"),
                      cv.getTrackbarPos('hV',"track")]))

  def detect(self,frame,background = None):
    # frame[0,:]
    # k = 1/9 * np.array([[1,1,1],[1,1,1],[1,1,1]])
    # frame = cv.filter2D(frame,0,k)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lowerColor = upperColor = 0
    mask = None
    if self.opt == 1:
      lowerColor, upperColor = self.customColor()
      mask = cv.inRange(hsv,lowerColor,upperColor)
    elif self.opt == 2:
      lowerColor, upperColor = self.skinColor()
      mask = cv.inRange(hsv,lowerColor,upperColor)
    elif self.opt == 3:
      # Cách xác định rõ màu đỏ
      lowerColor, upperColor = self.redColorLower()
      mask1 = cv.inRange(hsv,lowerColor,upperColor)
      lowerColor, upperColor = self.redColorUpper()
      mask2 = cv.inRange(hsv,lowerColor,upperColor)
      # mask cuối cùng sẽ là mask có màu đỏ rõ nhất
      mask = mask1 + mask2
      # làm cho màu đỏ smooth hơn
      mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3,3),np.uint8))
      # tô viền cho màu đỏ đó
      # mask = cv.morphologyEx(mask, cv.MORPH_DILATE, np.ones((3,3),np.uint8))
      
    elif self.opt == 4:
      lowerColor, upperColor = self.blueColor()
      mask = cv.inRange(hsv,lowerColor,upperColor)
    else:
      exit(self)
      
    res = cv.bitwise_and(frame,frame,mask=mask)

    return res

  def mouseClickPixel(self,event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONUP:
      px = param[y,x]
      print(f'BGR: {px}')
      pxHSV = cv.cvtColor(np.uint8([[px]]),cv.COLOR_BGR2HSV)
      print(f'HSV: {pxHSV}')

    else:
      pass



def main():
  i = input("1. Custom color\n2. Skin color\n3. Red color\n4. Blue color\nChoose: ")
  if i.strip().isdigit() is True:
    c = ColorDT(int(i))
  return


if __name__ == "__main__":
  main()