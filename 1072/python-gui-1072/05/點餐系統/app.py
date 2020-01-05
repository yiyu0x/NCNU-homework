from tkinter import *

def printInfo():
	pass
	# print(all_widget[0][1].get())

def submit():
	money = 0
	c = 0
	for item in all_widget:
		if item[1].get() != '0':
			print(menu[c][0], item[1].get(), '份')
			money += menu[c][1] * int(item[1].get())
		c += 1
	print('總價:', money, '元')
root = Tk()


menu = [
	('原味蛋餅:20元', 20),
	('火腿蛋餅:40元', 40),
	('高級蛋餅:60元', 60),
	('原味漢堡:30元', 30),
	('薯餅漢堡:45元', 45),
	('美式漢堡:50元', 50),
	('紅茶:15元', 15),
	('奶茶:25元', 25),
	('咖啡:40元', 40)
]

all_widget = []
c = 0
for name in menu:
	# print(i)
	l = Label(root, text=name).grid(row=c, column=0)
	spin = Spinbox(root,
				from_=0,
				to_=20,
				command=printInfo)
	all_widget.append((c, spin))
	spin.grid(row=c, column=1)
	c += 1
Button(text='結帳', command=submit).grid(row=c, column=0)
root.mainloop()