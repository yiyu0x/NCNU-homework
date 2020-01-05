from tkinter import * 
from datetime import datetime
def itemSelected(event):
    btnChoose.config(state="normal")
    obj = event.widget
    indexes = obj.curselection()
    s = ",".join([obj.get(i) for i in indexes])
    var.set(s) # Shown in label, rather than printing out.
def addItem():
    varAdd = entry.get()
    if (len(varAdd.strip()) == 0):
        return
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    lb.insert(END, time + ' ' + varAdd)
    entry.delete(0, END) # Clear the entry
def deleteItem():
    index = lb2.curselection() 
    if (len(index) == 0):
        return
    c = 0
    for i in index:
    	lb.insert(END, lb2.get(i-c))
    	lb2.delete(i-c)
    	c += 1
def deleteAll():
	c = lb2.size()
	for i in range(c):
		lb.insert(END, lb2.get(0))
		lb2.delete(0)

def chooseItem():
    btnChoose.config(state=DISABLED)
    btnFin.config(state="normal")
    index = lb.curselection() 
    if (len(index) == 0):
        return
    c = 0
    for i in index:
    	lb2.insert(END, lb.get(i-c))
    	lb.delete(i-c)
    	c += 1
def finItem():
    print('fin')
    btnFin.config(state=DISABLED)
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(time)
    new = lb2.get(0) + ' finishtime:' + ' ' + time
    lb2.delete(0)
    lb2.insert(END, new)

def chooseAll():
	c = lb.size()
	for i in range(c):
		lb2.insert(END, lb.get(0))
		lb.delete(0)

root = Tk()
F1 = Frame(root)
F2 = Frame(root)
F3 = Frame(root)
F1.pack(side='left')
F2.pack(side='left')
F3.pack(side='left')
#F1
var = StringVar()
label = Label(F1, text='todo list')
label.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(F1, width=12)
entry.grid(row=1, column=0, padx=5, pady=5)
btnAdd = Button(F1, text="Add", command=addItem)
btnAdd.grid(row=1, column=1, padx=5, pady=5)
boxList = Frame(F1)
boxList.grid(row=2, column=0)
scrollbar = Scrollbar(boxList)
scrollbar.pack(side=RIGHT, fill=Y)
lb = Listbox(boxList, selectmode=EXTENDED, yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)
lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack()

#F2
btnChoose = Button(F2, text="Start ▶", width=10, state=DISABLED ,command=chooseItem)
btnChoose.grid(row=0, column=1, padx=5, pady=5, sticky=W)
btnFin = Button(F2, text="Finish", width=10, state=DISABLED ,command=finItem)
btnFin.grid(row=4, column=1, padx=5, pady=5, sticky=W)
#F3
label2 = Label(F3, text='done list')
label2.grid(row=0, column=0, padx=5, pady=5)
l = Label(F3, text='') # use for layout
l.grid(row=1, column=0, padx=5, pady=5)
boxList2 = Frame(F3, width=500)
boxList2.grid(row=2, column=0)
scrollbar2 = Scrollbar(boxList2)
scrollbar2.pack(side=RIGHT, fill=Y)
lb2 = Listbox(boxList2, selectmode=EXTENDED, yscrollcommand=scrollbar.set)
scrollbar2.config(command=lb2.yview)
lb2.pack()
root.mainloop()