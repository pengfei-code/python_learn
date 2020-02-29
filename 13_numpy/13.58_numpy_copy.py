import numpy as np
a = np.arange(1,13).reshape((3,4))
print(a)

sub_a = a[:2,:2]
print("sub_a:\t",sub_a)

#if you modify the subsequence,and the a array will also be modified

sub_a[0,0]=100

print("a:\t",a)
print("sub_a:\t",sub_a)

#copy

sub_b =np.copy(sub_a)

sub_b[0,0] = 1
print(sub_b)


print("a:\t",a)
print("sub_a:\t",sub_a)