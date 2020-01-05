from tkinter import *

def status(id):
	global showStatus1, showStatus2, showStatus3, showStatus4
	if id == 1:
		msg['text'] = 'Now drawing a Line'
		showStatus1.set(True)
		showStatus2.set(False)
		showStatus3.set(False)
		showStatus4.set(False)
		button_img1['relief'] = SUNKEN
		button_img2['relief'] = FLAT
		button_img3['relief'] = FLAT
		button_img4['relief'] = FLAT
	elif id == 2:
		msg['text'] = 'Now drawing a Curve'
		showStatus1.set(False)
		showStatus2.set(True)
		showStatus3.set(False)
		showStatus4.set(False)
		button_img1['relief'] = FLAT
		button_img2['relief'] = SUNKEN
		button_img3['relief'] = FLAT
		button_img4['relief'] = FLAT
	elif id == 3:
		msg['text'] = 'Now drawing a Oval'
		showStatus1.set(False)
		showStatus2.set(False)
		showStatus3.set(True)
		showStatus4.set(False)
		button_img1['relief'] = FLAT
		button_img2['relief'] = FLAT
		button_img3['relief'] = SUNKEN
		button_img4['relief'] = FLAT
	elif id == 4:
		msg['text'] = 'Now drawing a Rectangle'
		showStatus1.set(False)
		showStatus2.set(False)
		showStatus3.set(False)
		showStatus4.set(True)
		button_img1['relief'] = FLAT
		button_img2['relief'] = FLAT
		button_img3['relief'] = FLAT
		button_img4['relief'] = SUNKEN

root = Tk()
root.geometry("300x180")

showStatus1=BooleanVar(root, False)
showStatus2=BooleanVar(root, False)
showStatus3=BooleanVar(root, False)
showStatus4=BooleanVar(root, False)

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_checkbutton(label="Line", command=lambda: status(1), variable=showStatus1)
filemenu.add_checkbutton(label="Curve", command=lambda: status(2), variable=showStatus2)
filemenu.add_checkbutton(label="Oval", command=lambda: status(3), variable=showStatus3)
filemenu.add_checkbutton(label="Rectangle", command=lambda: status(4), variable=showStatus4)

msg = Label(root, text='')
toolbar=Frame(root, relief=RAISED, borderwidth=3)
button1_img_gif = PhotoImage(file = 'line.gif')
button2_img_gif = PhotoImage(file = 'curve.gif')
button3_img_gif = PhotoImage(file = 'oval.gif')
button4_img_gif = PhotoImage(file = 'rectangle.gif')
button_img1 = Button(toolbar, image = button1_img_gif, text = '', command=lambda: status(1))
button_img2 = Button(toolbar, image = button2_img_gif, text = '', command=lambda: status(2))
button_img3 = Button(toolbar, image = button3_img_gif, text = '', command=lambda: status(3))
button_img4 = Button(toolbar, image = button4_img_gif, text = '', command=lambda: status(4))
button_img1.pack(side='left')
button_img2.pack(side='left')
button_img3.pack(side='left')
button_img4.pack(side='left')
toolbar.pack(anchor=NE)
msg.pack()

root.mainloop()