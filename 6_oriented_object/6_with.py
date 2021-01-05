#the usage of with
#



class WithTest:
    def __enter__(self):
        print("enter")
        return self# the object behind as （object）

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        return true  # if you return the true ,if the code contains exception then the system will not throw the exception else throw the exception
    
    def print_info(self):
        print("withtest")

wt = WithTest()
with wt :
    wt.print_info()
    pass

def with_method():
    print("with_method")
    print(1/0)
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



