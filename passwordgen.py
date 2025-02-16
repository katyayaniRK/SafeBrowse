import customtkinter as ctk
import random
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.title('Password Generater')
window.geometry('400x550')


def sendbtn():
    input = entrybox.get()
    textbox.insert('0.0', input)
  


textbox = ctk.CTkTextbox(window, width=300, height=200, corner_radius=10)
textbox.place(x=50, y=100)

entrybox = ctk.CTkEntry(window, placeholder_text='Enter your input', width=300, height=40, corner_radius=10)
entrybox.place(x=50, y=500)

submitbtn = ctk.CTkButton(window, text='send', command=sendbtn)
submitbtn.place(x=150, y=550)



window.mainloop()