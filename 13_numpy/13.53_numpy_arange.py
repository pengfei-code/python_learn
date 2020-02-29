#range
r = range(10)
print(type(r))
print(r)
for x in r:
    print(x)

#arange

import numpy as np

b = np.arange(1,10,3)
print(type(b))
print(b)

c = np.arange(1,30,2,dtype=float)
print(c)



