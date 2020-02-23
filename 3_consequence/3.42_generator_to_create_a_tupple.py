#generator

a = (x*2 for x in range(0,10))

print(a)
print(type(a))

#print(list(a))
#s = tuple(a)
#print(s)

#point

print(a.__next__())
print(a.__next__())


