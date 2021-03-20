import numpy as np

# block
fi = np.array([
  [1,1,0,0,1],
  [0,1,0,1,1],
  [0,0,1,0,0],
  [0,0,1,1,1],
  [1,0,0,0,1]
])

# key
key = np.array([
  [0,0,0,1,1],
  [1,1,1,0,1],
  [0,0,0,0,1],
  [0,0,0,1,0],
  [1,1,0,1,0]
])

print('key:\n',key,'\nSum:',key.sum())
print('fi & key:\n',np.bitwise_and(fi, key),'\nSum:',np.bitwise_and(fi, key).sum())
print('fi ^ key:\n',np.bitwise_xor(fi, key),'\nSum:',np.bitwise_xor(fi, key).sum())
