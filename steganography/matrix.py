import numpy as np

# block
fi = np.array([
  [1,1,0,0,1,0],
  [0,1,0,1,1,0],
  [0,0,1,0,0,1],
  [0,0,1,1,1,0],
  [1,0,0,0,1,1],
  [0,0,1,1,0,1]
])

# key
key = np.array([
  [0,1,0],
  [1,0,1],
  [1,1,0],
])

print(fi)

# print('key:\n',key,'\nSum:',key.sum())
# print('fi & key:\n',np.bitwise_and(fi, key),'\nSum:',np.bitwise_and(fi, key).sum())
# print('fi ^ key:\n',np.bitwise_xor(fi, key),'\nSum:',np.bitwise_xor(fi, key).sum())

# dect_key_1 = np.ones((5,5),dtype=int)

# dect_key_2 = np.zeros((5,5),dtype=int)

# print(dect_key_1)

# print('fi ^ dect_key_1:\n',np.bitwise_xor(fi, dect_key_1))
# print('fi ^ dect_key_2:\n',np.bitwise_xor(fi, dect_key_2))