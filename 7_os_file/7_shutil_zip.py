#shutil zip

import shutil

# the first args is the destination and allow the directory not exists

shutil.make_archive("test2/test","zip","test")


#2 zipfile

import zipfile

testzip = zipfile.ZipFile("testa.zip","w")

testzip.write("test/a.html")
testzip.write("1.6_iter.py")


testzip.extractall("testzip")


testzip.close()


