path = "/Users/songpengfei/desktop/a.txt"

with open(path,"rb") as f:
    listLines = f.readlines()
    print(len(listLines))
    print(listLines)
f.close()



#writeLines will not implements the "\n"

#but if the file you read is already exist and it has muti lines then the listLines you
#read is more than 1