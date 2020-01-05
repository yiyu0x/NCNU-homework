from tkinter import *
from math import cos, sin, pi
import math
root = Tk()
canvas = Canvas(root, width=1200, height=800, bg='red') #初始化給定紅底
canvas.pack()
# canvas.create_rectangle(0, 0, 600, 400, fill='red') #國旗紅底
canvas.create_rectangle(0, 0, 600, 400, fill='blue') #國旗藍底

loc = []
center = [300, 200]
for i in range(0, 360, 30):
    loc.append([center[0] + 150*math.sin(math.radians(i)),
                center[1] + 150*math.cos(math.radians(i))])
locs = []
for i in range(12):
	x1 = loc[i][0] + ((loc[(i+7)%12][0] - loc[i][0]) / 3)
	y1 = loc[i][1] + ((loc[(i+7)%12][1] - loc[i][1]) / 3)
	x2 = loc[i][0] + ((loc[(i+5)%12][0] - loc[i][0]) / 3)
	y2 = loc[i][1] + ((loc[(i+5)%12][1] - loc[i][1]) / 3)
	locs.append([x1, y1])
	locs.append([loc[i][0], loc[i][1]])
	locs.append([x2, y2])

canvas.create_polygon(*locs, fill='white')
border = 10
canvas.create_oval(225-border, 125-border, 375+border, 275+border, fill='blue', outline='blue') #國旗 藍色圓形
canvas.create_oval(225  , 125  , 375  , 275  , fill='white', outline='white') #國旗 白色圓形

root.mainloop()