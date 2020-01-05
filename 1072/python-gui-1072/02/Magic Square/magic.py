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
#
root = Tk()
N = 5
labels = []
counter = 1
# get magic matrix
magicMatrix = magic(5)

for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(Label(root, text=str(magicMatrix[i][j]), relief="raised", font=("Courier", 20), width=4, heigh=2))
    labels.append(tmp)

for i in range(N):
    for j in range(N):
        labels[i][j].grid(row=i, column=j)
root.mainloop()