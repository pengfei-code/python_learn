#other ways to create numpy
import numpy as np
#zeros
z1 = np.zeros(5,dtype=int)
z2 = np.zeros((5,),dtype = int)

z3 = np.zeros((2,3),dtype=float)

print("z1:\t",z1,"\nz2:",z2,"\nz3:",z3)

#ones

o1 = np.ones((2,3),dtype=int)
print(o1)

#empty

em = np.empty((2,3),dtype =float)
print("em:\t",em)

#linspace
#线性等差分量

l1 = np.linspace(1,10,5)
print("l1",l1)
l2 = np.linspace(1,11,5,endpoint=True)
print("l2",l2)
l3 = np.linspace(1,9,5,endpoint=False)
print("l3",l3)

#logspace
#对数等分分量

lg1 = np.logspace(1,10,10)
print(lg1)
lg2 = np.logspace(1,10,10,base =2)
print(lg2)


