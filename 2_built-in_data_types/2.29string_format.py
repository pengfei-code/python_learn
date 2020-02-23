#format  placeholder {}

a = "my name is {0},and i have {1} years old"

aa = a.format("song","17")

b = "i have 3 {0},you can give it to {1}{2}{3}"
bb = b.format("apples","xiaoming","xiaoqiang","and xiaohong")

print(aa)
print(bb)

# fill and alignment
#^center >right alignment <left alignment
#it is a alpha after colon
#but it is a number  after gt or lt or^

print("{:*>9}".format("hello"))
print("{:_<10}".format("world"))
print("{:*^11}".format("ti"))


#numberformat

a = 3.14159265359
b = -3.14159265359
#
print("{:.3f}".format(a))#3.142
print("{:+.2f}".format(b))#-3.14
print("{:.0f}".format(2.777))#3

print("{:0>2d}".format(5))#05
print("{:x<5d}".format(5))#5xxxx
print("{:,}".format(123234728347234))# 123,234,728,347,234
print("{:.2%}".format(0.25))#25.00%
print("{:.5e}".format(121312414124))#1.21312e+11

#default blank space
print("{:^10d}".format(3))
print("{:<10d}".format(3))
print("{:>10d}".format(3))




