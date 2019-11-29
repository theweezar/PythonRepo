# Logistic regression

import numpy as np 
import pandas as pd 
import math
import matplotlib.pyplot as plt 

data = pd.read_csv("dataset.csv")

N = data.shape[0]

# khởi tạo x,y trong database
x = data.values[:,0:2]
y = data.values[:,2].reshape((-1,1))
w = np.array([0,0.1,0.1])

# print(data.values)

print(f"x[0,1]: \n{x}\n")
print(f"y: \n{y}\n")

learning_rate = 0.001
iTerate = 10

for i in range(0,iTerate):
  yP = 1 / (1 + np.exp(-(w[0] + w[1] * x[:,0] + w[2] * x[:,1])))
  yP = np.reshape(yP,(-1,1))
  # print(f"yP : \n{yP}\n")
  L = -(y * np.log(yP) + (1 - y) * np.log(1 - yP))
  # print(f"L : \n{L}\n")
  # print(f"sum(L) : {np.sum(L)}\n")

  w[0] += np.sum(yP - y) * learning_rate
  w[1] += np.sum(x[:,0] * (yP - y)) * learning_rate 
  w[2] += np.sum(x[:,1] * (yP - y)) * learning_rate

  # w[0] += learning_rate * -np.sum(y * yP * (1 - yP) / yP * math.log(10,math.e) + (1 - y) * (- yP * (1 - yP)) / (1 - yP) * math.log(10,math.e))
  # w[1] += learning_rate * -np.sum(y * x[:,0] * yP * (1 - yP) / yP * math.log(10,math.e) + (1 - y) * (- yP * x[:,0] * (1 - yP)) / (1 - yP) * math.log(10,math.e))
  # w[2] += learning_rate * -np.sum(y * x[:,1] * yP * (1 - yP) / yP * math.log(10,math.e) + (1 - y) * (- yP * x[:,1] * (1 - yP)) / (1 - yP) * math.log(10,math.e))
  
print(f"w after: {w}\n")

salary = 1
hour = 3

yP = 1 / (1 + math.exp(-(w[0] + w[1] * salary + w[2] * hour)))

print(f"\nPredited: {yP}\n")

# plt.scatter(x,y)
# plt.xlabel('Kinh nghiệm (năm)')
# plt.ylabel('Lương (triệu)')


# plt.show()

input()