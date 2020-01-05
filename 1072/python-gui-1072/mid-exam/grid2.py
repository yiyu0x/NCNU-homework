from tkinter import *

def insert(ch):
    ch = str(ch)
    if ch == '←':
    	print('delete !')
    	e.delete(len(e.get())-1)
    else:
    	e.insert('end', ch)
root = Tk()
# root.title('hello')

R0 = Frame(root)
R1 = Frame(root)
R2 = Frame(root)
R3 = Frame(root)
R4 = Frame(root)
R5 = Frame(root)
R0.pack()
R1.pack()
R2.pack()
R3.pack()
R4.pack()
R5.pack()

e = Entry(R0, width=20)
e.pack()

Button(R1, text='`', borderwidth=2, relief="groove", width=3, command=lambda: insert('`')).grid(row=0, column=0)
for i in range(1, 10):
	Button(R1, text=i, borderwidth=2, relief="groove" , command=lambda i=i: insert(i)).grid(row=0, column=i)
Button(R1, text='0', borderwidth=2, relief="groove" , command=lambda: insert('0')).grid(row=0, column=10)
Button(R1, text='-', borderwidth=2, relief="groove" , command=lambda: insert('-')).grid(row=0, column=11)
Button(R1, text='=', borderwidth=2, relief="groove" , command=lambda: insert('=')).grid(row=0, column=12)
Button(R1, text='←', borderwidth=2, relief="groove" , command=lambda: insert('←')).grid(row=0, column=13)


row2 = ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\']
counter = 0
for i in row2:
	if counter == 0 or counter == 13:
		Button(R2, text=i, borderwidth=2, relief="groove", width=4, command=lambda i=i: insert(i)).grid(row=0, column=counter)
	else:
		Button(R2, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)).grid(row=0, column=counter)
	counter += 1

row3 = ['C.LOCK', 'a' , 's', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', ';', '\'', 'Enter']
counter = 0
for i in row3:
	if counter == 0 or counter == 13:
		Button(R3, text=i, borderwidth=2, relief="groove", width=5, command=lambda i=i: insert(i)).grid(row=0, column=counter)
	else:
		Button(R3, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)).grid(row=0, column=counter)
	counter += 1

row4 = ['Shift', 'z' , 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift']
counter = 0
for i in row4:
	if counter == 0 or counter == 11:
		Button(R4, text=i, borderwidth=2, relief="groove", width=7, command=lambda i=i: insert(i)).grid(row=0, column=counter)
	else:
		Button(R4, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)).grid(row=0, column=counter)
	counter += 1
 
row5 = ['Ctrl', 'Win' , 'Alt', '                        ', 'Alt', 'Win', 'Ctrl']
for i in row5:
	if counter == 3:
		Button(R5, text=i, borderwidth=2, relief="groove", width=15, command=lambda i=i: insert(i)).grid(row=0, column=counter)
	else:
		Button(R5, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)).grid(row=0, column=counter)
	counter += 1
root.mainloop()