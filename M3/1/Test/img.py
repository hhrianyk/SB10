from PIL import Image, ImageFilter, ImageEnhance
from customtkinter import *

image = Image.open("3.png")
'''
image.show()
print(image.format)
print(image.size)
print(image.mode)

image.rotate(120).show()
image.convert("L").show()
image.filter(ImageFilter.BLUR ).show()
'''

window = CTk()
window.geometry("400x300")
window.maxsize(400, 300)

CTK_img = CTkImage(image, size=(100,400))
lable = CTkLabel(window, image=CTK_img, text="")
lable.pack()
window.mainloop()

