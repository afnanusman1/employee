import os
from tkinter import *
from tkinter import messagebox
main=Tk()
main.geometry('490x290')
main.title("NAAK & Co.")
photo=PhotoImage(file='MAIN.png')
label=Label(main,image=photo).place(x=-40,y=-35)
def signin():
    main.destroy()
    os.system("login.py")
def exit():
    m=messagebox.askquestion("","Are you sure?")
    if m=="yes":
        main.destroy()
btn_1=Button(main,font=('arial',20,'bold'),text="Sign in",bg="gold",bd=10,
             command=signin).place(x=180,y=110)
btn_2=Button(main,font=('arial',20,'bold'),text="Exit",bg="red",bd=10,command=exit)\
    .place(x=200,y=200)
main.mainloop()