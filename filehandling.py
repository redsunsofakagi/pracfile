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
    with open("Poem.txt") as fin:
        count_to=0
        count_the=0
        for i in fin.readlines():
            for j in i.split():
                if j.lower()=='to':
                    count_to+=1
                elif j.lower()=='the':
                    count_the+=1
    
    print("Number of occurences of 'to':",count_to)
    print("Number of occurences of 'the':",count_the)

def f16():
    with open("emails.txt") as fin:
        count=0
        d={}
        data=fin.read()
        l1=data.split()
        counted=[]
        for i in l1:
            if i not in counted:
                d[i]=l1.count(i)
                counted.append(i)
            else:
                continue
        #WAY 1:
        #lmax=list(d.items()) #------->WILL NOT WORK. THIS SORTS IT IN REVERSE ALPHABETICAL ORDER AND NOT BY NO. OF OCCURENCES. THIS METHOD HINTED IN THE QUESTION IS INCORRECT.
        lmax=[]
        for i,j in d.items():
            lmax.append((j,i))
        lmax.sort(reverse=True)
        print("WAY 1- Top 2 most commonly used words are:", lmax[0][1], 'and', lmax[1][1])
        print()

        #WAY 2:
        print("WAY 2- Top 2 most commonly used words are:")
        for i in range(2):
            all_keys=list(d.keys())
            all_values=list(d.values())
            print(all_keys[all_values.index(max(all_values))])
            del d[all_keys[all_values.index(max(all_values))]]
def f17():
    with open("old.txt") as fin:
        new_lst=[]
        data=fin.readlines()
        for i in data:
            for j in i.split():
                if j=="a":
                    new_lst.append(i)
                    break
    
    with open("new.txt","w") as fout:
        fout.writelines(new_lst)

def f18():
    rec_count=int(input("Enter number of records to be entered: "))
    lst_out=[]
    for i in range(rec_count):
        title=input("Enter title: ")
        price=input("Enter price: ")
        rec=title+", "+price
        lst_out.append(rec)
    with open("books.dat","w") as fout:
        fout.writelines(lst_out)

def DISPLAYWORDS():
    with open("STORY.TXT") as fin:
        data=fin.readlines()
        for i in data:
            for j in i.split():
                if len(j)<4:
                    print(j)

def f20():
    with open("file.txt","r") as fin:
        try:
            run=True
            while run:
                choice=input("Enter 'c' to continue or 'end' to stop: ")
                if choice=="c":
                    char=fin.read(1)
                    print(char)
                    if char.isupper()==True:
                        with open("UPPER.TXT","a") as fout:
                            fout.write(char)
                    elif char.islower()==True:
                        with open("LOWER.TXT","a") as fout:
                            fout.write(char)
                    else:
                        with open("OTHERS.TXT","a") as fout:
                            fout.write(char)
                elif choice=="end":
                    run=False
                else:
                    print("Enter a valid choice")
        except EOFError:
            print("Reached end of the file.")

def f21(file1,file2):
    with open(file1) as fin:
        data=fin.read()
        lst=data.split("  ")
        new_data=""
        for i in lst:
            new_data+=i
            new_data+=" "
        new_data=new_data.rstrip(new_data[-1])
    with open(file2,"w") as fout:
        fout.write(new_data)

def f22():
    with open("file1.txt","r") as fin:
        data=fin.readlines()
        count=1
        for i in data:
            with open("file2.txt","a") as fout:
                fout.write(str(count)+i+"\n")
            count+=1

def f23(filename):
    with open(filename,"r") as fin:
        str1=fin.read()
        print("Size of file is " + str(len(str1)) + " bytes.")
        fin.seek(0)
        lst=fin.readlines()
        print("Number of lines is "+str(len(lst)))
        word_count=0
        for i in lst:
            for j in range(len(i.split())):
                word_count+=1
        print("Number of words is "+ str(word_count))    

def f24():
    with open("students.dat","ab") as fout:
        while True:
            rec_add={}
            choice=input("Do you want to add a new entry? (y/n)")
            if choice.lower()=="y":
                name=input("Enter name: ")
                rollno=int(input("Enter roll no.: "))
                rec_add[rollno]=name
                pickle.dump(rec_add,fout)
            elif choice.lower()=="n":
                print("Okay!")
                break
            else:
                print("Enter a valid choice")
    with open("students.dat","rb") as fin:
        roll_search=int(input("Enter a roll no. to search for in the file: "))
        run=True
        while run:
            try:
                rec=pickle.load(fin)
                for i in rec:
                    if i==roll_search:
                        print("Matching record found: ")
                        print(rec)
                        run=False
            except EOFError:
                print("No matching record was found :(")
                run=False
