import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sql
comp=Tk()
comp.geometry('1005x620')
comp.title("Complaints")
photo=PhotoImage(file='COMPLAINT.PNG')
label=Label(comp,image=photo).place(x=-2,y=-2)
f=open('user.txt','r')
a=f.read()
f.close()
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
sty_tab=ttk.Style()
sty_tab.theme_use("clam")
sty_tab.configure("Treeview",font=(None,12))
sty_tab.configure("Treeview.Heading",font=(None,20))
tab=ttk.Treeview(comp,columns=('date','prob','status'),show='headings',height=14)
tab.column('date',anchor=CENTER,width=89)
tab.column('prob',anchor=W,width=807)
tab.column('status',anchor=W,width=87)
tab.heading('date',text='Date',anchor=CENTER)
tab.heading('prob',text='Problem',anchor=W)
tab.heading('status',text='Status',anchor=W)
tab.place(x=10,y=120)
cursor.execute("select id from detail where username='%s'"%a)
id=cursor.fetchone()
cursor.execute("select date,problem,status from complaint where id=%s order by date "
               "desc"%id[0])
k=cursor.fetchall()
for i in range(len(k)):
    tab.insert(parent='',index=i,values=k[i])
v=StringVar()
def submit():
    cursor.execute("select name from detail where username='%s'"%a)
    c=cursor.fetchone()
    cursor.execute("insert into complaint value(curdate(),%s,'%s','%s',default)"
                   %(id[0],c[0],v.get()))
    db.commit()
    messagebox.showinfo("","Complaint sent")
    comp.destroy()
    os.system("complaint.py")
def back():
    comp.destroy()
    os.system("employee.py")
lab_1=Label(comp,font=('arial',50,'bold'),text="COMPLAINTS",fg="dark red",
            bg="light blue").place(x=310,y=5)
lab_2=Label(comp,font=('arial',20,'bold'),text="Report problem",fg="black",
            bg="light blue").place(x=10,y=480)
entry=Entry(comp,font=('arial',20,'bold'),textvariable=v,width=43).place(x=240,y=481)
btn_1=Button(comp,font=('arial',15,'bold'),text="Submit",bg="green",bd=5,
             command=submit).place(x=905,y=476)
btn_2=Button(comp,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=890,y=540)
comp.mainloop()