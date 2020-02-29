#ndarray
import  numpy as np

a = np.arange(10)

print(type(a))

print(a)


b = [3,6,9]

import math


sqrt_num = []
for b_son in b:
    sqrt_num.append(math.sqrt(b_son))
    pass

for sqrt_num_son in sqrt_num:
    print(sqrt_num_son)
    pass

t = np.sqrt(a)
print(t)