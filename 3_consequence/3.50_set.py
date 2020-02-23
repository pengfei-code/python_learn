#set

#set is a special dictionary ,it can be thought of  dict of keys so it  can not be repeat

set1 = set()

set1.add("song")
set1.add("song")
set1.add(112)

print(set1)


# intersection  difference

set2 = set()
set2.add("song")
set2.add(223)

print(set2)

a = set1.intersection(set2)#a&b
print(a)

b = set1.difference(set2)#a-b
print(b)

c = set1|set2
print(c)

