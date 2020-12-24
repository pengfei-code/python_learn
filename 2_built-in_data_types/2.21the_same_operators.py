# the same operators is is not

#what is the difference between == and is
# == is equals to value

# "is" is equals to id


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

#the following  example 
# the id of a  is diffrent from id of b 
a = "ss"
b= ["s","s"]
b = "".join(b)

print(id(a))
print(id(b))
print(a == b)
print(a is b)

