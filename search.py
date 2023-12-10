import os
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
search=Tk()
photo=PhotoImage(file='SEARCH.png')
label_1=Label(search,image=photo).place(x=-2,y=-2)
search.geometry('610x700')
search.title("Search Employee Details")
v=IntVar()
v.set('')
def submit():
    global l
    l.destroy()
    i=v.get()
    l=Listbox(search,font=('arial',20,'bold'),width=37,height=12)
    db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
    cursor=db.cursor()
    cursor.execute("select id from detail")
    a=cursor.fetchall()
    t=i,
    if t in a:
        cursor.execute("select * from detail x,dept y where x.dept_no=y.dept_no and id=%s "%i)
        k=cursor.fetchone()
        l.insert(1,"ID No. : "+str(k[0]))
        l.insert(2,"Name : "+k[1])
        l.insert(3,"Designation : "+k[2])
        l.insert(4,"Department No. : "+str(k[3]))
        l.insert(5,"Department Name : "+k[12])
        l.insert(6,"Date of Birth : "+str(k[4]))
        l.insert(7,"Sex : "+k[5])
        l.insert(8,"Salary : "+str(k[6]))
        l.insert(9,"Mobile No. : "+k[7])
        l.insert(10,"Email : "+k[8])
        l.insert(11,"Username : "+k[9])
        l.insert(12,"Password : "+k[10])
    else:
        v.set('')
        l.insert(1,"No details found")
        messagebox.showerror("Error","ID No. invalid")
    l.place(x=30,y=180)
def back():
    search.destroy()
    os.system("control.py")
lab_1=Label(search,font=('arial',50,'bold'),text="SEARCH",fg="violet",
            bg="light blue").place(x=170,y=5)
lab_2=Label(search,font=('arial',20,'bold'),text="ID No.",bg="light blue")\
    .place(x=30,y=120)
btn_1=Button(search,font=('arial',15,'bold'),text="Submit",bg="green",bd=5,
             command=submit).place(x=500,y=116)
btn_2=Button(search,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=482,y=610)
entry=Entry(search,font=('arial',20,'bold'),textvariable=v,width=22)\
    .place(x=140,y=122)
l=Listbox(search,font=('arial',20,'bold'),width=37,height=12)
l.place(x=30,y=180)
search.mainloop()