from customtkinter import *
from PIL import Image, ImageFilter, ImageEnhance


win = CTk()
win.geometry('600x500')
set_default_color_theme('green')

image = Image.open('3.png')
image_ctk = CTkImage(light_image=image,size=(300,200))

label_img = CTkLabel(win, text='', image=image_ctk)
label_img.pack()



def do_BW():
    global image
    image = image.convert("L")
    image_ctk.configure(light_image=image)
    label_img.configure(image = image_ctk)

def do_Blur():
    global image
    image = image.filter(ImageFilter.BLUR)
    image_ctk.configure(light_image=image)
    label_img.configure(image = image_ctk)

def do_Rotate():
    global image
    image = image.rotate(90)
    image_ctk.configure(light_image=image)
    label_img.configure(image = image_ctk)


set_frame  = CTkFrame(win)
set_frame.pack(side = "bottom", pady=20)

btn_rotate = CTkButton(set_frame, text="Поворот на 90", command=do_Rotate)
btn_rotate.grid(row = 0, column = 0, padx= 10)

btn_blur = CTkButton(set_frame, text="Розмиття", command=do_Blur)
btn_blur.grid(row = 0, column = 1, padx= 10)

btn_L = CTkButton(set_frame, text="Ч/Б", command=do_BW)
btn_L.grid(row = 0, column = 2, padx= 10)



win.mainloop()
