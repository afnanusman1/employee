import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
update=Tk()
photo=PhotoImage(file='UPDATE.png')
label=Label(update,image=photo).place(x=-2,y=-2)
update.geometry('650x455')
update.title("Update Employee Details")
v1=IntVar()
v2=IntVar()
v3=StringVar()
v1.set('')
def choice():
    o=v2.get()
    if o==1:
        s='Name'
    elif o==2:
        s='Designation'
    elif o==3:
        s='Dept_No'
    elif o==4:
        s='DOB'
    elif o==5:
        s='Sex'
    elif o==6:
        s='Salary'
    elif o==7:
        s='Mobile'
    elif o==8:
        s='Email'
    elif o==9:
        s='Username'
    else:
        s='Password'
    return s
def submit():
    db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
    cursor=db.cursor()
    cursor.execute("select id from detail")
    a=cursor.fetchall()
    o=v1.get()
    t=o,
    if t in a:
        c=choice()
        u=v3.get()
        cursor.execute("update detail set %s='%s' where id=%s"%(c,u,o))
        if c=="Name":
            cursor.execute("update complaint set Name='%s' where id=%s"%(u,o))
        db.commit()
        messagebox.showinfo("","Details updated")
        update.destroy()
        os.system("update.py")
    else:
        v1.set('')
        messagebox.showerror("Error","ID No. invalid")
def back():
    update.destroy()
    os.system("control.py")
lab_1=Label(update,font=('arial',50,'bold'),text="UPDATE",fg="orange",
            bg="light blue").place(x=180,y=5)
lab_2=Label(update,font=('arial',20,'bold'),text="ID No.",bg="light blue")\
    .place(x=30,y=120)
lab_3=Label(update,font=('arial',15,'bold'),
            text="Select the option which you want to update : ",fg="black",
            bg="light blue").place(x=30,y=180)
lab_4=Label(update,font=('arial',15,'bold'),text="Enter the change",bg="light blue")\
    .place(x=30,y=318)
btn_1=Button(update,font=('arial',20,'bold'),text="Submit",bg="green",bd=10,
             command=submit).place(x=370,y=370)
btn_2=Button(update,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=530,y=370)
entry_1=Entry(update,font=('arial',20,'bold'),textvariable=v1,width=32)\
    .place(x=140,y=122)
entry_2=Entry(update,font=('arial',15,'bold'),textvariable=v3,width=37)\
    .place(x=215,y=319)
radio_1=Radiobutton(update,font=('arial',12,'bold'),text="Name",padx=10,variable=v2,
                    command=choice,value=1,bg="light blue").place(x=30,y=220)
radio_2=Radiobutton(update,font=('arial',12,'bold'),text="Designation",padx=10,
                    variable=v2,command=choice,value=2,bg="light blue").place(x=130,y=220)
radio_3=Radiobutton(update,font=('arial',12,'bold'),text="Dept No.",padx=10,variable=v2,
                    command=choice,value=3,bg="light blue").place(x=278,y=220)
radio_4=Radiobutton(update,font=('arial',12,'bold'),text="DOB",padx=10,variable=v2,
                    command=choice,value=4,bg="light blue").place(x=400,y=220)
radio_5=Radiobutton(update,font=('arial',12,'bold'),text="Sex",padx=10,variable=v2,
                    command=choice,value=5,bg="light blue").place(x=492,y=220)
radio_6=Radiobutton(update,font=('arial',12,'bold'),text="Salary",padx=10,variable=v2,
                    command=choice,value=6,bg="light blue").place(x=30,y=260)
radio_7=Radiobutton(update,font=('arial',12,'bold'),text="Mobile No.",padx=10,
                    variable=v2,command=choice,value=7,bg="light blue").place(x=135,y=260)
radio_8=Radiobutton(update,font=('arial',12,'bold'),text="Email",padx=10,variable=v2,
                    command=choice,value=8,bg="light blue").place(x=273,y=260)
radio_9=Radiobutton(update,font=('arial',12,'bold'),text="Username",padx=10,
                    variable=v2,command=choice,value=9,bg="light blue").place(x=372,y=260)
radio_10=Radiobutton(update,font=('arial',12,'bold'),text="Password",padx=10,
                    variable=v2,command=choice,value=10,bg="light blue").place(x=508,y=260)
update.mainloop()