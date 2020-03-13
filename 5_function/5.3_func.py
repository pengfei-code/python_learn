

#hannuota


count = 0
def hannuo(a,b,c,n):


    if n==0:
        move(a,b)
        return
    else:
        hannuo(a,c,b,n-1)
        move(a,c)
        hannuo(b,a,c,n-1)



def move(a,b):
    print(a,"->",b)
    global count
    count+=1

hannuo("a","b","c",3)
print(count)

#factorial

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

b = factorial(10)
print(b)

#e

def e_test(n):
    if n==1:
        return 1/factorial(1)
    else:
        return 1/factorial(n)+e_test(n-1)

print(e_test(10))

import  math
print(math.e)


def test(n):
    sum = 0;

    for  x in range(n,-1,-1):

        factorial = 1
        for b in range(x,0,-1):
            factorial=  factorial *b
        sum += 1 / factorial
    return sum

print(test(30))



