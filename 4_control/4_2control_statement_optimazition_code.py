#very important
#loop code optimization

#1: minimize the caculation within the loop
#2:In the  nested loop ,Put the caculation  as far as possible to the external loop
#3 Use the local variable  whenever possible

#example

import time

start = time.time()

for i in range(1000):
    result = []
    for j in range(10000):
        result.append(i*1000+j*10000)

end  = time.time();

print(end-start)


start = time.time()
for i in range(1000):
    result = []
    w = i*1000
    for j in range(10000):
        result.append(w+j*10000)

end = time.time()
print(end-start)

#list  add and delete the object as far as possible  at the end
