import cv2 as cv
import numpy as np

img = cv.imread('pic.jpg')
print(f"First img data: \n{img}")
height = len(img)
width = len(img[0])

r = np.array(img[:,:,0])
g = np.array(img[:,:,1])
b = np.array(img[:,:,2])

# r[:,0] = r[:,-1]
# print(r[0,:])

afterImg = np.hstack((r.reshape((-1,1)),g.reshape((-1,1)),b.reshape((-1,1))))
print(f"After img data: \n{afterImg}\n")
print(afterImg[:width])
# afterImg = afterImg.reshape((width,height))
# img = img.T
# print(img)
# cv.imwrite('pic_rw.jpg', img)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a.T)