import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
pwd=Tk()
photo=PhotoImage(file='PASSWORD.png')
label=Label(pwd,image=photo).place(x=-2,y=-2)
pwd.geometry('910x320')
pwd.title("Change Password")
v1=StringVar()
v2=StringVar()
v3=StringVar()
def submit():
    f=open('user.txt','r')
    a=f.read()
    f.close()
    op=v1.get()
    np=v2.get()
    rp=v3.get()
    db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
    cursor=db.cursor()
    cursor.execute("select password from detail where username='%s'"%a)
    k=cursor.fetchone()
    if op in k:
        if np==rp:
            cursor.execute("update detail set password='%s' where username='%s'"
                           %(np,a))
            db.commit()
            messagebox.showinfo("","Password changed")
            back()
        else:
            v2.set('')
            v3.set('')
            messagebox.showerror("Error","Passwords are not matching")
    else:
        v1.set('')
        messagebox.showerror("Error","Old password is invalid")
def back():
    pwd.destroy()
    os.system("profile.py")
lab_1=Label(pwd,font=('arial',50,'bold'),text="CHANGE PASSWORD",fg="steel blue",
            bg="light blue").place(x=130,y=5)
lab_2=Label(pwd,font=('arial',12,'bold'),text="Old Password",bg="light blue")\
    .place(x=320,y=120)
lab_3=Label(pwd,font=('arial',12,'bold'),text="New Password",bg="light blue")\
    .place(x=320,y=160)
lab_4=Label(pwd,font=('arial',12,'bold'),text="Confirm Password",bg="light blue")\
    .place(x=320,y=200)
entry1=Entry(pwd,textvariable=v1).place(x=530,y=123)
entry2=Entry(pwd,textvariable=v2).place(x=530,y=163)
entry3=Entry(pwd,textvariable=v3).place(x=530,y=203)
btn_1=Button(pwd,font=('arial',15,'bold'),text="Submit",bg="green",bd=10,
             command=submit).place(x=700,y=250)
btn_2=Button(pwd,font=('arial',15,'bold'),text="Back",bg="red",bd=10,command=back)\
    .place(x=820,y=250)
pwd.mainloop()