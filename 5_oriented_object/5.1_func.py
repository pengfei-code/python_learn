#func

#1 : Func  are   object essentially
#2 :If you import the third module ，It will exccute it's func

#It is particular important to note that the parenthesis of func cannot be omitted
def my_print():
    print("hello world")

my_print()

print(type(my_print))
print(id(my_print))


#help annotation

def  max_num(a,b):
    '''This funciton is used to compare the size of numbers '''
    if(a>b):
        return a
    else:
        return b

print(max_num(2,3))
help(max_num.__doc__)


# return
def add(a,b):
    print("the {0} plus {1} equals {2}".format(a,b,a+b))

    return a+b
    print("try to see")

print(add(20,30))

# no return

def test_ret():
    print("no return")

print(test_ret())#None

def test_mutiplication_tuple(a,b,c):
    return tuple((10*a,10*b,10*c))

print(test_mutiplication_tuple(10,20,30))

#func  memory analysis

def test_memory ():
    print("test_memory")
c = test_memory
c()
print(id(test_memory))
print(id(c))

#global and local variable

a = 100
def test_domain():
    #the a is a global variable ,a is treated as an declared local variable
    global a
    a+=10
    print("the a is :",a)
    print(locals())
    print("**************************************************")
    print(globals().keys())




