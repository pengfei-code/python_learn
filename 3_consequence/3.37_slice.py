#slice

a = list(range(0,10))
print(a)
b = a[0:10:2]
print(b)

print(a[10:0:-1])

print(a[2::])

#travers

for x in a:
    print(x,end = "\t")
