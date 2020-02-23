#the format like [(),()] you can use the method under the phrase to traverse
lists = []
for i in range(10):
    tps = tuple((f"name{i}",f"age{i}"))
    lists.append(tps)

for names ,ages in lists:
    print(names,"\t",ages)
for row in lists:
    print(row)

