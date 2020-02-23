import  sys

paths = sys.path

# sys.path is a list

print(type(paths))

for p  in  paths:
    print(p)

#As you can see from path，you can import the test

# /Users/songpengfei/PycharmProjects/untitled1
# /Users/songpengfei/PycharmProjects/test
# /Users/songpengfei/PycharmProjects/untitled1
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload
# /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
# /Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend



#sys.path

dir_path = "/users/songpengfei/"
sys.path.append(f"{dir_path}")

paths = sys.path

for p   in  paths:
    print(p)
#path1 is under the dir of /users/songpengfei

#Through the path1 to create the file of path1

import os

file_name = "path1"

file_path = f"{dir_path}{file_name}.py"
with open(file_path,"w")as f:
    f.write("print(f'the path1 is called')\n")
    f.write("def sayhello():\n")
    f.write("\tprint('hello world')\n")
    f.write('\tpass')
f.close()

# import  f"{file_name}"
# eval("import path1")
#
# eval(f"{file_name}".sayhello())

# eval("import path1")
import path1

# path1.sayhello()

eval(f"{file_name}".sayhello())