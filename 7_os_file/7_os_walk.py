#walk

import os

cwd_path = os.getcwd()

print(cwd_path)

walks = os.walk("./test")
# The walks is a generator it made up of tupples

#The tupple's format like （dirpath,dirnames,filenames）
#Nomatter how deeps in you dirs ,It comprehensive treat all the subdirs as a one level directory

print(walks)

# for dirpath,dirnames,filenames in walks:
#     # print(os.path.join(dirpath,dirnames))
#     # print(type(type(dirnames)))
#     for dir in dirnames:
#         print("dirs:",os.path.join(dirpath,dir))
#
#     print("\n\n************************************\n")
#     for file in filenames:
#         print("files:",os.path.join(dirpath,file))
#also you can use other variable of name to traverse

for path,dirs,files in walks:
    for dir in dirs:
        print("dirs:",os.path.join(path,dir))
    for file in files:
        print("files:",os.path.join(path,file))