#dict visit

#a list can be thought of as an array

a = dict((("name","songpengfei"),("age","20")))

print(a)

name = a["name"]
print(name)
try:
    print(a["unexists"])
except KeyError:
    print("keyError")
else:
    print("continue")

print(a.get("age"))

print(a.get("unexists"))


b = a.items()
print(b)
#print(b[0])
print(type(b))#dict_item

#traverse  dict_items object
for key,value  in b:
    print ("key :",key,"value:",value)


c = a.keys()
print(c)
for key in c:
    print(key,end= "\t")
d = a.values()
print(d)
for value in d:
    print(value)


