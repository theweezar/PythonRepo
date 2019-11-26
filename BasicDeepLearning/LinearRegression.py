import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

data = pd.read_csv("data_linear.csv")
print(data.values)
# data ở đây là 1 class Object, không phải là list
# data.values sẽ return lại 1 Array gôm các phần tử trong đó theo dạng [][]

# Số lượng dữ liệu đầu vào
N = data.shape[0] 

# Khởi tạo ma trận 1 x N (1 row - N col), sau đó đảo nó thành ma trận N x 1 (N row - 1 col)
x = data.values[:,0].reshape((-1,1))
y = data.values[:,1].reshape((-1,1))

print(f"\nx: \n{x}\n")
# print(f"y: {y}")

xMatrix = np.hstack((np.zeros((N,1)),x))

print(f"\nxMatrix: \n{xMatrix}\n")

# w0 = 0, w1 = 1
w = np.array([0,1]).reshape(-1,1)
print(f"\nFirst const: \n{w}\n")

i = 100

learning_rate = 0.000001

cost = np.zeros((i,1))

for i in range(1,i):
  r = np.dot(x,w) - y
  cost[i] = 0.5 * np.sum(r*r)
  w[0] -= learning_rate * np.sum(r)
  w[1] -= learning_rate * np.sum(np.matmul(r,x[:,1].reshape((-1,1))))
  print(cost[i])

predict = np.dot(x,w)

x1 = 50
y1 = w[0] + w[1] * 50

print(f"\nThe price is {y1}")

# need to debug 

input()
