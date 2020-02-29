#one degree slice

import numpy as np

od = np.arange(0,10)
print(od)
print(od[::2])
print(od[-1])
print(od[-3:-1])

#two degree slice

td = np.arange(1,13)
print("before reshape td:\t",td)
td = td.reshape((4,3))
print("after reshape td:\t",td)

#get the second row
print(td[1])

#get the third column of the second row
print(td[1][2])


#get all  rows and all columns

print(td[::,::])

#get the secend columns of  all rows
print(td[::,1])

#get the first and second columns of all rows
print(td[::,0:2])

#get all columns with an odd number of rows
print(td[::2,::])

#get the first and second column with an odd number of rows

print(td[::2,0:2])


#-----------------
#use index
print(td[2,1])

print(np.array((td[1,2],td[3,0])))

print(td[(1,3),(2,0)])
#-----------------------
#use nagtive number

#get the last row

print(td[-1])

#reverse the rows

print(td[::-1])

#reverse the rows and columns

print(td[::-1,::-1])



