# Neural Network

import numpy as np
import pandas as pd

def sigmode(z):
  return 1 / (1 + np.exp(-z))

# Cách dùng là truyền tham biến là 1 hàm sigmode luôn, chứ ko phải là 1 hàm pt linear
def dSigmode(z): 
  return z * (1 - z)

class NeuralNetWork:
  def __init__(self, layers, alphal):
    # super().__init__()
    # z = b[] + x * w[]
    # alphal là learning rate
    self.layers = layers
    self.alphal = alphal
    self.w = []
    self.b = []

    for i in range(0, len(layers) - 1):
      w = np.random.randn(self.layers[i],self.layers[i+1]) # tham số là 1 shape
      b = np.zeros((self.layers[i+1],1))
      self.w.append(w / self.layers[i]) # có thể không cần chia vẫn được
      self.b.append(b)

    print(f"w:\n{self.w}")
    print(f"b:\n{self.b}")

  def fit(self,x,y):
    A = [x]

    # Feedforward - tức là đi tính xác suất dự đoán vs những hệ số bias có sẵn
    out = A[-1] # out ở khúc này là giá trị input
    for i in range(0, len(self.layers) - 1):
      out = sigmode(np.dot(out,self.w[i]) + self.b[i].T)
      A.append(out) # append số lần i của out trong này là xác suất của những hidden layer

    # Backpropagation - tức là đạo hàm ngược lại đi qua từng hidden layer để tìm giá trị nhỏ nhất
    # Sau đó set những giá trị nhỏ nhất cho những hệ số bias

    print(A)
    print(y)

    dA = y - A[-1]
    dW = []
    dB = []

    for i in reversed(range(0, len(self.layers) - 1)):
      dw = 0 + 2
    
data = pd.read_csv('dataset.csv').values
x = data[:,0:2]
y = data[:,2].reshape(-1,1)
# print(x.shape)

nnw = NeuralNetWork([x.shape[1],2,1],0.1)
nnw.fit(x,y)

# a = [x]
# print(a[-1])