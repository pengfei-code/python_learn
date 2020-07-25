#del

a = ["white","green","yellow"]
print(a)
del a[1]
print(a)

a = list("sdfjpqweruzcvm")

#pop
b = a.pop()
print("the b is :",b)
print("the a is :",a)

b = a.pop(1)
print(a)


#remove  if the list contains multiple element  then the method of remove will remove the first element and retain others
a.extend(["a","b","c"]*3)
a.remove("a")
print(a)

