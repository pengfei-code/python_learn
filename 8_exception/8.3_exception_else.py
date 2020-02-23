#If you don't catche any exceptions ,then the program will enter the block of else

try:
    a = 3
    pass
except BaseException as e:
    print(e)
    pass
else:
    print("enter the else ,havenot catched any exceptions")

