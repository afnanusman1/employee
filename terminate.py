import os
from tkinter import *
from tkinter import ttk
import mysql.connector as sql
term=Tk()
term.geometry('1005x550')
term.title("Terminated Employees' Details")
photo=PhotoImage(file='TERMINATE.png')
label=Label(term,image=photo).place(x=-2, y=-2)
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
f=open('user.txt','r')
a=f.read()
f.close()
sty_tab=ttk.Style()
sty_tab.theme_use("clam")
sty_tab.configure("Treeview",font=(None,12))
sty_tab.configure("Treeview.Heading",font=(None,20))
tab=ttk.Treeview(term,columns=('name','desg','dno','dob','sex','sal','mob','email'),
                 show='headings',height=14)
tab.column('name',anchor=W,width=150)
tab.column('desg',anchor=W,width=180)
tab.column('dno',anchor=CENTER,width=115)
tab.column('dob',anchor=CENTER,width=89)
tab.column('sex',anchor=CENTER,width=58)
tab.column('sal',anchor=CENTER,width=86)
tab.column('mob',anchor=W,width=98)
tab.column('email',anchor=W,width=205)
tab.heading('name',text='Name',anchor=W)
tab.heading('desg',text='Designation',anchor=W)
tab.heading('dno',text='Dept No.',anchor=CENTER)
tab.heading('dob',text='DOB',anchor=CENTER)
tab.heading('sex',text='Sex',anchor=CENTER)
tab.heading('sal',text='Salary',anchor=CENTER)
tab.heading('mob',text='Mobile',anchor=W)
tab.heading('email',text='Email',anchor=W)
tab.place(x=10,y=120)
cursor.execute("select * from terminate")
k=cursor.fetchall()
for i in range(len(k)):
    tab.insert(parent='',index=i,values=k[i])
def back():
    term.destroy()
    os.system("control.py")
lab=Label(term,font=('arial',50,'bold'),text="TERMINATED",fg="indigo",
          bg="light blue").place(x=310,y=5)
btn=Button(term,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=890,y=470)
term.mainloop()