# complex table data stored

#  name  age  job
#   xxx    xxx    xxx
#  xxx      xxx   xxx

dict1 = dict(name = "n1",age=1,job = "job1")
dict2 = dict(name = "n2",age = 2,job = "job2")
dict3 = {"name":"n3","age":3}
table1 = list()
table1.append(dict1)
table1.append(dict2)
table1.append(dict3)

print(table1)

dict_all = dict()

dict_all["key1"] = dict1
dict_all["key2"] = dict2
dict_all["key3"] = dict3
print(dict_all)


