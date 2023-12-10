import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
delete=Tk()
photo=PhotoImage(file='DELETE.png')
label=Label(delete,image=photo).place(x=-2,y=-2)
delete.geometry('610x270')
delete.title("Delete Employee Details")
v=IntVar()
v.set('')
def submit():
    db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
    cursor=db.cursor()
    cursor.execute("select id from detail")
    a=cursor.fetchall()
    o=v.get()
    t=o,
    if t in a:
        m=messagebox.askquestion("","Are you sure?")
        if m=='yes':
            cursor.execute("delete from complaint where id=%s"%o)
            cursor.execute("delete from detail where id=%s"%o)
            db.commit()
            messagebox.showinfo("","Details deleted")
            delete.destroy()
            os.system("delete.py")
    else:
        v.set('')
        messagebox.showerror("Error","ID No. invalid")
def back():
    delete.destroy()
    os.system("control.py")
lab_1=Label(delete,font=('arial',50,'bold'),text="DELETE",fg="red",
            bg="light blue").place(x=200,y=5)
lab_2=Label(delete,font=('arial',20,'bold'),text="ID No.",bg="light blue")\
    .place(x=90,y=120)
btn_1=Button(delete,font=('arial',20,'bold'),text="Submit",bg="green",bd=10,
             command=submit).place(x=340,y=180)
btn_2=Button(delete,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=490,y=180)
entry=Entry(delete,font=('arial',20,'bold'),textvariable=v).place(x=200,y=122)
delete.mainloop()