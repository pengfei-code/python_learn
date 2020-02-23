#In the package ,a file of "__init__.py" is necessary
#So if a directory contains a  file of "__init__"
#the the system will regard the dir as  a package

#1:
#
import  modulea.a.aa.aainner as tt


tt.aainner_print()


# # 2
from modulea import  modulea_inner

mt = modulea_inner.modulea_test("songpengfei")

mt.print_info()

#3 error
#
# from modulea import *
#
# mt = modulea_inner.modulea_test("songpengfei")
#
#
# mt.print_info()





#notice

# import is used to import module
#the phrase of "from ..import .." is used to import content of a module
#for instance: class method or variable


import 

