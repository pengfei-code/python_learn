import numpy as np

a = np.arange(1,13)
b = np.split(a,2)
b1,b2 = np.split(a,2)

c = np.split(a,[3,5])
c1,c2,c3 = np.split(a,[3,5])

print(b)
print(c)
print("---b1,b2------")
print(b1,b2)
print("----c1,c2,c3----")
print(c1,c2,c3)

print("----------------------")
a = np.arange(1,17).reshape(4,4)

b = np.split(a,2)

print(b)
print(np.shape(b))

c = np.split(a,2,axis = 1)
print(c)
print(np.shape(c))


print("----------------------")
a = np.arange(1,17).reshape(4,4)
a1,a2 = np.split(a,2)
print(a1,a2)



#vsplit hsplit
print("--------vsplit-----------")
a = np.arange(1,17).reshape(4,4)
a1,a2 = np.vsplit(a,2)
print(a1,a2)
a1,a2 = np.hsplit(a,2)
print(a1,a2)


