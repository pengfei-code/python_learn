#mro()

#If there is a class which inherite two class and they have same one method
#if you call the method it will call the first class you inherite


class A:

    def find(self):
        print("A : find")
        pass
    pass

class B:

    def find(self):
        print("B: find")
        pass
    pass


class C(A,B):


    pass

cc = C()

cc.find()# A:find



print("***************************************")


#访问父类的私有属性和方法 请用_父类
#super
class Animal:
    def __init__(self,name):
        self.__name = name
        pass
    def say(self):
        print("animal say")
        pass
    def __my(self):

        print("__my()")
        pass
    def tt(self,a):

        print("tt->{0}".format(a))
        pass

class Dog:
    def __init__(self,name):
        self._Animal__name = name
        pass
    def say(self):
        #调用父类方法 可以直接使用 父类名字.方法(子类对象)
        Animal.say(self)
        print("dog say")
        pass

dd = Dog("bb")

dd.say()
print(dd._Animal__name)




print("***************************************")

class Person(Animal):
    def __init__(self,name):

        #__init__方法不能算是私有方法
        Animal.__init__(self,name)
        Animal.tt(self,"tttt")
        pass

    def say(self):
        super().say()
        print("Person say")
        pass
pp = Person("hehe")

pp.say()

#polymorphism 多态

class Man :
    def say(self):
        print("man ->say")
    pass
pass

class English(Man):
    def say(self):
        print("english -->say")
        pass
    pass

class Chinese(Man):
    def say(self):
        print("chinese -->say")
        pass

    pass


def test_say(m):
    if(isinstance(m,Man)):

        m.say()
        pass

    pass

test_say(English())

test_say(Chinese())

#运算符 重载

class Person:
    @property
    def name(self,name):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name


    def __init__(self,name):
        self.__name = name
        pass
    def __add__(self, other):
        print(self.__name +"\t" +other.__name)
        pass


p = Person("per")

p1 = Person("p1")

p+p1




#特殊属性 special property

class A:
    def __init__(self,name):
        self.__name = name
        pass
    def aa(self):
        print("aa")
    pass

class B(A):
    def bb(self,name):
        A.__init__(self,name)
        print("bb")

    pass

a = A("aaaa")
b = B("bbbb")

print(dir(a))
print(a.__dict__)


#父类方法
print(A.__bases__)

print(A.__dict__)

print(A.__subclasses__())

print(B.__bases__)

print(a.__dict__)

print(A.__class__)

