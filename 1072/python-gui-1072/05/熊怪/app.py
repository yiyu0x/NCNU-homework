from tkinter import *


# f = open('./bear.txt', 'r')
with open('./bear.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 



def printBear(source):
	beerStr = ''
	for i in range(sv.get()):
		beerStr += content[i] + '\n'
	print(beerStr)
	beer.config(text=beerStr)


root = Tk()
sv = Scale(root, from_=0, 
					to_=13, 
					resolution=1,   #移動一次多少
					# tickinterval=1,  #刻度間隔
					troughcolor="yellow",
					label='',
					length=300,      #bar長度
					command=printBear
					# orient=HORIZONTAL#bar水平, defalut是垂直
					)

beer = Label(root, text=' '*22, width=100)
beer.grid(row=0, column=0)
sv.grid(row=0, column=1)
root.mainloop()