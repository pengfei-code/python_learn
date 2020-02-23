# the same operators is is not

#what is the difference between == and is
# In the python the comparison of the equal sign is the value
#but the “is” is used to determine whether the two object are refrerenced
#by the  variables is the same
##in the python3 ， the digital existenc of cache ，so the defined numbers  can be reused
#but in the python2 ,the scope of cache of a number is between -5 to 255
a = 2E1000
b = 2E1000
print("a == b:",a==b)
print("a is b:",a is b)
print("the id of a is :",id(a))
print("the id of b is :",id(b))
c = -25
d = -25
print(c is d)
print(c ==d)

