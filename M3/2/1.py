from customtkinter import *
from random import randint

win = CTk()
win.geometry('400x300')

def buttton_adaptive():
    window_width = win.winfo_width()
    window_height = win.winfo_height()
    btn.configure(width=window_width-100, height=window_height-100)
 
    win.after(50, buttton_adaptive)

lable = CTkLabel(win, text= "TEXT")
lable.place(x=50, y=40)
btn = CTkButton(win, text='', width=300, height=100)
btn.place(x=50, y=40)
buttton_adaptive()

win.mainloop()
