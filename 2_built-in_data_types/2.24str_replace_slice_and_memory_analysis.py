#str()转换成字符串

a = str(True)
b = str(12345)
c = str(3.140)
print(a)
print(b)
print(c)

#slice 切片
strSlice = 'abcdefghijklmnopqrstuvwxyz'
print(strSlice[0:5])
print("the strSlice from -5 to -1:",strSlice[-5:-1])
print("the strSlice from -1 to -5:",strSlice[-1:-5])
print("the strSlice from 0 to 0:",strSlice[0:0])
print("the strSlice from 0 to 26:",strSlice[0:26])
print("the strSlice from 0 to 27:",strSlice[0:27])
print("the strSlice from -30 to -1:",strSlice[-30:-1])

print("the strSlice 0:",strSlice[0])

#replace

abc = strSlice.replace('c','a')
print(strSlice)
print(abc)

str1 = "aaaabbbaacc"
print(str1.replace('a','f'))
