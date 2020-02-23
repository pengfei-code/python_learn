#seria unpack

a,b,c = 1,2,3
(a,b,c)=1,2,3
[a,b,c]=1,2,3
[a,b,c]=(a,b,c)

print(a,b,c)


a = dict(name="songpengfei",age=20,job="programmer")
print(a)
a1,a2,a3 = a.items()
print(a1,"\t",a2,"\t",a3)

a11,a22,a33 =a.keys()
print(a11,"\t",a22,"\t",a33)

a111,a222,a333 = a.values()
print(a111,"\t",a222,"\t",a333)

