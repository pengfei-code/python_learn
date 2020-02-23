#list

# 4 ways to create list

# 1 []
a1 = []
print(a1)

#2:list()
a2 = list()
print(a2)

#3 : assignment

a3 = ["monday","tuesday","wednesday","thursday"]
print(a3)
#4: serializable object

a4 = list("hello world")
print(a4)
#range()
a44 = list(range(10,20))
print(a44)

a441 = list(range(10,20,2))
print(a441)

a442 = list(range(20,10,-2))
print(a442)
        

#....

b = list(x*2 for x in range(0,100))
print(b)

c = list(x*3 for x in range(0,100) if x%3==0)
print(c)
