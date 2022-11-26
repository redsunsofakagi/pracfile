from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

#---Lists, Stacks and Queues---#

def p34():
    
    Runs = [[0, 6, 4, 1, 0, 0], [3, 0, 2, 0, 0, 0], [0, 0, 4, 4, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]

    def maxrunover(runs):
        l1=[]
        for i in runs:
            l1.append(sum(i))
        for i in runs:
             if sum(i)==max(l1):
                 return i
                 
    def minrunover(runs):
        l1=[]
        for i in runs:
            l1.append(sum(i))
        for i in runs:
             if sum(i)==min(l1):
                 return i

    def total(runs):
        l1=[]
        for i in runs:
            l1.append(sum(i))
        return sum(l1)


def p35():

    def AFIND(CITIES):
        for i in CITIES:
            if i[0] in ['a','A']:
                print(i)

def p36(): #For some reason, running this using p36() results in errors. Run in a seperate file.
    import sys
    top=None
    stk=[]
    s_stk=5
    
    def PUSH():
        global top
        
        if top==s_stk-1:
            print("OVERFLOW")
            sys.exit()
        else:
            adm_no=int(input("Enter admission number: "))
            name=input("Enter name: ")
            ele=(adm_no,name)
            stk.append(ele)
            if top==None:
                top=0
            else:
                top=top+1
            
    def POP():
        global top
        
        if stk==[]:
            print("UNDERFLOW")
            sys.exit()
        else:
            print("Element deleted:", stk.pop())
            if top == 0:
                top=None
            else:
                top=top-1
                
    def DISPLAY():
        
        global top
        print('[')
        for i in list(reversed(stk)):
            print(i)
        print(']')
    
    while True:
        print('#-----Welcome to the Interface!-----#')
        print()
        print('[a] Insert an element to the stack: ')
        print('[b] Delete an element from the stack: ')
        print('[c] Display the elements of the stack: ')
        print('[d] Quit the program: ')
        print()
        opt=input("Enter a choice in the [closed brackets] to proceed : ")
        
        if opt=='a':
            PUSH()
            continue
        elif opt=='b':
            POP()
            continue
        elif opt=='c':
            DISPLAY()
        elif opt=='d':
            print()
            print("Bye!")
            sys.exit()
        else:
            print()
            print("Invalid option. Aborting.")
            sys.exit()

def p37():
    pkg_desc=[]
    top = None
    
    def MakePush(Package):
        top=0
        pkg_desc.append(Package)
        if top==None:
            top=0
        else:
            top=top+1
        
    def MakePop(Package):
        global top
        
        if pkg_desc==[]:
            print("UNDERFLOW")
            sys.exit()
        else:
            print("Element deleted:", pkg_desc.pop())
            if top == 0:
                top=None
            else:
                top=top-1

def p38(): #run as seperate file
    import sys
    top=None
    stk=[]

    str1=input("Enter a string: ")
    
    def PUSH():
        global top

        for i in range(len(str1)):
            ele=str1[i]
            stk.append(ele)
            if top==None:
                top=0
            else:
                top=top+1
            
    def POP():
        global top
        
        if stk==[]:
            print("UNDERFLOW")
            sys.exit()
        else:
            print("Element deleted:", stk.pop())
            if top == 0:
                top=None
            else:
                top=top-1
                
    #PUSH()
    #for i in range(len(str1)):
        #POP()
                
def p39():
    import sys
    top=None
    stk=[]

    def PUSH():
        global top
        ele=input("Please enter the URL: ")
        stk.append(ele)
        if top==None:
            top=0
        else:
            top=top+1
            
    def POP():
        global top
        
        if stk==[]:
            print("UNDERFLOW")
            sys.exit()
        else:
            print("Element deleted:", stk.pop())
            try:
                print("URL now on top:", stk[-1])
            except IndexError:
                print("No URL on top:")
                print("WARNING- APPROACHING UNDERDERFLOW")
            if top == 0:
                top=None
            else:
                top=top-1
                
    def DISPLAY():
        
        global top
        print('[')
        for i in list(reversed(stk)):
            print(i)
        print(']')

    while True:
        print('#-----MANAGE HISTORY-----#')
        print()
        print('1. Go to a new URL ')
        print('2. URLs visited till now ')
        print('3. Go Back ')
        print('4. Exit ')
        print()
        opt=int(input("Select a choice to proceed : "))
        
        if opt==1:
            PUSH()
            continue
        elif opt==2:
            DISPLAY()
            continue
        elif opt==3:
            POP()
        elif opt==4:
            print()
            print("Bye!")
            sys.exit()
        else:
            print()
            print("Invalid option. Aborting.")
            sys.exit()
