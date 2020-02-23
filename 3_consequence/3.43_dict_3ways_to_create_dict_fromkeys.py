#dict 3 ways to create a dic
#1
d1 = {"name":"songpengfei","age":"20","job":"programmer"}
# 2 dict
d2 = dict(name = "songna",age = "30",job="accountant")
#3 dict
d3 = dict((("name","hu"),("age","40"),("job","chairman")))

print(d1)
print(d2)
print(d3,end="#")


#zip create
a = ("type","integer")
b = ("length","32")
d4 = dict(zip(a,b))
print(d4)
# zip the number of objects determine the a tuple's length and zip the shortest  tupple determine the count

#总短长

#fromkeys

a = dict.fromkeys(["name","age"])
print(a)

# attention
a1=dict.fromkeys("name","age")
print(a1)
