#对象的深拷贝 和浅拷贝
class Cap:
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color = color

    def __init__(self,color):
        self.__color = color

        pass
    def character(self):
        print("cap's color is {0}".format(self.__color))
        pass

    pass

class Handler:
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
    def __init__(self,color):
        self.__color = color
        pass
    def character(self):
        print("handler's color is {0}".format(self.__color))
        pass


class Bottle:

    @property
    def cap(self):
        return self.__cap
    @cap.setter
    def cap(self,cap):
        self.__cap = cap
        pass

    @property
    def handler(self):
        return self.__handler
    @handler.setter
    def handler(self,handler):
        self.__handler = handler

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,color):
        self.__color = color

    def __init__(self,cap,handler,color):
        self.__cap = cap
        self.__handler = handler
        self.__color = color

        pass
    def character(self):
        print("Bottle's color is {0}".format(self.__color))
        self.handler.character()
        self.cap.character()
    pass

b = Bottle(Cap("blue"),Handler("white"),"complex")

b.character()

import  copy
b_shallow = copy.copy(b)
b_deep = copy.deepcopy(b)

b._Bottle__handler._Handler__color = "change_handler_color"
print("shallow_______________________")
b_shallow.character();


print("deep__________________________")
b_deep.character()




#composition 组合

# is a  inherit
#has a  composition

class Toy:
    def __init__(self,name):
        self.__name = name


class Father:
    def __init__(self,name):
        self.__name = name
        pass

class Son(Father):
    def __init__(self,name,toy):

        self.__name = name
        #composition
        self.__toy = toy
    def has_toy(self):
        print("{0} has a toy {1}".format(self.__name ,self.__toy._Toy__name))

s = Son("son song",Toy("a"))

s.has_toy()





