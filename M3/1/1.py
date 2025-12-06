from customtkinter import *
from PIL import Image

img = Image.open("3.png")
C_img = CTkImage(light_image=img, size=(150,50))

window = CTk()
label = CTkLabel(window, image=CTkImage(light_image=Image.open("3.png"), size=(150,50)), text ="")
label.pack()

b = CTkButton(window, image=C_img, text="Відправити", width=200, height=200 )
b.pack()

window.mainloop()