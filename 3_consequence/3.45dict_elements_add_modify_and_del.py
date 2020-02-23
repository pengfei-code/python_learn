#dict  element add

a = {"name":"songpengfei","age":20}
a["job"]="programmer"
print(a)

#dict del

b = dict((("name","songna"),("hh","sdf"),("bb",23)))

a.update(b)

print("the a update :",a)

#del(a["job1"])
print(a)

a.pop("job")
print(a)

a1 = tuple("sdfsdfsdsdds")
b1 = tuple("sdfsfjksdf")
print(a1,"\t\t",b1)
#print(len(zip(a1,b1)))
a = dict(zip(a1,b1))

while len(a)>0:
    c = a.popitem() 
    print(c)


