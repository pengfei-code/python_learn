#A generator  can  generator iterators from a set of items you want to add

#yield

# Implement a fibonacci to use generator

#generator a special iter you can use the next and for to traverse
#send()




def fibonacci():
    print("start")
    a = 0
    b = 1
    c = 0

    print("before yield")
    for i in range(10):
        c = a + b
        a = b
        b = c
        yield c
    print("after yield")
    # raise StopIteration




w = fibonacci()
#what is the diffrence between the method of generator and the normal method
#w =fibonacci() will not  execute the content of method untill the method of next or
#method of send

#and if you call the next() method then the system will execute the method of fibonacci
#and it will be stoped in the phrase of "yield c" ,and if you traverse all over the
#iters and then it will jump out the "yield c",then it will execute the last phrase of
#print("after yield")




print("after w = fibonacci()  wwwwwwwwwwwwwwwwwwwwww")
print(next(w))
print(w.__next__())
print("after next .....................................")
print("w.send(10080) ：",w.send(10080))
print("after send......................................")

print(type(w))
# print(next(w))
# print(next(w))


for x in w:
    print(x)