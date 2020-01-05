from tkinter import * 
from math import cos, sin, pi
def printInfo():
	canvas.delete('all')	
	print(sp.get())
	N=int(sp.get())
	theta = 2*pi/N
	x0, y0, r = 320, 240, 90
	points = [ (x0 + r*cos(theta*i), y0 + r*sin(theta*i)) for i in range(N) ]
 
	canvas.create_polygon(*points, fill='blue') # aqua not in my python3.5 (macOS)
	for i in points:
		canvas.create_line([x0, y0], i)
	msg = 'Total inner angle: ' + str((N-2)*180) + 'degrees.'
	l.config(text=msg)
	print((N-2)*180)


root = Tk()
sp = Spinbox(root, from_=3, to_=30, command=printInfo)
sp.pack(pady=10, padx=10)

canvas = Canvas(root, width=640, height=480) 

l = Label(root, text='', font=("Courier", 30))
l.pack()
canvas.pack()

printInfo()
root.mainloop()