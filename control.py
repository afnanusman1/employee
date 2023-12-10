import os
from tkinter import *
con=Tk()
photo=PhotoImage(file='CONTROL.png')
label=Label(con,image=photo).place(x=-2,y=-2)
con.geometry('830x390')
con.title("Employee Control")
def create():
    con.destroy()
    os.system("create.py")
def search():
    con.destroy()
    os.system("search.py")
def update():
    con.destroy()
    os.system("update.py")
def delete():
    con.destroy()
    os.system("delete.py")
def dept():
    con.destroy()
    os.system("dept_details.py")
def term():
    con.destroy()
    os.system("terminate.py")
def back():
    con.destroy()
    os.system("admin.py")
lab=Label(con,font=('arial',40,'bold'),text="EMPLOYEE CONTROL",fg="dark green",
            bg="light blue").place(x=130,y=5)
btn_1=Button(con,font=('arial',20,'bold'),text="Create",bg="blue",bd=10,
             command=create).place(x=60,y=122)
btn_2=Button(con,font=('arial',20,'bold'),text="Search",bg="green",bd=10,
             command=search).place(x=260,y=122)
btn_3=Button(con,font=('arial',20,'bold'),text="Update",bg="violet",bd=10,
             command=update).place(x=460,y=122)
btn_4=Button(con,font=('arial',20,'bold'),text="Delete",bg="light blue",bd=10,
             command=delete).place(x=660,y=122)
btn_5=Button(con,font=('arial',20,'bold'),text="Department Details",bg="orange",bd=10,
             command=dept).place(x=40,y=210)
btn_6=Button(con,font=('arial',20,'bold'),text="Terminated Employee's Details",bg="pink",bd=10,
             command=term).place(x=350,y=210)
btn_7=Button(con,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=695,y=300)
con.mainloop()