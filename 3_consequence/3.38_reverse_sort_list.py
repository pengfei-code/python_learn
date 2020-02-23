#sort

a = [20,10,30,50,15]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#shuffle
import random
random.shuffle(a)
print(a)
random.shuffle(a)
print(a)

#sorted method which is a system  method


b = sorted(a)
print(a)
print(b)

b = sorted(a,reverse=True)
print(a)
print(b)

#reverse iterator

# iterator traverses only once

b = reversed(a)
print(type(b))
for temp  in b:
    print(temp)
b1 = list(b)
print(b1)

    
c = reversed(a)

d = list(c)
print("------------------------")
#print(c)
for temp in d:
    print(temp)
    

#max min

print(max(a))
print(min(a))
    
