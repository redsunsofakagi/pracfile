from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

def p1():
    dic1={}
    count=0
    for i in range (5):
        count+=1
        name=input("Enter name "+str(count)+" :")
        marks=int(input("Enter marks "+str(count)+" :"))
        dic1[name]=marks

def p2():
    print("*******")
    for i in range(4):
        s=" "
        print(s*(5-i)+"*")
    print("*******")

def p4():
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
    cube=a^3
    print("The cube of",a,"is",cube)

def p5b(a,b):
    if a==b:
        return True
    else:
        return False

print(p5b("arin","arin"))
    

