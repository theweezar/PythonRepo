# Ở đây, mình sẽ minh họa từng bước xử lý ảnh trong deep learning
# để sau này đọc lại có thể hiểu được cách xử lý ảnh trong DL ra sao
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

# 1: Load ảnh

img = cv.imread('pic.jpg')
print(img)