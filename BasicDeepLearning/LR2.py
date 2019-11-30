# Logistic regression

import numpy as np 
import pandas as pd 
import math
import matplotlib.pyplot as plt 

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

data = pd.read_csv("dataset.csv")

N = data.shape[0]

# khởi tạo x,y trong database
# x (thời gian làm việc: x1 - lương: x2)
x = np.hstack((np.ones((N,1)),data.values[:,0:2]))
# y (được vậy hay không 1 | 0)
y = data.values[:,2].reshape((-1,1))
w = np.array([0,0.1,0.1])

# print(data.values)

print(f"x[1,x1,x2]: \n{x}\n")
print(f"y: \n{y}\n")
print(f"w[w0,w1,w2]: {w}\n")

learning_rate = 0.001
iTerate = 1

for i in range(0,iTerate):
  # lấy w[0] + x1*w[1] + x2*w[2] rồi sau đó cộng lại hết với nhau theo từng hàng, rồi bỏ
  # vào hàm sigmoid để yP dc trả về là 1 ma trận
  yP = sigmoid(np.sum(w * x,axis=1).reshape(-1,1))
  print(f"yP : \n{yP}\n")
  
  # print(f"L : \n{L}\n")
  # print(f"sum(L) : {np.sum(L)}\n")

  # w[0] += np.sum(yP - y) * learning_rate
  # w[1] += np.sum(x[:,0] * (yP - y)) * learning_rate 
  # w[2] += np.sum(x[:,1] * (yP - y)) * learning_rate
  
# print(f"w after: {w}\n")

# salary = 1
# hour = 3

# yP = 1 / (1 + math.exp(-(w[0] + w[1] * salary + w[2] * hour)))

# print(f"\nPredited: {yP}\n")

# plt.scatter(x,y)
# plt.xlabel('Kinh nghiệm (năm)')
# plt.ylabel('Lương (triệu)')


# plt.show()

input()