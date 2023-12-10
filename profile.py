import os
from tkinter import *
import mysql.connector as sql
profile=Tk()
photo=PhotoImage(file='PROFILE.png')
label_1=Label(profile,image=photo).place(x=-2,y=-2)
prof_photo=PhotoImage(file='PROFILE LOGO.png')
label=Label(profile,image=prof_photo).place(x=470,y=100)
profile.geometry('700x540')
profile.title("Profile")
f=open('user.txt','r')
a=f.read()
f.close()
db=sql.connect(host="localhost",user="root",passwd="usman",database="tk")
cursor=db.cursor()
cursor.execute("select * from detail where username='%s'"%a)
k=cursor.fetchone()
def password():
    profile.destroy()
    os.system("password.py")
def back():
    profile.destroy()
    if a=="admin":
        os.system("admin.py")
    else:
        os.system("employee.py")
lab_1=Label(profile,font=('arial',50,'bold'),text="PROFILE",fg="purple",
            bg="light blue").place(x=210,y=5)
lab_2=Label(profile,font=('arial',12,'bold'),text="ID No. : "+str(k[0]),
            bg="light blue").place(x=20,y=100)
lab_3=Label(profile,font=('arial',12,'bold'),text="Name : "+k[1],bg="light blue")\
    .place(x=20,y=140)
lab_4=Label(profile,font=('arial',12,'bold'),text="Designation : "+k[2],
            bg="light blue").place(x=20,y=180)
lab_5=Label(profile,font=('arial',12,'bold'),text="Department No. : "+str(k[3]),
            bg="light blue").place(x=20,y=220)
lab_6=Label(profile,font=('arial',12,'bold'),text="Date of Birth : "+str(k[4]),
            bg="light blue").place(x=20,y=260)
lab_7=Label(profile,font=('arial',12,'bold'),text="Sex : "+k[5],bg="light blue")\
    .place(x=20,y=300)
lab_8=Label(profile,font=('arial',12,'bold'),text="Salary : "+str(k[6]),
            bg="light blue").place(x=20,y=340)
lab_9=Label(profile,font=('arial',12,'bold'),text="Mobile No. : "+k[7],
            bg="light blue").place(x=20,y=380)
lab_10=Label(profile,font=('arial',12,'bold'),text="Email : "+k[8],bg="light blue")\
    .place(x=20,y=420)
lab_11=Label(profile,font=('arial',12,'bold'),text="Username : "+k[9],
             bg="light blue").place(x=20,y=460)
lab_12=Label(profile,font=('arial',12,'bold'),text="Password : "+k[10],
             bg="light blue").place(x=20,y=500)
btn_1=Button(profile,font=('arial',12,'bold'),text="Change password",bg="silver",
             bd=10,command=password).place(x=520,y=380)
btn_2=Button(profile,font=('arial',20,'bold'),text="Back",bg="red",bd=10,
             command=back).place(x=580,y=450)
profile.mainloop()