from tkinter import *
import random

file = open('source_eng.txt', 'r')
line = file.readlines()
chinese = []
english = []

for i, e in enumerate(line):
	if i % 2 == 0:
		english.append(e)ÏÏ
	else:
		chinese.append(e)

root = Tk()
root.geometry('600x100')
index = 0

def change():
	global index
	index += 1
	if index == len(english):
		index = 0
	b.set(english[index])

b = StringVar()
b.set(english[index])
Lab_text = Label(root, textvariable=b)
Btn_next = Button(root, text='Next', width = '30', command=change)
Lab_text.pack()
Btn_next.pack()

root.mainloop()