#call method 对象方法

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __call__(self, *args, **kwargs):
        print("This is an obj method")
        print(kwargs)
        return dict((("name",self.name),("age",self.age)))



Per = Person

per1 = Per("songpengfei",22)

dicts = dict((("key1","value1"),("key2","value2")))

tt = per1(2,3,aa="aa",bb = "bb",cc = dicts)

print(tt)



#在python中 没有重载方法，方法名相同会覆盖掉之前方法，调用之前方法会报错

class OverloadTest:

    def print_info(self):
        print("tay")
    def print_info(self,a,b):
        print(a,b)

OLT = OverloadTest

olt1 = OLT()

#olt1.print_info() error

olt1.print_info("hello","\tworld")


#给python中的类添加方法
def test01(name):
    print("test01 {0}".format(name))

class ClassAdd:

    def __init__(self):
        self.t01 =test01

    def print(self):
        print("print info")
    @classmethod
    def test_class(cls):
        print("This is class method")
ca1 = ClassAdd()

def add_method1(t):
    print("add_method1 {0}".format(t))

def add_method2(t,s):
    print("add_method1 {0} and {1}".format(t,s))
    if isinstance(t,ClassAdd):
      t.print()

#给对象一个属性赋值为方法
ca1.tt =add_method1

ca1.tt("hehe")

#给类添加实例方法

ClassAdd.a1 = add_method1
ClassAdd.a2 = add_method2

ca1.a1()
ca1.a2("s")
ca1.t01("name")

print(ClassAdd.a1)

ClassAdd.test_class()


#class 三种方法详解

class  Student:
    count = 0
    def instance_method(self):
        print("This is 实例方法")
    #静态方法主要放一些逻辑代码  主要放一些和类无关的
    @staticmethod
    def static_method(a):
        print("这是一个静态方法{0}".format(a))
        Student.count+=1
    @classmethod
    def class_method(cls):
        print("这是一个类方法")



stu = Student()
stu.instance_method()




#由类来调用类方法和静态方法 对象调用没有问题

Student.class_method()
Student.static_method("hehe")

print(Student.count)


#私有属性  private porverty


class Teacher :
    def __init__(self,name,age):
        self.name = name
        self.__age = age

tea1 = Teacher("songpengfei",22)


print(tea1.name)
print(tea1.__age)#访问不到

