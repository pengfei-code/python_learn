import numpy as np

a = np.arange(1,25).reshape((2,3,4))

b = np.arange(101,125).reshape((2,3,4))

addR = np.add(a,b)
print(addR)

substractR = np.subtract(b,a)
print(substractR)

a1 = np.arange(1,13).reshape(3,4)
b1 = np.ones((3,4))
b1[0][0] =2
print(np.multiply(a1,b1))
print(np.divide(b1,a1))


#round

r1 = np.array([1,1.2,2.55,123,456.97])
print(np.round(r1))
print(np.ceil(r1))
print(np.floor(r1))

#power

p1 = np.arange(1,11)
print(np.power(p1,2))
#power out

p2 = np.arange(1,11)
y = np.zeros(shape=(20))
np.power(p2,2,out=y[:10])
print(y)


