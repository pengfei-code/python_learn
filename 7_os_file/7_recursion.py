#To implement a factorial in range 10  use recursion
import os
# result = 1
def factorials(num):
    # global  result
    if num==1:
        return 1
    else:
        return num*factorials(num-1)

print(factorials(5))

#Use recusion to implement list all of the files in hierachicle

path = "test"
count_level = 0


def listTree(path,level):
    global count_level
    count_level +=1
    listFiles = os.listdir(path)
    for file_or_dir in listFiles:
        print(level*"\t",f"under the {path} : \t",file_or_dir)
        if os.path.isdir(file_or_dir):
            listTree(file_or_dir,count_level)
            pass

    pass

listTree(path,0)