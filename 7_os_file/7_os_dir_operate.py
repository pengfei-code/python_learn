# execute an executable file through os

import os

tt = os.system("ls -l /Applications/Notes.app")

print(tt)
#directory related operations

if os.path.exists("mkdirtest"):
    os.mkdir("mkdirtest")

if os.path.exists("mkdirtest"):

    os.rmdir("mkdirtest")

#create a multi-layer dirs
if not os.path.exists("dirs/sondir"):

    os.makedirs("dirs/sondir")

# Remove all folders at once

if os.path.exists("dirs/sondir"):

    os.removedirs("dirs/sondir")
#get some os info
print(f"os.name: {os.name}")
print(os.sep)

print(repr(os.linesep))


#print the subdir of a directory

print(os.listdir("../"))

#print the current working directory

print(os.getcwd())



