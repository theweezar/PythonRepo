# Logistic regression

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("dataset.csv")

N = data.shape[0]

# khởi tạo x,y trong database
x = data.values[:,0].reshape((-1,1))
y = data.values[:,1].reshape((-1,1))

print(data.values)


plt.scatter(x,y)
plt.xlabel('Kinh nghiệm (năm)')
plt.ylabel('Lương (triệu)')

plt.show()