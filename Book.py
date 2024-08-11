import tkinter
from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os


def backkk():
    root1.destroy()
    os.system("python userpage.py")


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


root1 = ctk.CTk()
ctk.set_appearance_mode('system')
root1.title('Event management system')
root1.iconbitmap('assests/ticket_856232.ico')
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
center_x = 0
center_y = 0
root1.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')
img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root1, image=img1)
label_photo.pack()

outer_frame = Frame(root1)
outer_frame.pack(padx=5, pady=0, fill=BOTH, expand=True)

inner_frame = ctk.CTkFrame(root1, bg_color='#7E9779', fg_color='#262724', corner_radius=60, width=600, height=500)
inner_frame.place(relx=0.3, rely=0.47, anchor=tkinter.CENTER)

labelText = ctk.CTkLabel(inner_frame, text='Book Ticket', pady=10, text_color='#7B9B75',
                         font=('Times New Roman', 50, 'bold'))
labelText.place(x=180, y=15)

ctk.CTkLabel(inner_frame, text='Name', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50, y=135)
ctk.CTkEntry(inner_frame, width=300, height=30, font=('Times New Roman', 20, 'bold'),
             placeholder_text='Enter Your Name as Ahmed Hassan').place(x=210, y=140)

ctk.CTkLabel(inner_frame, text='Ticket Id', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50,
                                                                                                              y=215)
ctk.CTkEntry(inner_frame, state='disabled', width=300, height=30, font=('Times New Roman', 20, 'bold'),
             placeholder_text='Ticket Id').place(x=210, y=220)

ctk.CTkLabel(inner_frame, text='Event', text_color='#7B9976', font=('Times New Roman', 30, 'bold')).place(x=50, y=288)
ctk.CTkComboBox(inner_frame, width=300, height=30, values=['Event1', 'Event2'],
                font=('Times New Roman', 20, 'bold')).place(x=210, y=290)
back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(inner_frame, text='', fg_color='#262724', image=back_image, width=40, hover_color='#262724',
                         command=backkk)
but_back.place(x=20, y=20)
submitIcon = PhotoImage(file='assests/subb.png')
ctk.CTkButton(inner_frame, text='Submit', corner_radius=20, text_color='#262724', fg_color='#7B9976',
              hover_color='#7B9976', font=('Times New Roman', 30, 'bold'), image=submitIcon).place(x=210, y=400)

change_theme_box = ctk.CTkSwitch(master=root1, text='', bg_color='#7B9976', progress_color='#262724',
                                 fg_color='#262724', font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)
root1.mainloop()
