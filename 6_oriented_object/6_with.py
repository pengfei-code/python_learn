# In the with block
#1： for instance ： with objcet | method ：
#                       pass

#2：the object you must override the method of __enter__ and the block in with
# and It will be execute the obj's __enter__ and then execute the obj's __exit__ finally
#the obj's __exit__

#3 if you use like this with method : and the method must return the object implemented the
#__enter__ and the __exit__




class WithTest:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def print_info(self):
        print("withtest")

wt = WithTest()
with wt :
    wt.print_info()
    pass

def with_method():
    print("with_method")
    return wt

with with_method() :
    wt.print_info()
    pass

#use as
##4 If you want to use as ,On the condition that  you must return the object itself implemented __enter__
# in the method of __enter__

with wt as x:
    x.print_info()
    pass


with with_method() as  x:
    x.print_info()
    pass



