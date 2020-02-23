#私有属性 和私有方法
class Person:

    def __init__(self,name,age):
       self.__name = name
       self.age = age

    def __find(self):
        print("__find")
    def test(self):
        self.__find()

    def get_name(self):
        return self.__name
    pass

per = Person("song",22)

per.test()
print("************ 调用私有方法")
per._Person__find()

print(per.get_name())



#getter setter 方法

#getter setter 方法的属性必须是私有的

class Student:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        pass

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @name.setter
    def age(self,age):
        if age<0:
            print("The age is in error range")
        else:
            self.__age = age
    pass

stu = Student("song",22)
print(stu.name,stu.age)

#显示继承顺序
print("method resolution order")

print(Student.mro())














