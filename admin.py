import os
from tkinter import *
from tkinter import messagebox
admin=Tk()
photo=PhotoImage(file='PORTAL.png')
label=Label(admin,image=photo).place(x=-2,y=-2)
admin.geometry('520x350')
admin.title("Admin Portal")
def profile():
    admin.destroy()
    os.system("profile.py")
def announcement():
    admin.destroy()
    os.system("admin_announcement.py")
def complaint():
    admin.destroy()
    os.system("admin_complaint.py")
def control():
    admin.destroy()
    os.system("control.py")
def logout():
    messagebox.showinfo("","Logout successful")
    admin.destroy()
    os.system("main.py")
lab=Label(admin,font=('arial',50,'bold'),text="PORTAL",fg="indigo",
            bg="light blue").place(x=140,y=5)
btn_1=Button(admin,font=('arial',15,'bold'),text="Profile",bg="blue",bd=10,width=15,
             command=profile).place(x=40,y=122)
btn_2=Button(admin,font=('arial',15,'bold'),text="Announcements",bg="green",bd=10,
             width=15,command=announcement).place(x=280,y=122)
btn_3=Button(admin,font=('arial',15,'bold'),text="Complaints",bg="violet",bd=10,
             width=15,command=complaint).place(x=40,y=200)
btn_4=Button(admin,font=('arial',15,'bold'),text="Employee Control",bg="light blue",
             width=15,bd=10,command=control).place(x=280,y=200)
btn_5=Button(admin,font=('arial',15,'bold'),text="Sign out",bg="red",bd=10,
             command=logout).place(x=210,y=278)
admin.mainloop()