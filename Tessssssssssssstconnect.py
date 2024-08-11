import os
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import sqlite3

def back():
    root.destroy()
    os.system("python User_Loginn.py")

def summit():
    username = Enter_username.get()
    first_name = Enter_first_name.get()
    last_name = Enter_last_name.get()
    password = Enter_password.get()
    mother_name = Enter_mother_name.get()

    if not username or not first_name or not last_name or not password or not mother_name:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO user (username, first_name, last_name, password, mother_name) VALUES (?, ?, ?, ?, ?)",
                       (username, first_name, last_name, password, mother_name))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Successfully created, go and log in again")
    root.destroy()
    os.system("python User_Loginn.py")



def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.title('Event management system')
root.iconbitmap('assests/ticket_856232.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')

img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root, image=img1)
label_photo.pack()
createAccountFrame = ctk.CTkFrame(root, corner_radius=60, width=700, height=500, fg_color="#262624", bg_color='#7B9976')
createAccountFrame.place(x=20, y=150)
title = ctk.CTkLabel(createAccountFrame, text='Create Account', pady=15, font=('Times New Roman', 30, 'bold'),
                     text_color="#7B9976")
title.place(relx=0.5, y=50, anchor=ctk.CENTER)

slogan = ctk.CTkLabel(createAccountFrame, text='Join us and book with ease', pady=15, font=('Times New Roman', 20),
                      text_color="#7B9976")
slogan.place(relx=0.5, y=100, anchor=ctk.CENTER)

Enter_username = ctk.CTkEntry(createAccountFrame, placeholder_text='Username', corner_radius=10, width=280, height=30)
Enter_username.place(relx=0.5, y=150, anchor=ctk.CENTER)

Enter_first_name = ctk.CTkEntry(createAccountFrame, placeholder_text='First Name', corner_radius=10, width=280,
                                height=30)
Enter_first_name.place(relx=0.5, y=200, anchor=ctk.CENTER)

Enter_last_name = ctk.CTkEntry(createAccountFrame, placeholder_text='Last Name', corner_radius=10, width=280, height=30)
Enter_last_name.place(relx=0.5, y=250, anchor=ctk.CENTER)

Enter_password = ctk.CTkEntry(createAccountFrame, placeholder_text='Password', show='*', corner_radius=10, width=280,
                              height=30)
Enter_password.place(relx=0.5, y=300, anchor=ctk.CENTER)

Enter_mother_name = ctk.CTkEntry(createAccountFrame, placeholder_text="What's your mother's name?", corner_radius=10,
                                 width=280, height=30)
Enter_mother_name.place(relx=0.5, y=350, anchor=ctk.CENTER)
back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(createAccountFrame, text='', fg_color='#262724', hover='#262724', image=back_image, width=40,
                         hover_color='#7B9B75', command=back)
but_back.place(x=20, y=20)

but_Submit = ctk.CTkButton(createAccountFrame, text='Submit', font=('Times New Roman', 20, 'bold'),
                           hover_color='#7B9976', text_color='#262624', bg_color='#262624', fg_color='#7B9976',
                           command=summit)
but_Submit.place(relx=0.5, y=400, anchor=ctk.CENTER)
change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)

root.mainloop()