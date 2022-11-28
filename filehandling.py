import pickle
import csv

from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

def f13():
    with open("text.txt","r") as fin:
        for i in fin.readlines():
            for j in i.split():
                print(j,end="")
                print("#",end="")
            print()

def f14():
    with open("text.txt","r") as fin:
        count_vowel=0
        count_consonant=0
        count_upper=0
        count_lower=0
        for i in fin.read():
            if i.isalpha()==True:
                if i.lower() in ["a","e","i","o","u"]:
                    count_vowel+=1
                else:
                    count_consonant+=1
            
            if i.isupper()==True:
                count_upper+=1
            if i.islower()==False:
                count_lower+=1
        
    print("Number of vowels:",count_vowel)
    print("Number of consonants:",count_consonant)
    print("Number of uppercase characters:", count_upper)
    print("Number of lowercase characters:",count_lower)


def f15():
    with open("poem.txt") as fin:
        count_to=0
        count_the=0
        for i in fin.readlines():
            for j in i.split():
                if j.lower=="to":
                    count_to+=1
                if j.lower=="the":
                    count_the+=1
    
    print("Number of occurences of 'to':",count_to)
    print("Number of occurences of 'the':",count_the)

def f16():
    with open("emails.txt") as fin:
        data=fin.read()
        for i in data.split():
            pass


def f17():
    with open("old.txt") as fin:
        new_lst=[]
        data=fin.readlines
        for i in data:
            for j in i.split():
                if j=="a":
                    new_lst.append(i)
                    break
    
    with open("new.txt","w") as fout:
        fout.writelines(new_lst)


def f18():
    pass

def f19():
    pass

def f20():
    pass

def f21():
    pass

def f22():
    pass

def f23():
    pass

def f24():
    pass

def f25():
    pass




def f26():
    run=True
    rec={}
    while run:
        print("Telephone directory program!\n(a) Add New Record\n(b) Display All Records\n(c) Search Telephone Number\n(d) Search Name\n(e) Update Telephone Number\n(f) Delete a record")
        option=input("Select an option(a/b/c/d/e/f):")
        if option.lower()=="a":
            rec_add={}
            name=input("Enter name: ")
            phnum=input("Enter phnum: ")
            rec_add[name]=phnum
            with open("phonebook.dat","ab") as fout:
                pickle.dump(rec_add,fout)

        if option.lower()=="b":
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:    
                        data=pickle.load(fin)
                        print(data)  
                    except EOFError:    
                        break

                    
        if option.lower()=="c":
            phnum=input("Enter number: ")
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:
                        data=pickle.load(fin)
                        for i in data:
                            if data[i]==phnum:
                                print("Record found\n"+data)
                    except EOFError:
                        print("Record not found")
                        break

        if option.lower()=="d":
            name=input("Enter Name: ")
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:
                        data=pickle.load(fin)
                        for i in data:
                            if i==name:
                                print("Record found\n"+data)
                    except EOFError:
                        print("Record not found")
                        break



        if option.lower()=="e":
            name=input("Enter name: ")
            with open("phonebook.dat","rb+") as fout:
                while True:
                    try:
                        pos=fout.tell()
                        data=pickle.load(fout)
                        for i in data:
                            if i==name:
                                data[i]=input("Enter a new number: ")
                                fout.seek(pos)
                                pickle.dump(data,fout)
                    except EOFError:
                        print("Record not found")
                        break

        else:
            print("Enter a valid option.")




def f27():
    with open("27.dat","wb") as fout:
        str1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        pickle.dump(str1,fout)

    with open("27.dat","rb") as fin:
        data=pickle.load(fin)
        new_str=""
        for i in data:
            if i=="o":
                break
            else:
                new_str+=i
        print(i)


def f28():
    with open("CINEMA.DAT","rb") as fin:
        while True:
            try:
                data=pickle.load(fin)
                if data["MYTYPE"]=="Comedy":
                    print(data)
            except EOFError:
                break

def f29():
    with open("emp1.dat","rb+") as fout:
        while True:
            try:
                pos=fout.tell()
                data=pickle.load(fout)
                if data['empno']==1251:
                    data['salary']+=2000
                fout.seek(pos)
                pickle.dump(data,fout)
            except EOFError:
                break


def f30():
    with open("Items.csv","w") as fout:
        wr=csv.writer(fout)
        lst_out=[]
        for i in range(5):
            itemno=input("Enter item no: ")
            name=input("Enter name: ")
            price=int(input("Enter price: "))
            category=input("Enter category: ")
            rec=[itemno,name,price,category]
            lst_out.append(rec)
        wr.writerows(lst_out)

def f31():
    with open("Items.csv","r") as fin:
        re=csv.reader(fin)
        itemno=input("Enter item no to search for: ")
        search=False
        for i in re:
            if i[0]==itemno:
                print(i)
                search=True
        if search==False:
            print("Item not found")


def f32():
    with open("Items.csv","r") as fin:
        re=csv.reader(fin)
        lst_out=[]
        for i in re:
            if int(i[2])>250:
                lst_out.append[i]
    
    with open("highitems.csv","w") as fout:
        wr=csv.writer(fout)
        wr.writerows(lst_out)


def f33():
    with open("Items.csv","w") as fout:
        wr=csv.writer(fout,delimiter="|")
        lst_out=[]
        for i in range(5):
            itemno=input("Enter item no: ")
            name=input("Enter name: ")
            price=int(input("Enter price: "))
            category=input("Enter category: ")
            rec=[itemno,name,price,category]
            lst_out.append(rec)
        wr.writerows(lst_out)

            
            