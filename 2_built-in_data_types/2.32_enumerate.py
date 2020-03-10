#enumerate can make the sequence into a sequence of index

list1 = [f"hello{i}" for i in  range(10)]
print(list1)

enum1 = enumerate(list1)

print(next(enum1))

for x in enum1:
    print(x)