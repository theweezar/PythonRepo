# Neural Network

import numpy as np
import pandas as pd

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

# Cách dùng là truyền tham biến là 1 hàm sigmoid luôn, chứ ko phải là 1 hàm pt linear
def dSigmoid(z): 
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
    self.loss = 0

    for i in range(0, len(layers) - 1):
      w = np.random.randn(self.layers[i],self.layers[i+1]) # tham số là 1 shape
      b = np.zeros((self.layers[i+1],1))
      self.w.append(w / self.layers[i]) # có thể không cần chia vẫn được
      self.b.append(b)

    print(f"w:\n{self.w}") 
    print(f"b:\n{self.b}")

  def predict(self, x):
    # sigmoid(Xo * Wo + Xi * Wi + b)
    for i in range(0, len(self.layers) - 1):
      x = sigmoid(np.dot(x,self.w[i]) + self.b[i].T)
    return x

  def calculateLoss(self, x, y):
    yP = self.predict(x)
    return -np.sum(y * np.log(yP) + (1 - y) * np.log(1 - yP))

  def fit(self,x,y):
    A = [x]

    # Feedforward - tức là đi tính xác suất dự đoán vs những hệ số bias có sẵn
    out = A[-1] # out ở khúc này là giá trị input
    # tính những giá trị y predict của từng layer, phần tử cuối là giá trị y predict output
    # ta có thể dùng cho hàm loss function
    for i in range(0, len(self.layers) - 1):
      out = sigmoid(np.dot(out,self.w[i]) + self.b[i].T)
      A.append(out) # append số lần i của out trong này là xác suất của những hidden layer


    # Backpropagation - tức là đạo hàm ngược lại đi qua từng hidden layer để tìm giá trị nhỏ nhất
    # Sau đó set những giá trị nhỏ nhất cho những hệ số bias

    # Mảng A sẽ chứa theo thứ tự: (x-input, hlayer1 tính theo x, output tính theo hlayer1)
    # print(f"A: \n{A}")
    # print(y)
    # A[-1] sẽ là kết quả output
    dA = [-(y - A[-1]) / (A[-1] * (1 - A[-1]))] 
    # cái này là dL/dyP - đạo hàm Loss function theo yP
    dW = []
    dB = []

    # db = 
    # reversed(range(0,3)) -> nghĩa là i bắt đầu từ 2 chứ ko phải từ 3
    # A[i] có thể hiểu là 1 x để tính A[i+1] 
    for i in reversed(range(0, len(self.layers) - 1)):
      db = np.sum(dA[-1] * dSigmoid(A[i+1]),axis = 0).reshape(-1,1)
      # dw = np.sum(A[i] * (dA[-1] * dSigmoid(A[i+1])),axis = 0)
      dw = np.dot(A[i].T,dA[-1] * dSigmoid(A[i+1]))
      # Xi * dA[] * dSigmoid(yP) - có thể dùng 2 cách trên để tính dw
      da = np.dot(dA[-1] * dSigmoid(A[i+1]),self.w[i].T)
      # da = dA[-1] * dSigmoid(A[i+1]) * self.w[i].T 
      dA.append(da)
      dB.append(db)
      dW.append(dw)
    
  
    # Đảo ngược lại để đúng vị trí bias của từng layer
    dW = dW[::-1]
    dB = dB[::-1]

    # print(f"dW:\n {dW}")
    # print(f"dB:\n {dB}")
    for i in range(0, len(self.layers) - 1):
      self.w[i] -= dW[i] * self.alphal
      self.b[i] -= dB[i] * self.alphal

  def train(self,x,y,loop = 100,epoch = 10):
    # epoch là kỷ nguyên, nghĩa là sau bao nhiêu epoch thì kết quả sẽ như nào,ko cần thêm cũng dc :)
    for i in range(0,loop + 1):
      self.fit(x,y)
      if i % epoch == 0:
        print(f"Epoch {i}, Loss: {self.calculateLoss(x, y)}")

    # print(self.w)
    
data = pd.read_csv('dataset.csv').values
x = data[:,0:2]
y = data[:,2].reshape(-1,1)
t = 0.5
# print(x.shape)

nnw = NeuralNetWork([x.shape[1],2,1],0.1)
nnw.train(x,y,loop = 10000,epoch = 100)


while True:
  typeWrong = False
  tInput = input("Nhap Luong - Gio: ")
  if tInput.strip() == "":
    break
  tInput = tInput.split(" ")
  # for e in tInput: 
  #   if e.isdigit() is False:
  #     typeWrong = True
  #     break
  if typeWrong is False: 
    predicted = nnw.predict(np.array([[float(tInput[0]),float(tInput[1])]]))
    print(f"\nPredicted: {predicted}\n")
    if predicted >= t:
      print("Pass")
    else:
      print("Not pass")