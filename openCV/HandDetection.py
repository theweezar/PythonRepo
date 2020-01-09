import numpy as np
import os
import cv2 as cv
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils

class HandDetection:
  def __init__(self):
    self.x, self.y = self.loadData()
    # self.y = np.ones((self.x.shape[0],1))
    # [1,0] : vị trí [0] nghĩa là bàn tay, vị trí [1] nghĩa là ko phải
    # self.y = np.hstack((np.ones((self.x.shape[0],1)),np.zeros((self.x.shape[0],1))))
    self.xTrain, self.xVal, self.xTest = self.x[:500], self.x[500:700], self.x[700:900]
    self.yTrain, self.yVal, self.yTest = self.y[:500], self.y[500:700], self.y[700:900]
    self.model = self.train()
    # print(self.yTrain)
    # print(self.y.shape)
    print(self.predict(self.x[1450]))
    print(self.predict(self.x[107]))
    # for i in self.y:
    #   print(i)
  
  def loadData(self):
    # parentPath = "D:\\file_cua_a_Duc\\datafortrain"
    # listDir = os.listdir(parentPath)
    listImg_x = list()
    list_y = list()
    # đoạn code ở dưới này sẽ dành cho Object Detection, trước mắt chúng ta chỉ cần 1 output
    # Tạo 1 array list, để load hết ảnh vào array list đó
    # for d in listDir:
    #   path = f"D:\\file_cua_a_Duc\\datafortrain\\{d}"
    #   for fImg in os.listdir(path):
    #     img = cv.imread(f"{path}\\{fImg}",cv.IMREAD_GRAYSCALE)
    #     listImg_x.append(img)
    #   if len(list_y) == 0:
    #     list_y.append(np.ones((len(listImg_x),1)))
    #   else:
    #     list_y.append(np.zeros((len(os.listdir(path)),1)))

      # if len(list_y) == 0:
      #      
      # else:
      #   for y in list_y:
      # ==============================================

    path_h = "D:\\file_cua_a_Duc\\datafortrain\\hand"
    path_nt = "D:\\file_cua_a_Duc\\datafortrain\\nothing"
    for fImg in os.listdir(path_h):
      img = cv.imread(f"{path_h}\\{fImg}",cv.IMREAD_GRAYSCALE)
      listImg_x.append(img)
    list_y = np.hstack((np.ones((len(os.listdir(path_h)),1)),
                        np.zeros((len(os.listdir(path_h)),1))))
    for fImg in os.listdir(path_nt):
      img = cv.imread(f"{path_nt}\\{fImg}",cv.IMREAD_GRAYSCALE)
      listImg_x.append(img)
    list_y = np.vstack((list_y, 
                        np.hstack((np.zeros((len(os.listdir(path_nt)),1)),
                        np.ones((len(os.listdir(path_nt)),1))))))
    # cái list_y là những hàng [0,1] giữa thằng hand vs nothing, hand bên trái, nothing bên phải
    # biến array list thành array numpy
    listImg_x = np.asarray(listImg_x)
    print(listImg_x.shape)
    
    # Sắp xếp random cái numpy array lại
    
    for p in range(0, len(listImg_x)):
      r = random.randrange(p, listImg_x.shape[0]) # or len(listImg_x)

      tx = listImg_x[p]
      listImg_x[p] = listImg_x[r]
      listImg_x[r] = tx

      ty = list_y[p,:]
      list_y[p,:] = list_y[r,:]
      list_y[r,:] = ty


    return (listImg_x, list_y)

  def train(self):
    # 500,200,200,1
    self.xTrain = self.xTrain.reshape((self.xTrain.shape[0],200,200,1))
    self.xVal = self.xVal.reshape((self.xVal.shape[0],200,200,1))
    self.xTest = self.xTest.reshape((self.xTest.shape[0],200,200,1))
    # self.yTrain = np_utils.to_categorical(self.yTrain,1)
    # self.yVal = np_utils.to_categorical(self.yVal,1)
    # self.yTest = np_utils.to_categorical(self.yTest,1)
    model = Sequential()
    # những hàm .add dưới này là add layer vào model để train
    model.add(Conv2D(32,(3,3),activation = "sigmoid",input_shape = (200,200,1)))
    # model.add(Conv2D(32,(3,3),activation = "sigmoid"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(32,activation='sigmoid'))
    model.add(Dense(2, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
    # verbose có nghĩa là cách hiển thị quá trình training
    # 0 là ko làm gì
    # 1 là hiển thị cái dòng [=============>...............]
    # 2 là hiển thị Epoch 1, ...., Epoch n
    H = model.fit(self.xTrain,self.yTrain, validation_data = (self.xVal,self.yVal),
                  epochs=2,verbose=1,batch_size=32)
    score = model.evaluate(self.xTest,self.yTest,verbose=0)
    print(score)
    return model

  def predict(self, input):
    # input phải là ảnh xám
    yP = self.model.predict(input.reshape(1,200,200,1))
    return yP
    

# t = HandDetection()
