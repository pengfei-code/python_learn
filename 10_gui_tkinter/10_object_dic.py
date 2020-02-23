class Person():


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    def __init__(self,name):
        self.__name = name
        self.dict = {}

        pass
    def __getitem__(self, item):

        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value
        pass


    pass

per = Person("songpengfei")

per["age"] = 25
per["gender"] = "male"

for key,value in per.dict.items():
    print(f"key :{key}\t, value :{value}")


