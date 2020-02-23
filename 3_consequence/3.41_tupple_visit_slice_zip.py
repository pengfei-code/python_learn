#tupple visit

a = tuple("asjkzzoqpwwerzxcvxcv234")
print(a)
print(a[2])

#len

print(len(a))


#slice

b = a[2:3:2]

print(b)

#in
print("s" in a)

print(sum(tuple(range(0,10))))

print(max(tuple(range(2,15))))

#zip object

c = ("monday","tuesday","wednesday")
d = tuple(range(0,10))
e = tuple("hello china!")
f = zip(c,d,e)
print(f)
print(type(f))
g = list(f)
print(g)

#zip 1
c1 = [10,20,30]
c2 = [25,31,32]
c3 =["a","b","c"]
d1 = zip(c1,c2,c3)
print(list(d1))

#zip3
print(list(zip(d,e,c,c1,c2,c3)))
f1 =(11,)
print(list(zip(d,e,c,c1,c2,c3,f1)))



