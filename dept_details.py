import os
from tkinter import *
from tkinter import ttk
import mysql.connector as sql
dept=Tk()
dept.geometry('1140x380')
dept.title("Department Details")
photo=PhotoImage(file='DEPT_DETAILS.png')
label=Label(dept, image=photo).place(x=-2, y=-2)
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
f=open('user.txt','r')
a=f.read()
f.close()
sty_tab=ttk.Style()
sty_tab.theme_use("clam")
sty_tab.configure("Treeview",font=(None,12))
sty_tab.configure("Treeview.Heading",font=(None,20))
tab=ttk.Treeview(dept, columns=('dno', 'name', 'hod', 'tot'),
                 show='headings', height=6)
tab.column('dno',anchor=CENTER,width=115)
tab.column('name',anchor=W,width=230)
tab.column('hod',anchor=W,width=558)
tab.column('tot',anchor=CENTER,width=210)
tab.heading('dno',text='Dept No.',anchor=CENTER)
tab.heading('name',text='Department Name',anchor=W)
tab.heading('hod',text='HOD',anchor=W)
tab.heading('tot',text='Employee Count',anchor=CENTER)
tab.place(x=10,y=120)
cursor.execute("select x.dept_no,x.name,hod,count(*) from dept x,detail y where x.dept_no="
                "y.dept_no group by y.dept_no order by x.dept_no")
k=cursor.fetchall()
for i in range(len(k)):
    tab.insert(parent='',index=i,values=k[i])
def back():
    dept.destroy()
    os.system("control.py")
lab=Label(dept, font=('arial', 50, 'bold'), text="DEPARTMENT DETAILS", fg="blue",
          bg="light blue").place(x=210,y=5)
btn=Button(dept, font=('arial', 20, 'bold'), text="Back", bg="red", bd=10,
           command=back).place(x=1020,y=300)
dept.mainloop()