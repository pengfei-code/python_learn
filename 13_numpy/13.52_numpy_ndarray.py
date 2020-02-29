

import numpy as np

#create a one_digit array
one_digit = np.array([1,2,3,4])

print(one_digit)

#create a two_digit array
two_digit = np.array([[1,2,3],[11,22]])

print(two_digit)


#create a three_digit array

three_digit = np.array([[[1],[2,3],[4,5,6],[6,7,8,9]]])
print(three_digit)

#dtype to set the type

d = np.array([2,3,4],dtype = float)

print(d)


#ndmin to set the numerical digit
#three_digit array
e = np.array([1,2,3],dtype = float,ndmin=3)
print(e)

#four_digit array

f = np.array([1,2,3],dtype = float,ndmin =4)
print(f)
#test

#In a muti_digit array ,It's subarray is only small than its own array dimensions

c = np.array([[[1,2,3],[22]],[3,4],[[4,5,6]]])
print(c)


