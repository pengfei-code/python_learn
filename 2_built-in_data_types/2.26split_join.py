#split
a = "april  febrary march jenuray may"
#the defalt is  a number of spaces
b = a.split()
print(b)
c = a.split("febrary")
print(c)
d = a.split("f")
print(d)
#if the character segmentation is the first ,then the list the first will be a string of  blank
e = a.split("a")
print(e)

#join
a = ["monday","tuesday","wednesday","thursday"]
b = "".join(a)
print(b)
#还可以单独链接字符串
c ="".join("hello")
print(c)
d="*".join(a)
print(d)
