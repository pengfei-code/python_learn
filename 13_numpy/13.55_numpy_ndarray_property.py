import numpy as np

#one-digit

od = np.random.randint(0,10,size=5)
print(od)

#two-digit

td = np.random.random(size=(2,3))

print(td)

#three-digit

thd = np.random.random(size=(2,2,3))
print(thd)


#property

print("type:\t",od.dtype,td.dtype,thd.dtype)

print("size:\t",od.size,td.size,thd.size)

print("itemsize:\t",od.itemsize,td.itemsize,thd.itemsize)

print("shape:\t",od.shape,td.shape,thd.shape)

print("ndim:\t",od.ndim,td.ndim,thd.ndim)

print("dtype:\t",od.dtype,td.dtype,thd.dtype)

