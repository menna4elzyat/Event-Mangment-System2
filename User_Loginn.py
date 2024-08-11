import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

def backkk():
    root.destroy()
    os.system("python login_as.py")


def createe():
    root.destroy()
    os.system("python Creatte_accc.py")


def loginpage():
    conn = sqlite3.connect("database.db")
    userconnect = conn.cursor()
    userconnect.execute("SELECT * from user WHERE username= ? and password= ?",
                         (Enter_user.get(), Enter_password.get()))
    user = userconnect.fetchone()
    if user:
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()
        os.system("python userpage.py")
    else:
        messagebox.showerror("Login", "Username or password incorrect!")
    conn.close()


def forgetpassword():
    root.destroy()
    os.system("python Forget_password.py")


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


root = ctk.CTk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
root.title("Event Management System")
root.iconbitmap("assests/ticket_856232.ico")
img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = tk.Label(root, image=img1)
label_photo.image = img1
label_photo.pack()

loginFrame = ctk.CTkFrame(root, corner_radius=40, width=700, height=500, bg_color='#7B9976', fg_color="#262724")
loginFrame.place(x=70, y=200)
title = ctk.CTkLabel(loginFrame, text='Log In', pady=15, font=('Times New Roman', 30, 'bold'), text_color="#7B9976")
title.place(relx=0.5, y=70, anchor=tk.CENTER)

slogan = ctk.CTkLabel(loginFrame, text='its time to have fuuuuuuun', pady=15, font=('Times New Roman', 20),
                      text_color="#7B9976")
slogan.place(relx=0.5, y=120, anchor=tk.CENTER)

Enter_user = ctk.CTkEntry(loginFrame, placeholder_text='Username', corner_radius=10, width=280, height=30)
Enter_user.place(relx=0.5, y=220, anchor=tk.CENTER)

Enter_password = ctk.CTkEntry(loginFrame, placeholder_text='Password', show='*', corner_radius=10, width=280, height=30)
Enter_password.place(relx=0.5, y=275, anchor=tk.CENTER)

but_Login = ctk.CTkButton(loginFrame, text='Login', font=('Times New Roman', 20, 'bold'), fg_color="#7B9976",
                          hover_color="#7B9976", text_color='#262724', command=loginpage)

but_Login.place(relx=0.5, y=360, anchor=tk.CENTER)
back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(loginFrame, text='', fg_color='#262724', hover='#262724', image=back_image, width=40,
                         hover_color='#7B9B75', command=backkk)

but_back.place(x=20, y=20)

but_CreateAccount = ctk.CTkButton(loginFrame, text='Create Account', font=('Times New Roman', 15),

                                  text_color='#7B9976',
                                  fg_color='#262724', hover_color='#262724', command=createe

                                  )
but_CreateAccount.place(relx=0.3, y=400, anchor=tk.CENTER)

but_ForgotPassword = ctk.CTkButton(
    loginFrame,
    text='Forgot Password',
    font=('Times New Roman', 15),
    text_color='#7B9976',
    fg_color='#262724',  hover_color='#262724'
    , command=forgetpassword
)
but_ForgotPassword.place(relx=0.7, y=400, anchor=tk.CENTER)
change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)

root.mainloop()