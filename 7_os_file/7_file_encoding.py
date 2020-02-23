#文件分为文本文档 和二进制文件

#ASCII  america stand code infomation interchange 美国标准信息交换码 one byte
#unicode universal code 全球码  2 byte
#utf-8 unicode transformation format 变长编码 英文 onbyte  中文 3byte


# Both readlines and read are able to read all the files  ，but ReadLine is only read the nextline

#instance 1  write read and use the module of codecs

import codecs
import os
fr = None
path1  = "/Users/songpengfei/a.txt"
try:
    # In the module of codecs, you can choice which encoding you want to use
    fr = codecs.open(path1, "wb", encoding="ASCII")
    li1 = []
    for i in range(10):
        fr.write(f"{i}\tttaabbccdd\n")



finally:
    if fr is not None:
        fr.close()
    
        print("f is closed")

fw = None

try:
    fw = codecs.open(path1, "rb", encoding="iso8859-1")
    strs = fw.read()
    print(type(strs))
    print(strs)


except BaseException as e:
    print(e)
    pass

finally:
    if fw is not None:
        fw.close()

#delete the file in path1
command_del = "rm -rf {0}".format(path1)
os.system(command_del)


#instance 2 writelines readlines
#the diffrence between write and writeLines is writelines can write a list

fr1 = None
try:
    fr1 = codecs.open(path1,"wb",encoding="utf-8")
    list1 = []
    for i in range(10):
        list1.append(f"{i}\thello world\n")
    fr1.writelines(list1)

except BaseException as e:
    pass
finally:
    fr1.close()

fw1 = None

try:
    fw1 = codecs.open(path1,"rb",encoding="utf-8")
    list1 = fw1.readlines()
    print(len(list1))
    print(list1)

except BaseException as e:
    pass
finally:
    if fw1 is not None:
        fw1.close()

#delete the file in path
command_del = "rm -rf {0}".format(path1)
os.system(command_del)


#instance 3
#readline you can read the nextline
#seek(offset,whence) offset 偏移量  whence  0 the file begins 1 current files 2 the end of the file
#the argument limit of readline is determine that how many bytes you want to read
fw2 = None
try:
    fw2 = codecs.open(path1,"wb",encoding="utf-8")
    list2 = []
    for i in range(10):
        list2.append(f"{i}\thello world{i}\n")
    fw2.writelines(list2)

except BaseException as e:
    print(e)
    pass
finally:
    if fw2 is not None:
        fw2.close()
    pass

fr2 = None

try:
    fr2 = codecs.open(path1,"rb",encoding="utf-8")
    fr2.seek(0,0)
    line1 = fr2.readline()
    print(line1)
    fr2.seek(20,1)

    line2 = fr2.readline(20)
    print(line2+"s")

except BaseException as e:
    print(e)
    pass
finally:
    if fr2 is not None :
        fr2.close()
    pass














