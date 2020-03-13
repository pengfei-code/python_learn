#asterisk argument

# the argument *v and * kwargs

def test1(a,b,*c,d,d1,**e):
	print("a:\t",a)
	print("b:\t",b)
	print("c:\t",c)
	print("d:\t",d)
	print("d:\t",d1)
	print("e:\t",e)
	print("type c:\t",type(c))
	print("type e:\t",type(e))
	pass  
def test2(a,b,*c,**e):
	print("a:\t",a)
	print("b:\t",b)
	print("c:\t",c)
	print("e:\t",e)
	print("type c:\t",type(c))
	print("type e:\t",type(e))
	pass  


if __name__  == "__main__":
	test1('aa',20,"cc",d=3.14,d1= "d1",name="spf",age=20)
	c2 = list(("c21","c22"))
	e2 = dict((('name2',"spf2"),))
	test1('aa2',"202",c2,d1="d2",d="ww",**e2)
	#test1('aa2',"202",c2,d="d",d1="d1",e2)#字典参数不能用作位置参数

	#test1('aa3',"203",c2,d="d3",**e2) #wrong keyword arguments must put after postional  arguments
	test1('aa3',b="203",c=c2,d="d",d1="d1",**e2)
	#单一 双结  （单一）后妃 点心 （字典要想变为非位置参数 可以加**）有序 合并
	test1("aa4","204",c2,d="d4",d1="d1",name="pengfei",education="college")
	#合并
	print("combine-------->")
	test1("aa4","204","c2combine1",*c2,d="d4",d1="d1",name="pengfei",education="college",**e2)
	print("not combine-------->")
	test1("aa4","204","c2combine1",c2,d="d4",d1="d1",name="pengfei",education="college",**e2)
	test2("aa4","204","c2combine1",c2,e2)

		
	pass
