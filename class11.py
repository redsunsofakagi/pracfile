from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

#---Class 11th Revision---#

def p1():
    RESULT={}
    count=0
    for i in range (5):
        count+=1
        name=input("Enter name "+str(count)+" :")
        marks=int(input("Enter marks "+str(count)+" :"))
        RESULT[name]=marks
    lst=[('Name','Marks')]
    for i in range(5):
        m=0
        for i in RESULT.keys():
            if m<RESULT[i]:
                m=RESULT[i]
                n=i
        lst.append((n,RESULT.pop(n)))
    for i in lst:
        print(i)

def p2():
    print("*******")
    for i in range(4):
        s=" "
        print(s*(5-i)+"*")
    print("*******")

def p3():
    from pprint import pprint
    l1=[]
    l2=[]
    l3=[]
    l4="*"
    for i in range(6):
        l3.append(l4)
    for i in range(4):
        l2.append(l3)
    for i in range(3):
        l1.append(l2)
    pprint (l1)

#---Functions---#

def p4(l=15,b=10,h=5):
    vol=l*b*h
    print("Volume of box is: ", vol)

def p5a(a=2):
    cube=a**3
    print("The cube of",a,"is",cube)

def p5b(a,b):
    if a==b:
        return True
    else:
        return False

def p6(n):
    sum1=0
    factor=1
    while factor<n:
        if n%factor == 0:
            sum1+=factor
        factor+=1
    if sum1==n:
        print("PERFECT SQUARE")
    else:
        print("NOT A PERFECT SQUARE")

def p7():
    n=input("Enter a string of code: ")
    exec(n)

def p8(n):
    import random
    lower=10**(n-1)
    upper=10**(n)
    print(random.randrange(lower, upper))

def p9(a, an):
    #in an AP, an=a+(n-1)d
    #Here n=4, hence,
    #=> an=a+3d
    #=> d= (an - a)/3
    d= (an - a)/3
    return a + 0*d , a+d, a+ 2*d , a + 3*d

def p10(n):
    if n>1:
        x=n-1
        while x>1:
            y=n%x
            if y==0:
                print("NOT PRIME")
                break
            else:
                x=x-1
                continue
        else:
            print("PRIME")
    else:
        print("NOT PRIME")

p10(2)
p10(3)
p10(15)
