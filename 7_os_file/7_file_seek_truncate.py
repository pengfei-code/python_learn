#truncate
#truncate indicates how many characters you can truncate from current position or a
#specified position
import os
import codecs
path = "/Users/songpengfei/a.txt"

with codecs.open(path,"wb",encoding="utf-8") as fw:

    listW =[f"{i}hello world\n" for i in  range(10)]
    print(listW)
    fw.writelines(listW)
fw.close()

# if you want to use the truncate  the mode must contains a plus operation
# truncate will keep the file in sync,the characters you truncated will be deleted in
#the file

with codecs.open(path,"rb+",encoding="utf-8") as fr:
    fr.truncate(5)
    print(fr.name)
    listR =fr.readlines()
    print(listR)

fr.close()

#seek and truncate

command_del = f"rm -rf {path}"
os.system(command_del)

with codecs.open(path,"wb",encoding="utf-8") as fw:

    listW =[f"{i}hello world\n" for i in  range(10)]
    print(listW)
    fw.writelines(listW)
fw.close()

with codecs.open(path,"rb+",encoding="utf-8") as fr1:
    fr1.seek(25,0)

    fr1.truncate(30)
    listR = fr1.readlines()
    print(listR)

fr1.close()


command_del = f"rm -rf {path}"
os.system(command_del)

#not use the codecs


with open(path,"wb") as fwtest:
    fwtest.write(b"hello world")
fwtest.close()

with open(path,"rb+") as fr_test:
    fr_test.truncate(10)
    content = fr_test.read()
    print(content)
fr_test.close()


with open(path,"w") as fwtest1:
    lists = [f"{i}hello world\n" for i in range(10)]
    fwtest1.writelines(lists)

    pass
fwtest1.close()

with open(path,"rb+") as frtest1:
    frtest1.truncate(10)
    lists = frtest1.readlines()
    print(lists)
    pass
frtest1.close()

# It is important to note that if you want to write or read the bytes or use the encoding
#you'd better  use the codecs

