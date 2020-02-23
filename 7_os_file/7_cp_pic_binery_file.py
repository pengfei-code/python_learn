# copy a pic to implement the write and read the binary file

path = "/Users/songpengfei/desktop/a.jpeg"

destination = f"{path[0:path.rfind('/')]}/b.jpeg"
print(destination)
list_lines = []
with open(path,"rb") as f1:
    list_lines = f1.readlines()

    pass
f1.close()

with open(destination,"wb") as f2:
    f2.writelines(list_lines)
    pass
f2.close()