def f25():
        with open("students_info.dat","ab") as fout:
            while True:
                choice=input("Do you want to add a new entry? (y/n)")
                if choice.lower()=="y":
                    name=input("Enter name: ")
                    rollno=int(input("Enter roll no.: "))
                    marks=int(input("Enter marks: "))
                    rec_add=[rollno,name,marks]
                    pickle.dump(rec_add,fout)
                elif choice.lower()=="n":
                    print("Okay!")
                    break
                else:
                    print("Enter a valid choice")
        with open("students_info.dat","rb+") as fout:
            run=True
            rno=int(input("Enter roll no to change marks for: "))
            marks_new=int(input("Enter new marks: "))
            while run:
                try:
                    pos=fout.tell()
                    rec=pickle.load(fout)
                    if rec[0]==rno:
                        rec[2]=marks_new
                        fout.seek(pos)
                        pickle.dump(rec,fout)
                        run=False
                except EOFError:
                    print("Record with given roll number not found!")
                    run=False


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

        elif option.lower()=="b":
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:    
                        data=pickle.load(fin)
                        print(data)  
                    except EOFError:    
                        break

                    
        elif option.lower()=="c":
            found=False
            phnum=input("Enter number: ")
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:
                        data=pickle.load(fin)
                        for i in data:
                            if data[i]==phnum:
                                print("Record found:",data)
                                found=True
                    except EOFError:
                        break
            if not found:
                print("Record not found")
        elif option.lower()=="d":
            found=False
            name=input("Enter Name: ")
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:
                        data=pickle.load(fin)
                        for i in data:
                            if i==name:
                                print("Record found",data)
                                found=True
                    except EOFError:
                        break
            if not found:
                print('Record not found')

        elif option.lower()=="e":
            found=False
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
                                found=True
                    except EOFError:
                        break
            if not found:
                print("Record not found")

        elif option.lower()=="f":
            found=False
            l1=[]
            name=input("Enter name: ")
            with open("phonebook.dat","rb") as fin:
                while True:
                    try:
                        data=pickle.load(fin)
                        l1.append(data)
                    except EOFError:
                        break
            for i in l1:
                if name in i:
                    found = True
                    print('Record found')
                    l1.remove(i)
            with open("phonebook.dat","wb") as fout:
                for i in l1:
                    pickle.dump(i,fout)
            
            if not found:
                print("Record not found")   
        else:
            print("Enter a valid option.")



def f27():
    with open("27.dat","wb") as fout:
        str1="Supercaliflageristicexpialladocious. \nCrazy, right?"
        pickle.dump(str1,fout)

    with open("27.dat","rb") as fin:
        data=pickle.load(fin)
        new_str=""
        for i in data:
            if i=="o":
                break
            else:
                new_str+=i
        print(new_str)

def f28():
    '''import sys
    with open("CINEMA.DAT","wb") as fout:
        ans='y'
        MULTIPLEX={}
        while ans=='y':
                mno=int(input("Enter MNO: "))
                mname=input("Enter MNAME: ")
                mtype=input("ENTER MTYPE: ")
                MULTIPLEX['MNO']=mno
                MULTIPLEX['MNAME']=mname
                MULTIPLEX['MTYPE']=mtype
                pickle.dump(MULTIPLEX, fout)
                ans=input("COntinue adding records? (y/n): ")
                if ans == 'n':
                    break
                elif ans not in ['y','n']:
                    print("Invalid input. Aborting.")
                    sys.exit()'''
    with open("CINEMA.DAT","rb") as fin:
        while True:
            try:
                data=pickle.load(fin)
                if data["MTYPE"]=="Comedy":
                    print(data)
            except EOFError:
                break
def f29():
    '''
    import sys
    with open("emp1.dat","wb") as fout:
        ans='y'
        Emp={}
        while ans=='y':
                no=int(input("Enter empno: "))
                salary=int(input("Enter salary: "))
                Emp['empno']=no
                Emp['Salary']=salary
                pickle.dump(Emp, fout)
                ans=input("Continue adding records? (y/n): ")
                if ans == 'n':
                    break
                elif ans not in ['y','n']:
                    print("Invalid input. Aborting.")
                    sys.exit()'''
    with open("emp1.dat","rb+") as fout:
        while True:
            try:
                pos=fout.tell()
                data=pickle.load(fout)
                if data['empno']==1251:
                    data['Salary']+=2000
                fout.seek(pos)
                pickle.dump(data,fout)
            except EOFError:
                break

def f30():
    with open("Items.csv","w", newline='') as fout:
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
                lst_out.append(i)
    
    with open("highitems.csv","w", newline='') as fout:
        wr=csv.writer(fout)
        wr.writerows(lst_out)

def f33():
    with open("Items.csv","w", newline='') as fout:
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
            
