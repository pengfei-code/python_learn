import numpy as np

a = np.arange(1,25)
print(a)

#to [3,8]

b = np.reshape(a,(3,8))

print("b:\t",b)

#to [2,3,4]
bb = np.reshape(b,(2,3,4))

print("b:\t",bb)

#multiple degree to one degree

#0
c0 = bb.reshape(24)
print(c0)
#1
c = bb.reshape(-1)
print(c)
#2
d = np.ravel(bb)
print(d)
#3
e = bb.flatten()
print(e)

