import numpy as np
import os
import cv2 as cv
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils

class HandDetection:
  def __init__(self):
    self.x = self.load_data()
    self.y = np.ones((self.x.shape[0],1))
    self.xTrain, self.xVal, self.xTest = self.x[:500], self.x[500:600], self.x[600:700]
    self.yTrain, self.yVal, self.yTest = self.y[:500], self.y[500:600], self.y[600:700]
    self.yTrain[250] = 0
    self.yTrain[257] = 0
    
    # print(self.yTrain)
    self.train()
  
  def load_data(self):
    path = "D:\\file_cua_a_Duc\\datafortrain\\hand"
    listImg = list()
    if not os.path.exists(path):
      print("Don't have data to train !")
    else:
      for fImg in os.listdir(path):
        img = cv.imread(f"{path}\\{fImg}",cv.IMREAD_GRAYSCALE)
        listImg.append(img)
    # biến array list thành array numpy
    listImg = np.asarray(listImg)
    print(listImg.shape)
    return listImg

  def train(self):
    self.xTrain = self.xTrain.reshape((self.xTrain.shape[0],200,200,1))
    self.xVal = self.xVal.reshape((self.xVal.shape[0],200,200,1))
    self.xTest = self.xTest.reshape((self.xTest.shape[0],200,200,1))
    # self.yTrain = np_utils.to_categorical(self.yTrain,1)
    # self.yVal = np_utils.to_categorical(self.yVal,1)
    # self.yTest = np_utils.to_categorical(self.yTest,1)
    model = Sequential()
    # model.add(Conv2D(32,(3,3),activation = "sigmoid",input_shape = (200,200,1)))
    # model.add(Conv2D(32,(3,3),activation = "sigmoid"))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(128,activation='sigmoid'))
    model.add(Dense(1, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
    H = model.fit(self.xTrain,self.yTrain, validation_data = (self.xVal,self.yVal),
                  batch_size=32,epochs=1,verbose=10)

t = HandDetection()
