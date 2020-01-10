import numpy as np 
import cv2 as cv 

img = cv.imread("pic.jpg")
# chuyển ảnh xám
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# contour nghĩa là những vùng màu giống nhau để track, thí dụ mặc áo màu trắng nó sẽ 
# track cái áo màu trắng, rồi vẽ viền cái frame đó
# threshold là tìm ngưỡng trắng đen - gần trắng thì sẽ gán = 255, gần đen thì gán = 0, 127 ở dưới
# là mức ở giữa
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # 255 / 2 = 127.5
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imshow("img",img)
cv.imshow("thresh",thresh)
cv.waitKey(0)
cv.destroyAllWindows()

