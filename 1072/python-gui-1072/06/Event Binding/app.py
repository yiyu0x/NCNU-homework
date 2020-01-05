from tkinter import *
from PIL import Image, ImageTk

img = Image.open('rgb.jpg')

def mouseMotion(event):
	x, y = event.x, event.y
	print(img.size, img.getpixel((x, y)))
	rgb = img.getpixel((x, y))
	hex_rgb = (format(rgb[0], 'x'), format(rgb[1], 'x'), format(rgb[2], 'x'))
	msg = str(img.size) + '(' + hex_rgb[0] + ',' + hex_rgb[1] + ',' + hex_rgb[2] + ')'
	rgb_msg.config(text=msg)

root = Tk()

img_png = ImageTk.PhotoImage(img)
label_img = Label(root, image=img_png)
label_img.pack()

rgb_msg = Label(root, text='')
rgb_msg.pack()

root.bind("<Button-1>", mouseMotion)
root.mainloop()