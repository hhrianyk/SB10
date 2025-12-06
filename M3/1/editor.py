from customtkinter import *
from PIL import Image, ImageFilter

win = CTk()
win.geometry("600x500")
set_default_color_theme("green")

image_ctk = CTkImage(light_image=Image.open("3.png"), size=  (350, 200))
label_img = CTkLabel(win, image=image_ctk, text = "")
label_img.pack(pady = 100)

set_fram = CTkFrame(win)
set_fram.pack(pady = 20, side="bottom")

image = Image.open("3.png")

def do_wb():
    global image
    image = image.convert("L")
    image_ctk.configure(light_image=image)
    label_img.configure(image=image_ctk)

def do_Blur():
    global image
    image = image.filter(ImageFilter.BLUR)
    image_ctk.configure(light_image=image)
    label_img.configure(image=image_ctk)
img_griginal = Image.open("3.png")
def do_Original():
    global image
    image = img_griginal
    image_ctk.configure(light_image=image)
    label_img.configure(image=image_ctk)
def do_Save():
    global image
    image.save("new_3.png")
btn_bw = CTkButton(set_fram, text="BW", command=do_wb)
btn_bw.grid(row = 0, column = 0,padx =  10)

btn_blur = CTkButton(set_fram, text="BLUR", command=do_Blur)
btn_blur.grid(row = 0, column = 1,padx =  10)

btn_Original = CTkButton(set_fram, text="Скинути", command=do_Original)
btn_Original.grid(row = 0, column = 2,padx =  10)

btn_Save = CTkButton(set_fram, text="Sava", command=do_Save)
btn_Save.grid(row = 1, column = 1,pady =  10)

win.mainloop()
