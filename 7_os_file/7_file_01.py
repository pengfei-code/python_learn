# file r w a b
import os
f = open("/Users/songpengfei/a.txt","wb")

f.write(b"hello")
f.write(b" world")
f.close()

f1 = open("/Users/songpengfei/a.txt","rb")

print(os.path.getsize("/Users/songpengfei/a.txt"))
len = os.path.getsize("/Users/songpengfei/a.txt")
ss = f1.read(len)

f1.close()

print(ss)





