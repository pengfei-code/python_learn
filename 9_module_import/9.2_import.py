#1
import math as m

#2

# from math import *

#3

from math import sin,pi,e

print(sin(90))
print(pi)
print(e)

#if you import the module, the system will treat the math as a object of module



print(m)


#The phrase of import is equivalent to the method of __import__
smp = __import__("math")
print(smp.pi)

#

import importlib

tw = importlib.import_module("math")

print(tw.pi)

import module_second
import module_second

ms = importlib.import_module("module_second")
importlib.reload(ms)



