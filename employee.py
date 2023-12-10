import os
from tkinter import *
from tkinter import messagebox
emp=Tk()
photo=PhotoImage(file='PORTAL.png')
label=Label(emp,image=photo).place(x=-2,y=-2)
emp.geometry('520x350')
emp.title("Portal")
def profile():
    emp.destroy()
    os.system("profile.py")
def announcement():
    emp.destroy()
    os.system("announcement.py")
def complaint():
    emp.destroy()
    os.system("complaint.py")
def logout():
    messagebox.showinfo("","Logout successful")
    emp.destroy()
    os.system("main.py")
lab=Label(emp,font=('arial',50,'bold'),text="PORTAL",fg="indigo",
            bg="light blue").place(x=140,y=5)
btn_1=Button(emp,font=('arial',15,'bold'),text="Profile",bg="blue",bd=10,width=15,
             command=profile).place(x=40,y=122)
btn_2=Button(emp,font=('arial',15,'bold'),text="Announcements",bg="green",bd=10,
             width=15,command=announcement).place(x=280,y=122)
btn_3=Button(emp,font=('arial',15,'bold'),text="Complaints",bg="violet",bd=10,
             width=15,command=complaint).place(x=160,y=200)
btn_4=Button(emp,font=('arial',15,'bold'),text="Sign out",bg="red",bd=10,
             command=logout).place(x=210,y=278)
emp.mainloop()