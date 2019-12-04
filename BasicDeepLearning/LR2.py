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

learning_rate = 0.01
iTerate = 1000

for i in range(0,iTerate):
  # lấy w[0] + x1*w[1] + x2*w[2] rồi sau đó cộng lại hết với nhau theo từng hàng, rồi bỏ
  # vào hàm sigmoid để yP dc trả về là 1 ma trận
  yP = sigmoid(np.sum(w * x,axis=1).reshape(-1,1))
  # print(f"yP : \n{yP}\n")

  loss = -np.sum(y * np.log(yP) + (1 - y) * np.log(1 - yP)) / N
  
  print(f"Loss : {loss}")

  r = y - yP
  # print(f"r: \n{r}")
  w[0] -= - np.sum(r) * learning_rate 
  w[1] -= - np.sum(x[:,1].reshape((-1,1)) * (r)) * learning_rate
  w[2] -= - np.sum(x[:,2].reshape((-1,1)) * (r)) * learning_rate

  # print(f"x[:,1]: \n{x[:,1]}")
  
# w *= -1
print(f"w after: {w}\n")

salary = 4
hour = 3

yP = 1 / (1 + math.exp(-(w[0] + w[1] * salary + w[2] * hour)))

print(f"\nPredited: {yP}\n")
# quét hết 1 cột data, cột nào có pass = 1 thì gán vào xAllowed và ngược lại thì gán vào xDenied
xAllowed = data.values[:,0:3][data.values[:,2] == 1] 
xDenied = data.values[:,0:3][data.values[:,2] == 0]

plt.scatter(xAllowed[:,0],xAllowed[:,1],color='red',label='Allowed')
plt.scatter(xDenied[:,0],xDenied[:,1],color='blue',label='Denied')
plt.legend(loc=1)

plt.xlabel('Lương (triệu)')
plt.ylabel('Kinh nghiệm (năm)')

t = 0.5
plt.plot((4, 10),(-(w[0]+4*w[1]+ np.log(1/t-1)) / w[2], -(w[0] + 10*w[1]+ np.log(1/t-1)) / w[2]), 'g')

plt.show()

input()