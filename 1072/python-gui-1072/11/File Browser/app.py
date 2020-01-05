import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview



def process_directory(parent, path):
	#當前子目錄與檔案
	for p in os.listdir(path):
		abspath = os.path.join(path, p)
		isdir = os.path.isdir(abspath)
		# print('path:', path)
		# print('abspath:', abspath)
		if isdir:
			print('dir: ', p)
			oid = tree.insert(parent, 'end', open=False, text=p)
			process_directory(oid, abspath)
		else:
			print('file: ', p)
			tree.insert(parent, 'end', open=False, value=[p, os.path.getsize(abspath)])



root = Tk()

tree = Treeview(root, columns=("#1, #2"))
path ="./"
tree.heading('#0', text='Directory', anchor='w')
tree.heading('#1', text='Filename', anchor='w')
tree.heading('#2', text='Size', anchor='w')
abspath = os.path.abspath(path)
process_directory('', abspath)
tree.pack()
root.mainloop()
