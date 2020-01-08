import random

a = [1,2,3,4,5,6,7,8,9]

for p in range(0,len(a)):
  r = random.randrange(0,len(a))
  t = a[p]
  a[p] = a[r]
  a[r] = t

print(a)