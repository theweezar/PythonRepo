# Linear Regression

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# ta dùng công thức MSE 

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

plt.scatter(x, y)
plt.xlabel('Meter')
plt.ylabel('Price')

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
w = np.array([0, 1])
print(f"\nFirst const: \n{w}\n")

iTerate = 300

learning_rate = 0.0001

# cost = np.hstack((np.zeros((iTerate,1))))

# print(np.sum(y) / N)

for i in range(0,iTerate):
  # r = w * xMatrix - yMatrix
  yP = (w[0] + x * w[1])
  # cost[i] = np.sum(yP) / N
  r = y - yP
  # print(f"y & yP: \n {np.hstack((y,yP))}\n")
  # print(f"r: \n{r}\n")
  # print(f"\nSum abs(r) : {abs(np.sum(r))}\n")
  # print(f"\nSum (r * x) : {np.sum(r * x)}\n")
  loss = np.sum(r * r) / N
  # Loss = 0.5 * abs(np.sum(r)) / N

  print(f"\nLoss: {loss}\n")

  before_w0 = w[0]

  w[0] -= -2 / N * np.sum(r) * learning_rate
  w[1] -= -2 / N * np.sum(r * x) * learning_rate

  print(f"\nw after: {w}\n")

# S = data.values[15][0]

# P = w[1] * S + w[0]

# print(f"\nReality price of S = {S} is {data.values[15][1]}\n")
# print(f"\nPredicted price of S = {S} is {P}\n")

for i in range(0,N):
  S = data.values[i][0]
  P = w[1] * S + w[0]
  print(f"\nReality price of S{i+1} = {S} is {data.values[i][1]}")
  print(f"\nPredicted price of S{i+1} = {S} is {P}\n")

predict = x * w[1] + w[0]

# plt.plot((x.begin,x.end),(y.begin,y.end),'màu') # vẽ đường thẳng - r: red
plt.plot((x[0],x[N-1]),(predict[0],predict[N - 1]),'r') 
plt.show() 

input()
