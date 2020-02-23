#tuple create

#1
a = (20,30,15,17,12)
print(a)
#error 
b = (20)
print(b)
print(type(b))#int not as a tuple
#correct:
b1 = (20,)
print("the b1 is : ",b1)

#2 serializable objects

b = tuple([20,30,50,"a"])
print(b)

c= tuple("hello world")
print(c)
d = tuple(range(3))
print(d)

