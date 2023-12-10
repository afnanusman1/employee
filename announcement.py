import os
from tkinter import *
from tkinter import ttk
import mysql.connector as sql
anno=Tk()
anno.geometry('1005x560')
anno.title("Announcements")
photo=PhotoImage(file='ANNOUNCEMENT.png')
label=Label(anno,image=photo).place(x=-2,y=-2)
f=open('user.txt','r')
a=f.read()
f.close()
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
sty_tab=ttk.Style()
sty_tab.theme_use("clam")
sty_tab.configure("Treeview",font=(None,12))
sty_tab.configure("Treeview.Heading",font=(None,20))
tab=ttk.Treeview(anno,columns=('date','event'),show='headings',height=15)
tab.column('date',anchor=CENTER,width=89)
tab.column('event',anchor=W,width=893)
tab.heading('date',text='Date',anchor=CENTER)
tab.heading('event',text='Event',anchor=W)
tab.place(x=10,y=120)
cursor.execute("select * from announcement order by date desc")
k=cursor.fetchall()
for i in range(len(k)):
    tab.insert(parent='',index=i,values=k[i])
def back():
    anno.destroy()
    os.system("employee.py")
lab=Label(anno,font=('arial',50,'bold'),text="ANNOUNCEMENTS",fg="navy blue",
            bg="light blue").place(x=220,y=5)
btn=Button(anno,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
           command=back).place(x=890,y=476)
anno.mainloop()