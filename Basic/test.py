import numpy as np
import functools

a = np.array([[1,2,3],[4,1,1],[7,8,9]])

print(a[:,:].argmin(axis=1))