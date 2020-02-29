#random
import numpy as np

#the interval is [0,1.0)

#one-digit
a = np.random.random(size=10)
print("a:\t",a)

#two-digit

b = np.random.random(size=(2,3))
print("b:\t",b)

#three-digit

c = np.random.random(size=(2,2,3))
print("c:\t",c)

#random int
#one-digit
di = np.random.randint(0,10,size=30)
print("di:\t",di)

#two-digit

ei =np.random.randint(2,11,size=(2,3))
print("ei:\t",ei)

#three-digit
fi =np.random.randint(1,20,size=(2,2,3))
print("fi:\t",fi)