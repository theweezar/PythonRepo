# Linear Regression

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

data = pd.read_csv("data_linear.csv")
print(data.values)
# data ở đây là 1 class Object, không phải là list
# data.values sẽ return lại 1 Array gôm các phần tử trong đó theo dạng [][]

# Số lượng dữ liệu đầu vào
N = data.shape[0] 

# Khởi tạo ma trận 1 x N (1 row - N col), sau đó đảo nó thành ma trận N x 1 (N row - 1 col)

# dữ liệu diện tích 
x = data.values[:,0].reshape((-1,1))
# dữ liệu giá nhà thực tế
y = data.values[:,1].reshape((-1,1))

print(f"\nx: \n{x}\n")
print(f"\ny: \n{y}\n")

# [[1,S1]
#  [...]
#  [1,Sn]]
xMatrix = np.hstack((np.ones((N,1)),x))

# [[0,P1]
#  [...]
#  [0,Pn]]
yMatrix = np.hstack((y,np.zeros((N,1))))

print(f"\nxMatrix: \n{xMatrix}\n")
print(f"\nyMatrix: \n{yMatrix}\n")


# w0 = 0, w1 = 1
w = np.array([0,1])
print(f"\nFirst const: \n{w}\n")

iTerate = 10

learning_rate = 0.0001

# r = np.sum(w * xMatrix)

for i in range(1,iTerate):
  r = w * xMatrix - yMatrix
  print(f"r: \n{r}\n")
  print(f"\nSum abs(r) : {abs(np.sum(r))}\n")

# theo công thức trên mạng thì Loss phải nhân thêm 0.5
  Loss = 0.5 * math.pow(np.sum(r),2) / N
  # Loss = 0.5 * abs(np.sum(r)) / N

  print(f"\nLoss: {Loss}\n")

  before_w0 = w[0]

  w[0] += abs(-(np.sum(r[:,1] - y) / N)) * learning_rate
  # w[0] += abs(np.sum(r) * learning_rate / N)
  # w[1] += ((np.sum(y) - N * before_w0) / np.sum(x)) * learning_rate 
  w[1] += abs(np.sum(x * r) * learning_rate / N)
  print(f"\nw after: {w}\n")

S = data.values[5][0]

P = w[1] * S + w[0]

print(f"\nReality price of S = {S} is {data.values[5][1]}\n")
print(f"\nPredicted price of S = {S} is {P}\n")

# need to debug 

input()
