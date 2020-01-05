from tkinter import *
root = Tk()

label_tag = [[0, 1, 2], 
		     [3, 4, 5],
		     [6, 7, 8]]
label = []
counter = 0
####### set up #######
for i in range(3):
	tmp = []
	for j in range(3):
		if counter == 0:
			tmp.append(Label(root, text=' ', relief="raised", font=("Courier", 40), width=4, heigh=2))
		else:
			tmp.append(Label(root, text=str(counter), relief="raised", font=("Courier", 40), width=4, heigh=2))
		counter += 1
		tmp[-1].grid(row=i, column=j)
	label.append(tmp)
# ↑上 ↓下 ←左 →右

####### layout trash #######
Label(root, text='', font=("Courier", 40), width=4, heigh=2).grid(row=4, column=0)
Label(root, text='', font=("Courier", 40), width=4, heigh=2).grid(row=4, column=2)
Label(root, text='', font=("Courier", 40), width=4, heigh=2).grid(row=5, column=1)
Label(root, text='', font=("Courier", 40), width=4, heigh=2).grid(row=6, column=0)
Label(root, text='', font=("Courier", 40), width=4, heigh=2).grid(row=6, column=2)
############################
def showState():
	for i in range(3):
		for j in range(3):
			print(label[i][j]['text'], end=' ')
		print()
def move(pos):
	print(pos)
	if pos == 'up':
		for i in range(3):
			for j in range(3):
				if label[i - 1][j]['text'] == ' ':
					if i - 1 < 0: return
					print('x: ', str(i), ' y:', str(j), label[i][j]['text'])
					print('x: ', str(i - 1), ' y:', str(j), label[i - 1][j]['text'])
					l1 = label[i - 1][j]
					l2 = label[i][j]
					l1['text'], l2['text'] = l2['text'], l1['text']
					showState()
					return
	if pos == 'down':
		for i in range(2):
			for j in range(3):
				if label[i + 1][j]['text'] == ' ':
					if i + 1 > 2: return
					print('x: ', str(i), ' y:', str(j), label[i][j]['text'])
					print('x: ', str(i + 1), ' y:', str(j), label[i + 1][j]['text'])
					l1 = label[i + 1][j]
					l2 = label[i][j]
					l1['text'], l2['text'] = l2['text'], l1['text']
					showState()
					return
	if pos == 'left':
		for i in range(3):
			for j in range(3):
				if label[i][j - 1]['text'] == ' ':
					if j - 1 < 0: return
					print('x: ', str(i), ' y:', str(j), label[i][j]['text'])
					print('x: ', str(i), ' y:', str(j - 1), label[i][j - 1]['text'])
					l1 = label[i][j - 1]
					l2 = label[i][j]
					l1['text'], l2['text'] = l2['text'], l1['text']
					showState()
					return
	if pos == 'right':
		for i in range(3):
			for j in range(2):
				if label[i][j + 1]['text'] == ' ':
					if j + 1 > 2: return
					print('x: ', str(i), ' y:', str(j), label[i][j]['text'])
					print('x: ', str(i), ' y:', str(j + 1), label[i][j + 1]['text'])
					l1 = label[i][j + 1]
					l2 = label[i][j]
					l1['text'], l2['text'] = l2['text'], l1['text']
					showState()
					return


root.bind('<Left>', lambda pos='left': move(pos='left'))
root.bind('<Right>', lambda pos='left': move(pos='right'))
root.bind('<Up>', lambda pos='left': move(pos='up'))
root.bind('<Down>', lambda pos='left': move(pos='down'))
root.bind('<a>', lambda pos='left': move(pos='left'))
root.bind('<d>', lambda pos='left': move(pos='right'))
root.bind('<w>', lambda pos='left': move(pos='up'))
root.bind('<s>', lambda pos='left': move(pos='down'))

up = Button(root, text='↑', relief="raised", font=("Courier", 40), width=4, heigh=2, command=lambda: move('up'))
up.grid(row=4, column=1)
left = Button(root, text='←', relief="raised", font=("Courier", 40), width=4, heigh=2, command=lambda: move('left'))
left.grid(row=5, column=0)
right = Button(root, text='→', relief="raised", font=("Courier", 40), width=4, heigh=2, command=lambda: move('right'))
right.grid(row=5, column=2)
down = Button(root, text='↓', relief="raised", font=("Courier", 40), width=4, heigh=2, command=lambda: move('down'))
down.grid(row=6, column=1)
showState()
root.mainloop()