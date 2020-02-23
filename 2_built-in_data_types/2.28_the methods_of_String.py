#methods  of String
a = "学习进行时】“尊老”，是中华民族的优良传统。习近平始终尊重、关心老年\
人。重阳节之际，新华社《学习进行时》原创品牌栏\
目“讲习所”推出图文故事，重温总书记尊老敬贤的动人瞬间，领悟总书记的良苦用心。\
“尊老敬老是中华民族的传统美德，爱老助老是全社会的共同责任。\
”多年来，习近平总书记一直身体力行尊老敬老，其中有很多温情瞬间广为流传，细细品味让人感动"
print(a)
print(len(a))

print(a.startswith("学习"))
print(a.endswith("感动"))

print(a.count("心"))
print(a.isalnum())

b = "aaaa123"
print(b.isalnum())

print(a.find("心"))
print(a.rfind("老"))


c = " *sxt* "
print(c.strip())
#去不掉因为*不再最外层
print(c.strip("*"))

d = "*sxt*"
print(d.strip("*"))

#uppercase lowercase
e = "i am a programmer"
print(e.capitalize())
print(e.title())
print(e.upper())
print(e.lower())
print("i Am a PrOgRaMmEr".swapcase())




#format layout
f = "hello world"
print(f.center(6+len(f),"*"))
print(f.ljust(6+len(f),"*"))
print(f.rjust(6+len(f),"*"))

#other methods judge
print("as".islower())
print("as".isupper())
print("12323".isdigit())
print("sdfsdf_a".isalpha())
print("sdfdsf123".isalnum())


