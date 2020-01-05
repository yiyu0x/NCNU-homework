from tkinter import *
def magic(n):
    square = []
    for i in range(n + 1):
        square.append([0] * (n + 1))
    i = 0
    j = (n + 1) // 2
    for key in range(1, n ** 2 + 1):
        if key % n == 1:
            i += 1
        else:
            i -= 1
            j += 1
        if i == 0:
            i = n
        if j > n:
            j = 1
        square[i][j] = key
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    for k in range(len(matrix)):
        for l in range(len(matrix[0])):
            matrix[k][l] = square[k + 1][l + 1]
    return matrix
def createWin():
	windows = Toplevel()
	labels = []
	counter = 1
	# get magic matrix
	N = var.get()
	magicMatrix = magic(var.get())

	for i in range(N):
	    tmp = []
	    for j in range(N):
	        tmp.append(Label(windows, text=str(magicMatrix[i][j]), relief="raised", font=("Courier", 20), width=4, heigh=2))
	    labels.append(tmp)

	for i in range(N):
	    for j in range(N):
	        labels[i][j].grid(row=i, column=j)

root = Tk()
root.geometry("300x300")
var = IntVar()
var.set(0)

Radiobutton(root, text="5", variable=var, value=5, width=3).pack()
Radiobutton(root, text="7", variable=var, value=7, width=3).pack()
Radiobutton(root, text="9", variable=var, value=9, width=3).pack()
Button(root, text="確認", command=createWin).pack()

root.mainloop()