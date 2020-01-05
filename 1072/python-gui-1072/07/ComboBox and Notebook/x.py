from tkinter import *
from tkinter.ttk import *
# root = Tk()
def f1b():
	if e1.get() not in item:
		item.append(e1.get())
		f2cb1.config(value=item)
		d[e1.get()] = e1.get() + '\n' + \
				'日期:' + varYear.get() + '/' + varMonth.get() + '/' + varDay.get() + '\n'\
				'花費' + e2.get()
		print(d)

def f2b():
	l2.config(text=d[target.get()])

d = {}
notebook = Notebook()
f1 = Frame()
f2 = Frame()
notebook.add(f1, text='新增')
notebook.add(f2, text='查詢')
notebook.pack()
############################## frame 1 ##############################
cbY = [y for y in range(2000, 2020)]
cbM = [m for m in range(1, 13)]
cbD = [d for d in range(1, 32)]
varYear = StringVar()
varDay = StringVar()
varMonth = StringVar()
label1 = Label(f1, text='欲新增的花費名稱')
e1 = Entry(f1)
label2 = Label(f1, text='年')
label3 = Label(f1, text='日')
label4 = Label(f1, text='月')
cb1 = Combobox(f1, textvariable=varYear, value=cbY)
cb2 = Combobox(f1, textvariable=varDay, value=cbD)
cb3 = Combobox(f1, textvariable=varMonth, value=cbM)
label5 = Label(f1, text='多少錢')
e2 = Entry(f1)
f1b = Button(f1, text='新增', command=f1b)

label1.grid(row=0, column=0)
e1.grid(row=0, column=1)
label2.grid(row=1, column=0)
cb1.grid(row=1, column=1)
label3.grid(row=2, column=0)
cb2.grid(row=2, column=1)
label4.grid(row=3, column=0)
cb3.grid(row=3, column=1)
label5.grid(row=4, column=0)
e2.grid(row=4, column=1)
f1b.grid(row=5, column=0)
############################## frame 2 ##############################
item = []
target = StringVar()
f2l1 = Label(f2, text='查詢')
f2cb1 = Combobox(f2, textvariable=target, value=item)
f2b = Button(f2, text='確定', command=f2b)
l2 = Label(f2, text='', font=("Courier", 44))
f2l1.grid(row=0, column=0)
f2cb1.grid(row=0, column=1)
f2b.grid(row=1, column=1)
l2.grid(row=2, column=1)
# note = []
# var = StringVar()
# var.set(note[0])
# cb = Combobox(f2, textvariable=var, value=note)
# cb.pack()

notebook.mainloop()