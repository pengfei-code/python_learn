# to write a iter for list

# In the method of __iter__ ,you can return the iter object itself,Anyone who implemented the method of
#__iter__ is Iter object

# In the method of __next__,you can return the item you want to return
class IterTest:

    index = 0
    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self,list):
        self.__list = list
        pass

    def __init__(self,list):
        IterTest.index = 0
        self.__list = list

        pass

    def __iter__(self):
        return self

    def __next__(self):
        if IterTest.index <len(self.list):
            print(f"index:{IterTest.index}")
            temp = self.list[IterTest.index]
            IterTest.index+=1
            # raise StopIteration
        else:
            # print("else")
            raise StopIteration
        return temp


    pass

lists = [1,3,9,11,36]

it = IterTest(lists)
#Pass a object implemented method of iter and next  to method of iter
iters = iter(it)

for x in iters:
    print(x)

