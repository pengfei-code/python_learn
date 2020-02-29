import numpy as np

a = np.arange(1,13).reshape(3,4)
print(a)

print(np.transpose(a))

a = np.arange(1,25).reshape(2,3,4)
b = np.transpose(a,(1,0,2))
print(a)
print("--------------------")
print(b)

print(b.shape)



