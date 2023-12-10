import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
sign=Tk()
photo=PhotoImage(file='CREATE.png')
label=Label(sign,image=photo).place(x=-2,y=-2)
sign.geometry('550x585')
sign.title("Create Employee Details")
v=IntVar()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
v5.set('default')
def choice():
    o=v.get()
    if o==1:
        s='Male'
    else:
        s='Female'
    return s
def submit():
    cursor.execute("select id from detail")
    l=cursor.fetchall()
    for i in range(len(l)+1):
        c=i+1,
        if c not in l:
            id=i+1
            break
    n=v1.get()
    d=v2.get()
    dno=v3.get()
    dob=v4.get()
    s=choice()
    sal=v5.get()
    mob=v6.get()
    e=v7.get()
    u=v8.get()
    p=v9.get()
    t=u,
    cursor.execute("select username from detail")
    k=cursor.fetchall()
    if t in k:
        v7.set('')
        messagebox.showerror("Error","Username already exists")
    else:
        cursor.execute("insert into detail value"
                       "(%s,'%s','%s','%s','%s','%s',%s,'%s','%s','%s','%s')"
                       %(id,n,d,dno,dob,s,sal,mob,e,u,p))
        db.commit()
        messagebox.showinfo("","Account created\n\nID No. : "+str(id))
        back()
def back():
    sign.destroy()
    os.system("control.py")
lab_1=Label(sign,font=('arial',50,'bold'),text="CREATE",fg="black",
            bg="light blue").place(x=145,y=5)
lab_2=Label(sign,font=('arial',12,'bold'),text="Full Name",bg="light blue")\
    .place(x=150,y=120)
lab_3=Label(sign,font=('arial',12,'bold'),text="Designation",bg="light blue")\
    .place(x=150,y=160)
lab_4=Label(sign,font=('arial',12,'bold'),text="Dept No.",bg="light blue")\
    .place(x=150,y=200)
lab_5=Label(sign,font=('arial',12,'bold'),text="DOB",bg="light blue")\
    .place(x=150,y=240)
lab_6=Label(sign,font=('arial',12,'bold'),text="Sex",bg="light blue")\
    .place(x=150,y=280)
lab_7=Label(sign,font=('arial',12,'bold'),text="Salary",bg="light blue")\
    .place(x=150,y=320)
lab_8=Label(sign,font=('arial',12,'bold'),text="Mobile No.",bg="light blue")\
    .place(x=150,y=360)
lab_9=Label(sign,font=('arial',12,'bold'),text="Email",bg="light blue")\
    .place(x=150,y=400)
lab_10=Label(sign,font=('arial',12,'bold'),text="User Name",bg="light blue")\
    .place(x=150,y=440)
lab_11=Label(sign,font=('arial',12,'bold'),text="Password",bg="light blue")\
    .place(x=150,y=480)
entry1=Entry(sign,textvariable=v1).place(x=290,y=124)
entry2=Entry(sign,textvariable=v2).place(x=290,y=164)
entry3=Entry(sign,textvariable=v3).place(x=290,y=204)
entry4=Entry(sign,textvariable=v4).place(x=290,y=244)
entry5=Entry(sign,textvariable=v5).place(x=290,y=324)
entry6=Entry(sign,textvariable=v6).place(x=290,y=364)
entry7=Entry(sign,textvariable=v7).place(x=290,y=404)
entry8=Entry(sign,textvariable=v8).place(x=290,y=444)
entry9=Entry(sign,textvariable=v9).place(x=290,y=484)
radio_1=Radiobutton(sign,font=('arial',12,'bold'),text="Male",padx=10,variable=v,
                    command=choice,value=1,bg="light blue").place(x=260,y=278)
radio_2=Radiobutton(sign,font=('arial',12,'bold'),text="Female",padx=10,variable=v,
                    command=choice,value=2,bg="light blue").place(x=340,y=278)
btn_1=Button(sign,font=('arial',15,'bold'),text="Submit",bg="green",bd=10,
             command=submit).place(x=345,y=515)
btn_2=Button(sign,font=('arial',15,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=460,y=515)
sign.mainloop()