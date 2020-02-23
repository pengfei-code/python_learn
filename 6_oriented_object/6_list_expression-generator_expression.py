#list represatation列表表达式
lists = [x*2 for x in range(10)]

print(lists)

lists1 = [x*2 for x in range(10) if x>5]

print(lists1)

#generator represatation 生成器表达式

gernor = (x*2 for x in range(10))

print(type(gernor))

print(next(gernor))
print(next(gernor))



for x in gernor:
    print(x)


