import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
login=Tk()
photo=PhotoImage(file='LOGIN.png')
label=Label(login,image=photo).place(x=-2,y=-2)
login.geometry('550x275')
login.title("Login")
v1=StringVar()
v2=StringVar()
def submit():
    user=v1.get()
    pwd=v2.get()
    db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
    cursor=db.cursor()
    cursor.execute("select username,password from detail")
    l=cursor.fetchall()
    t=user,pwd
    if t in l:
        messagebox.showinfo("","Login successfull")
        login.destroy()
        f=open("user.txt","w")
        f.write(user)
        f.close()
        if user=="admin":
            os.system("admin.py")
        else:
            os.system("employee.py")
    else:
        v1.set('')
        v2.set('')
        messagebox.showerror("Error","Username or password invalid")
def back():
    login.destroy()
    os.system("main.py")
lab_1=Label(login,font=('arial',50,'bold'),text="LOGIN",fg="dark blue",
            bg="light blue").place(x=170,y=5)
lab_2=Label(login,font=('arial',12,'bold'),text="User Name",bg="light blue")\
    .place(x=140,y=120)
lab_3=Label(login,font=('arial',12,'bold'),text="Password",bg="light blue")\
    .place(x=140,y=160)
entry1=Entry(login,textvariable=v1).place(x=280,y=123)
entry2=Entry(login,textvariable=v2,show='*').place(x=280,y=163)
btn_1=Button(login,font=('arial',15,'bold'),text="Submit",bg="gold",bd=10,
             command=submit).place(x=350,y=205)
btn_2=Button(login,font=('arial',15,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=460,y=205)
login.mainloop()