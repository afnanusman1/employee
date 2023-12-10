import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sql
comp=Tk()
comp.geometry('1005x550')
comp.title("Complaints")
photo=PhotoImage(file='COMPLAINT.png')
label=Label(comp,image=photo).place(x=-2,y=-2)
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
f=open('user.txt','r')
a=f.read()
f.close()
sty_tab=ttk.Style()
sty_tab.theme_use("clam")
sty_tab.configure("Treeview",font=(None,12))
sty_tab.configure("Treeview.Heading",font=(None,20))
tab=ttk.Treeview(comp,columns=('date','id','name','prob','status'),show='headings',height=14)
tab.column('date',anchor=CENTER,width=89)
tab.column('id',anchor=CENTER,width=85)
tab.column('name',anchor=W,width=180)
tab.column('prob',anchor=W,width=542)
tab.column('status',anchor=W,width=87)
tab.heading('date',text='Date',anchor=CENTER)
tab.heading('id',text='ID No.',anchor=CENTER)
tab.heading('name',text='Name',anchor=W)
tab.heading('prob',text='Problem',anchor=W)
tab.heading('status',text='Status',anchor=W)
tab.place(x=10,y=120)
cursor.execute("select * from complaint order by date desc")
k=cursor.fetchall()
for i in range(len(k)):
    tab.insert(parent='',index=i,values=k[i])
def back():
    comp.destroy()
    os.system("admin.py")
def solve():
    s=tab.item(tab.selection())["values"]
    if s[4]=="Solved":
        messagebox.showerror("","Problem is already solved")
    else:
        m=messagebox.askquestion("","Are you sure?")
        if m=='yes':
            cursor.execute("update complaint set status='Solved' where id=%s and problem='%s'"
                           %(s[1],s[3]))
            db.commit()
            comp.destroy()
            os.system("admin_complaint.py")
lab=Label(comp,font=('arial',50,'bold'),text="COMPLAINTS",fg="dark red",
            bg="light blue").place(x=310,y=5)
btn_1=Button(comp,font=('arial',20,'bold'),text="Solve",bg="green",bd=10,
             command=solve).place(x=760,y=470)
btn_2=Button(comp,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=890,y=470)
comp.mainloop()