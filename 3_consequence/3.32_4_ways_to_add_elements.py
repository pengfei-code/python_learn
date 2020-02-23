#1 append

a = list()
a.append("february")
a.append("january")
a.append("april")
print(a)

#2 insert

a.insert(2,"march")
print(a)
a.insert(0,0)
print(a)

#3 plus  but  pay attention   there is a new element is generated

a = a+["may","june"]

print(a)


#4 extend

a.extend(["july","august"])
print(a)


#5 multiply

a = a+["aaa"]*3
print(a)
