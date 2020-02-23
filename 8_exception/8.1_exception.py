try:
    print("step1")
    print(1/0)
    print("step2")

except BaseException as  e:
    print(e)
    print(type(e))


try:
    print("step1")
    print(1/0)
    print("step2")

except:
    print("get a exception")
    pass


try :
    print("step1")
    print(1/0)
    print("step2")

except ZeroDivisionError as e:
    print(e)
