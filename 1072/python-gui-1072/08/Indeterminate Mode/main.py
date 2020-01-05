from tkinter import *
from tkinter.ttk import Progressbar
import time

def run():
	for i in range(100):
		pb["value"] = i + 1
		root.update()
		time.sleep(0.1)

root = Tk()
pb = Progressbar(root, length=200, mode="determinate", orient=HORIZONTAL)	
pb.pack(padx=10, pady=10)
btn = Button(root, text="Run", command=run)
btn.pack(pady=10)
root.mainloop()