#Local variable test in function


import  time
import math

count = 10000000
def test01():
    start_time  = time.time()
    for x in  range(1,count):
        math.sqrt(x)
    print("test01 execute over")
    end_time  = time.time()
    print("test01 execute over time is {time}".format(time = end_time-start_time))

def test02():
    start_time = time.time()
    b = math.sqrt
    for x in range(1,count):
        b(x)
    end_time  = time.time()
    print("test02 execute over time is {time}".format(time = end_time-start_time))


test01()
test02()


# actual parameters  and formal parameters passing
# It is particular important to note that  the actual parameters and formal parameters passing is
#reference passing not value passing
#example

b = list((22,10))
print(b)
t = 3
def pass_parameters(c):
    b.append(30)
    #It is particular important to note that if you want to use the basic variable(not object  or
    # immutable )  you must
    #declare global first
    # example error
    #t+=1
    #correct
    #global
    #t+=1
    c.append(40)

pass_parameters(b)
print("After the parameter value is passed,the value of b is :{0}".format(b))

#example 2

def pass_parameters1(c):
    c = 10

pass_parameters1(t)

print("t is {0}".format(t))


#Imutable variable  int float tupple string boolean
#In the python  All of the paramreters passing is references passing




#shallow copy

def test_shallow_copy():
    b = list(("aa","bb","cc",list((20,30,40))))
    c = b.copy()
    c[3][1] =90
    print("test_shallow_copy's b is {0}".format(b))

#deep copy  is copy of all the object in it

def test_deep_copy():
    b = list(("aa","bb","cc",list((20,30,40))))
    import  copy
    c = copy.deepcopy(b)
    c[3][1] =30
    print("test_deep_copy's b is {0}".format(b))

test_shallow_copy()
test_deep_copy()

#named parameter can shufle the para
def test_named_para(a,b,c,d):
    print("{0},{1},{2} and {3} ".format(a,b,c,d))

test_named_para(b="b",a="a",c="c",d="d")

#default value parameter

def test_default_value_parameter(a,b,c=20,d=30):
    print("{0},{1},{2} and {3} ".format(a,b,c,d))

test_default_value_parameter("a","b")

#mutable variable
#tuple
def test_mutable_para(a,b,*c):
    print(*c)
#dictionary
test_mutable_para(20,30,40,50,60,70)

#you can pass it no para to * or **
test_mutable_para(20,30)


def test_mutable_para1(a,b,**c):
    print("c is ",c)

#dd = dict(name = "songpengfei",age = 20) error

#* 变量可以接受一个字典变量  但是**c 虽然是一个字典变量 但是不能接受
test_mutable_para1(20,30,name = "songpengfei",age = 22)



#obsessive variable

def  test_obsessive_variable(*a,b,c):
    print("{0},{1},{2}".format(a,b,c))

test_obsessive_variable(20,30,40,b="b",c="c")

def  test_mutable_variable2(*a,**a1):
    print("{0},{1}".format(a,a1))

test_mutable_variable2(20,30,40,name = "song",age = 20,b="b",c="c")
#special  No parameters can be added  **v behind
'''mutable_para3(**a,b):
    print(a)
    '''


#lambda expressions is only one like a*b*c

f = lambda a,b,c,*d,**e:a*b*c

print(f(20,30,40))
print(f(20,30,40,50,60))

b = [lambda a,b:a+b,lambda a,b:a*b,lambda a,b :a/b]

c = b[0](20,30)
print(c)


#eval
eval("test_obsessive_variable(30,b=20,c=10)")

eval("print('hello world')")

# eval("print("hello world")") error

a = 10
b= 20
c = eval("a+b")
print(c)




