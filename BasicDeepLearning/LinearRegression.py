import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


data = pd.read_csv("data_linear.csv") 
# data ở đây là 1 class Object, không phải là list
# data.values sẽ return lại 1 Array gôm các phần tử trong đó theo dạng [][]
print("App is running")

print(data.values)

x = data.values[0][0]
y = data.values[0][1]

# data.shape = (hàng,cột) bên trong file dữ liệu có sẵn
# trong bài này thì có 30 hàng và 2 cột (giá,diện tích)

N = data.shape[0]
# điểm ngẫu nhiên cho trước
w1 = 1
w0 = 0

# sai số cao nhất là +-1
AllowedJ = 1

learning_rate = 0.00001

allow = False
# Đầu tiên ta giữ w0 và tăng w1
while not allow:
  tong = 0
  for d in data.values:
    tong += 0.5 * math.pow((w1 * d[0] - d[1]),2)  
  J = tong * 1 / N
  if J < AllowedJ:
    allow = True
    print(J)
    print(w1)


input()
