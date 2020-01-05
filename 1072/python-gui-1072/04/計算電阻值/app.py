from tkinter import *
def cal():
	s = (10 * colors.index(colors[var.get()]) + colors.index(colors[var2.get()])) * pow(10, colors.index(colors[var3.get()]))
	s /= 1000000
	msg.configure(text=str(s) + 'MΩ')
def printSelection():
	pass
	# print(colors[var.get()])
	# print(colors[var2.get()])
	# print(colors[var3.get()])

root = Tk()
colors = ['黑', '棕', '紅', '橙', '黃', '綠', '藍', '紫', '灰', '白']

var = IntVar()
var2 = IntVar()
var3 = IntVar()

var.set(0)
v = 0

Label(root, text='第一環', width=30).grid(row=0, column=0)
Label(root, text='第二環', width=30).grid(row=0, column=1)
Label(root, text='第三環', width=30).grid(row=0, column=2)

for i in colors:
	Radiobutton(root, text=i, variable=var, value=v, width=30
					, command=printSelection).grid(row=v+1, column=0)
	Radiobutton(root, text=i, variable=var2, value=v, width=30
					, command=printSelection).grid(row=v+1, column=1)
	Radiobutton(root, text=i, variable=var3, value=v, width=30
					, command=printSelection).grid(row=v+1, column=2)
	if v == 2:
		Button(root, text='計算電阻', width=30, command=cal).grid(row=2, column=3)

	v += 1

msg = Label(root, text='', width=30)
msg.grid(row=0, column=3)
root.mainloop()