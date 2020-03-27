import module_global
#t = 4 #outside default global
def test1():
    global count #As a variable of the global count does not have to be created outside
    #鸡肋 g内申
    count = 2
    global t
    t+=1
    print("test1 t:\t",t)
    pass

def test2():
    global count
    print(count)

    pass

if __name__ == "__main__":
    t = 4 #default global
    print("if t:%s"%t)
    test1()
    test2()
    print("if t:%s" % t)
    #print(re_) # must be redefined


    pass

#notice: 1 As a global variable you should have to declare it in outside ，
#        just declare  global p  in a function

        #2 if the global variable is imported by another module
        # the global variable will lose its global features you must redefined

        #3 about if __name__ =="__main__"
        # if another module import this module ,the another module will execute
        #the code except for if __name__=="__main__"