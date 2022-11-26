from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

#---Interfacing Python w/ MySQL---#

def p11():
    import mysql.connector as con
    import sys

    def f1():
        con1= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con1.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur1=con1.cursor()
        
        e1=input("Enter name of employee. ")
        e2=input("Enter their department. ")
        e3=input("Enter their designation. ")
        e4=int(input("Enter their salary. "))
        e5=input("Enter the date [yyyy/mm/dd] they joined. ")
        v1=(e1,e2,e3,e4,e5)
        q1= "insert into EMPLOYEE(ENAME, DEPT_NAME, DESIGNATION, SALARY, DATE_OF_JOINING) values(%s, %s, %s, %s, %s)"
        try:
            cur1.execute(q1,v1)
            con1.commit()
            print("Executed succesfully.")
        except:
            print("An error occured.")
            con1.rollback()
        con1.close()
        print()

    def f2():
        con2= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con2.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur2=con2.cursor()

        x=int(input("Enter number of rows of data to be stored. "))
        l_val=[]
        for i in range(x):
            e1=input("Enter name of employee. ")
            e2=input("Enter their department. ")
            e3=input("Enter their designation. ")
            e4=int(input("Enter their salary. "))
            e5=input("Enter the date [yyyy/mm/dd] they joined. ")
            v2=(e1,e2,e3,e4,e5)
            l_val.append(v2)
        q2= "insert into EMPLOYEE values(%s, %s, %s, %s, %s)"
        try:
            cur2.executemany(q2, l_val)
            con2.commit()
            print("Executed succesfully.")
        except:
            print("An error occured.")
            con2.rollback()
        con2.close()
        print()

    def f3():
        con3= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con3.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur3=con3.cursor()
        cur3.execute("select * from EMPLOYEE")
        result=cur3.fetchall()
        for i in result:
            print(i)
        print()
        con3.close()

    def f4():
        con4= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con4.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur4=con4.cursor()
        print("While it is not logical, the salary column distinguishes all the entries from one another. Please use it to update records.")
        print()
        p=input("Enter column name of record to be updated. ")
        if p=='DATE_OF_JOINING':
            q=input("Enter new value. ")
        else:
            q=eval(input("Enter new value. "))
        r=int(input("Enter original salary of record. "))
        q4="update EMPLOYEE set "+p+" = %s where SALARY = %s"
        v4=(q,r)
        try:
            cur4.execute(q4,v4)
            con4.commit()
            print("Executed succesfully.")
        except:
            print("An error occured.")
            con4.rollback()
        con4.close()
        print()

    def f5():
        con5= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con5.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur5=con5.cursor()
        print("While it is not logical, the salary column distinguishes all the entries from one another. Please use it to delete records.")
        print()
        s=int(input("Enter salary of record to be deleted. "))

        q5="delete from EMPLOYEE where SALARY = %s"
        v5=(s,)
        try:
            cur5.execute(q5,v5)
            con5.commit()
            print("Executed succesfully.")
        except:
            con5.rollback()
            print("An error occured.")
        con5.close()
        print()
        
    while True:
        print("#--------Welcome to the Interface!--------#")
        print()
        print("What would you like to do?")
        print("Add a record. [1]")
        print("Add multiple records. [2]")
        print("Display all records. [3]")
        print("Update a record. [4]")
        print("Delete a record. [5]")
        print("Exit. [6]")
        print()

        n=int(input("Enter your choice by selecting the value in the [closed brackets]. "))
        print()
        if n==1:
            f1()
            continue
        elif n==2:
            f2()
            continue
        elif n==3:
            f3()
            continue
        elif n==4:
            f4()
            continue
        elif n==5:
            f5()
            continue
        elif n==6:
            print("Bye!")
            sys.exit()

def p12():
    import mysql.connector as con
    import sys

    def fa():
        con1= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con1.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur1=con1.cursor()

        Id=int(input("Enter the primary key."))
        if Id in [1,2,3,4]:
            cur1.execute("select * from Hospital")
            print(cur1.fetchall())
        else:
            cur1.execute("select * from Doctor")
            print(cur1.fetchall())

        con1.close()

    def fb():
        con2= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con2.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur2=con2.cursor()

        sp=input("Enter speciality. ")
        qb= "select * from Doctor where Speciality = " + "'" + sp + "'"
        cur2.execute(qb)
        rb=cur2.fetchall()
        l1=[]
        for i in range(len(rb)):
            l1.append(rb[i][1])
        print("List of Doctors: ", l1)
        print("Details: ", rb)
        con2.close()

    def fc():
        con3= con.connect(
        host="localhost",
        username="root",
        passwd="1234",
        database="HHW")

        if con3.is_connected():
            print("Connection established.")
            print()
        else:
            print("Could not establish connection.")
            sys.exit()

        cur3=con3.cursor()
        H_id=input("Enter Hospital_Id. ")
        qc= "select * from Doctor where Hospital_id = "+H_id
        cur3.execute(qc)
        rc=cur3.fetchall()
        l2=[]
        for i in range(len(rc)):
            l2.append(rc[i][1])
        print("List of Doctors: ", l2)
        print("Details: ", rc)
        con3.close()

    fa()
    fb()
    fc()
