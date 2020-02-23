# you can use a as noun  while  b as verb
# It is particular important to note that self must put in the first position of the funcs's
#parenthesis

#You can declare a variable anywhere in a class  but be careful when you  call it
#while it is not decalare


#在python中类也是对象 一切都是对象  然后就是python的类可以看成是一个模具
class Student:
    sex =""
    def __init__(self,name,age,d):
        self.name = name
        self.age = age
        self.d  = d
    def print_info(self):
        print("My name is {0},and age is {1}".format(self.name,self.age))
        self.tt = "tt"
    def print_self_tt(self):
        self.tt


# list_stus = list()
# for x in range(0,5):
#     name = input("please input the name:")
#     age = int(input("please input the age:"))
#     temp_stu = Student(name,age)
#     list_stus.append(temp_stu)
#
# list_stus[0].print_info()
# print(list_stus[0].tt)

dict1 = dict((("name","song"),("age",20)))

stu = Student("tian",30,dict1)

print(stu.d)

def dir_test(a,b):
    print(a,b)
    c = 30
    #pass
    def inner_dir():
        pass

#print(dir_test.__dir__())



# print(stu.__dict__)
# print(stu.__dir__())


print(dir_test.__dir__())
print(dir_test.__dict__)

#Pass allows you to define a empty method or empty class
def pass_test():
    pass
class PassTest:
    pass


print(stu.__dict__)
print(stu.__dir__())
#Class func

Student.print_info(stu)


#you dont need to init the constructor


class Car :

    def get_car_info(self):
        print("hello")

c = Car()

c.get_car_info();

# Car.get_car_info();

#Class Object 类对象

# 和Java不同的是类属性是专属于类的  类其实也是一个对象  所以 和java static 不同的是
#java中其他对象改变了static  属性值之后 其它的对象也改变
#而这个是互不干扰的，你可以理解为每一个对象里面都包含了共同类对象！

class Person:
    #类属性
    high = 1.80

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_info(self):
        print("name is {0} and the age is {1},and the high is {2}".format(self.name,self.age,self.high))
    @classmethod
    def print_high(cls,*d):
        print("the high of class is {0}".format(cls.high))
        #cls.print_info() 这是错误的 因为类对象不能调用类方法
        #也不能用self

per1 = Person("song",25)

per1.high = 20
per1.print_info()
#类对象
per_class = Person

per2 = per_class("per2",35)
per2.print_info()
per2.high = 30
per2.print_info()

print("类对象Person.high is {0}".format(Person.high))

per1.print_high()
Person.print_high()


#析构方法
class Teacher:
    def __del__(self):
        print(" I have been destroyed")

tea1 = Teacher()
tea2 = Teacher()

del tea1
print(tea1)#not defined

#class test

class Department:

    per_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Department.per_count+=1
    @classmethod
    def print_info(cls):
        print("这是一个类方法 and the people of numbers is {0}".format(Department.per_count))
    def print_self_info(self):
        print("name is {0} and age is {1}".format(self.name,self.age))


def testDepartment():
    Department.print_info()
    de1 = Department("air", 33)
    de1.print_self_info()
    Dep = Department
    de2 = Dep("shen",33)
    de2.print_self_info()
    Department.print_info()





testDepartment()




















