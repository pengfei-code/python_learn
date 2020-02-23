class Father:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        pass

    pass


class Son(Father):
    def __init__(self, name, age, interest):
        Father.__init__(self, name, age)
        print(self.name)
        self.interest = interest

    pass


print(Son.mro())
son1 = Son("song", 22, "play game")

# 由于age是父类的私有属性 所以调用出错
# print(son1.name,son1.age,son1.interest)

print(dir(son1))

print(son1.name, son1._Father__age, son1.interest)


# 如果是getsetter呢
class Mother:
    @property
    def color_hair(self):
        return self.__color_hair

    @color_hair.setter
    def color_hair(self, color_hair):
        self.__color_hair = color_hair

    def __init__(self, color_hair):
        self.__color_hair = color_hair
        pass

    def dye_hair(self, color):
        print("dye the hair to use the {0}".format(color))


class Father:
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        pass

    pass


f = Father("f", 50)
print(f.age)


class Son(Father, Mother):
    def __init__(self, name, age, interest, color_hair):
        Father.__init__(self, name, age)
        Mother.__init__(self, color_hair)
        print(self.name)
        print(self.age)
        self.interest = interest

    pass


print(Son.mro())
son1 = Son("song", 22, "play game", "brown")

# 由于age是父类的私有属性 所以调用出错
print(son1.name, son1.interest)

print(son1.age)

print(son1.color_hair)

son1.dye_hair("purple")


# 方法的重写

class Animal:
    def __init__(self):
        pass

    def catch(self, animal):
        print("Animal cathch the {0}".format(animal))

    pass


class Tigger(Animal):
    def catch(self, animal):
        print("Tigger cathch the {0}".format(animal))

    pass


Tigger().catch("deer")


# object 根类

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    pass


teacher = Teacher("songpengfei", 23)

o = object()

teacher_dir = dir(teacher)
o_dir = dir(o)

print(teacher_dir)
print(o_dir)

print(set(teacher_dir).difference(set(o_dir)))


# 重写object str方法
class bottle:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("bottle's name {0}".format(self.name))

    pass
    pass


b = bottle("bb")

b.__str__()
