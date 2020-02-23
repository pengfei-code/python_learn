#inner func

def outter():
    print("outer")
    def inner():
        print("inner")
    inner()
outter()


def print_name(is_chinese,surname,name):
    def inner_print(a, b):
        print(a, b)
    if(is_chinese):
        inner_print(surname,name)
       # print(surname)
    else:
        inner_print(name,surname)

print_name(True,"song","pengfei")
print_name(False,"chen","jack")

#global
a=30
def aa():
    global a
    a+=1
    print(a)

aa()
#nonlocal
def outter():
    b = 20
    def inner():
        nonlocal b
        b+=10
        print(b)
    inner()
outter()

#legb local->enclosed->global->built in

#str() system  built in
str = "global"
def test_Legb():
    str = "enclosed"
    def inner():
        str = "local"
        print(str)
    inner()
test_Legb()
