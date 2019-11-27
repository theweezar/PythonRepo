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
x = data.values[:,0].reshape((-1,1))
y = data.values[:,1].reshape((-1,1))

print(f"\nx: \n{x}\n")
# print(f"y: {y}")

xMatrix = np.hstack((np.ones((N,1)),x))
yMatrix = np.hstack((y,np.zeros((N,1))))

print(f"\nxMatrix: \n{xMatrix}\n")
print(f"\nyMatrix: \n{yMatrix}\n")


# w0 = 0, w1 = 1
w = np.array([0,1])
print(f"\nFirst const: \n{w}\n")

iTerate = 100

learning_rate = 0.0001

# r = np.sum(w * xMatrix)

r = w * xMatrix - yMatrix
print(f"r: \n{r}\n")
print(f"Sum r : {np.sum(r)}\n")

while True:
  r = w * xMatrix - yMatrix
  J = 0.5 * math.pow(np.sum(r),2)
  w[0] += 5
  w[1] += 5 
  print(w)
  print(J)
  if J < 10:
    break



# need to debug 

input()
