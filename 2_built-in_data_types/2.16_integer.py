#python3 的int类型可以无限大
#不同进制

#binary

print(0b110)

#octonary

print(0o77)

#hexadecimal
print(0xaabbc223)
print(0xff)

#类型转换

print(int(22.3))
print(int(0x456abc))
try:
    print(int("456abc"))
    print(int("22.3"))
finally:
    print(10**10000)
print("hello world")
