
a = int(input("please input a score"))

if a<60:
    print("not  pass a test ")

elif 60<=a<70:
    print("pass a test")
elif 70<=a<80:
    print("fine")
elif 80<a<=90:
    print("good")
else:
    print("very well")

# three eyes operator
aa = 10
print("judge aa :"if aa>10 else  "<") #so strange

#while

a = 0
sum = 0
while(a<100):
    a+=1
    sum+=a

print ("the result of sum is :",sum)


#for  implementats the sum of  even and odd from 1 to 100 ,respectively

odd_sum = 0
even_sum = 0
for x in range(1,101):
    if x%2==0:
        even_sum+=x
    elif x%2==1:
        odd_sum+=x
print("the odd_sum is {0} and the even_sum is {1}".format(odd_sum,even_sum))


#nested loop implements a multiplication table

for x in range(1,10):
    for y in range(1,10):
        if y<=x:
            print("{0}*{1}={2}".format(x,y,x*y),end = "\t")

    print()

#nested loop implements a dict of data  and select the salary beyond the 15000
'''
    name  age   salary  city
    song1   20  30000   beijing
    song2   19  20000   shenzhen
    song3   18  10000   tianjin
'''

list_data = list()
dict1 = dict((("name","song1"),("age","20"),("salary","30000"),("city","beijing")))
dict2 = dict((("name","song2"),("age","19"),("salary","20000"),("city","shenzhen")))
dict3 = dict((("name","song3"),("age","18"),("salary","10000"),("city","tianjin")))
list_data.append(dict1)
list_data.append(dict2)
list_data.append(dict3)

for x in list_data:
    if int(x.get("salary"))>15000:
        print("name : {0},salary :{1}".format(x.get("name"),x.get("salary")))


#break statement

#when you enter the letter is q or Q stop the program


while True:
    a = input("please input a character")
    if a.upper() == "Q":
        print("program over")
        break
    else:
        print("you input the character is {0}:".format(a))


#continue
#implements a  average salary
list_salary = list()
average_salary = 0;
while True:
    salary = input("please input a salary")

    if salary.upper() == "Q":
        print("program quit")
        break
    elif salary.isalpha() or int(salary)<0  :
        continue

    list_salary.append(salary)
for x in list_salary:
    average_salary += int(x)
    average_salary = average_salary/len(list_salary)

print("all of the salary is {0} and the average salary is :{1}".format(list_salary,average_salary))


#while and else
# in the while statement  if it does not execute break  then it will be enter the else
a = 1
while a<3:
    a+=1
    b = int(input("please input a number:"))
    if b>10:
        break
else:
    print("while is complete  without  break")










