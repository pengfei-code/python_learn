#csv comma separated value


import csv

path = "/Users/songpengfei/a.txt"


with open(path,"w") as f1:
    list1 = ["张三",22,"男"]
    writers = csv.writer(f1)

    writers.writerow(list1)
    lists = [["李四",32,"男"],["lily",16,"female"],["jack",17,"male"]]
    writers.writerows(lists)

    print(type(writers))

f1.close()

with open(path,"r") as  f2:
    reader1 = csv.reader(f2)
    # print(reader1)
    print(csv.reader.__class__)
    for row in reader1:
        print(type(row))
        print(row)
    # print(reader.)

f2.close()

# print("hello)