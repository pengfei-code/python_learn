import numpy as np

#median

a = np.array([1,5,2,4,2,6])
print(np.sort(a))
print(np.median(a))
b = np.array([1,5,2,2,6])
print(np.median(b))

c = np.arange(1,13).reshape(3,4)

print(np.median(c))
print(np.median(c,axis=(0)))

#sum max min

print(np.sum(c))
print(np.sum(c,axis=(1)))

print(np.max(c))
print(np.max(c,axis=0))

print(np.min(c))
print(np.min(c,axis=0))

