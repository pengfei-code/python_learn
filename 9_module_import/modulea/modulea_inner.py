
class modulea_test:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name


    def __init__(self,name):
        self.__name = name

    def print_info(self):
        print(f"In the modulea_test ,the class's name is {self.__name}")

    pass



print("the modulea_inner is import")