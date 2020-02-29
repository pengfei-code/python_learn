import numpy as np


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])
#hstack
c = np.hstack([a,b])
print(c)
#vstack
d = np.vstack([a,b])
print(d)



a1 = np.arange(1,13).reshape((3,4))
a2 = np.arange(101,113).reshape(3,4)
print(a1)
print(a2)


b1 = np.concatenate([a1,a2],axis=0)
#the 0 means that the arrays merge its children starting at the highest latitude
print(b1)

b2 = np.concatenate([a1,a2],axis=1)
print(b2)


#three degree

a1 = np.arange(1,25).reshape(2,3,4)

print(a1)
print(a1.shape)
a2 = np.arange(101,125).reshape(2,3,4)
print(a2)
print(a2.shape)
print("---------0000-------")
c = np.concatenate([a1,a2],axis=0)
print(c.shape)
print(c)
print("---------1111-------")
c1 = np.concatenate([a1,a2],axis=1)
print(c1.shape)
print(c1)
print("-----------2222----------")
c2 = np.concatenate([a1,a2],axis=2)
print(c2.shape)
print(c2)


