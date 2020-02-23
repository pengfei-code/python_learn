#serialization
import pickle
import codecs
#pickle

a1 = "hello"

b1 = "world"

c1 = True
path = "/Users/songpengfei/a.txt"
with open(path,"wb") as f1:
    pickle.dump(a1,f1)
    pickle.dump(b1,f1)
    pickle.dump(c1,f1)
f1.close()


with open(path,"rb") as f2:
    a11 = pickle.load(f2)
    b11 = pickle.load(f2)
    c11 = pickle.load(f2)
    print(f"a11:\t{a11}\tb11:\t{b11}\tc11:{c11}")
f2.close()

class Person:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    pass
with open(path,"wb") as f3:
    pickle.dump(Person("songpengfei",22),f3)
f3.close()

with open(path,"rb") as f4:
    obj = pickle.load(f4)
    print(obj.name)
    pass
f4.close()