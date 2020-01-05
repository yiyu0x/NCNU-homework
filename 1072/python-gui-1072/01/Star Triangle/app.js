from tkinter import *
root = Tk()
root.title('hello, world')
# root.geometry('800x600')
root.configure(bg='black')
# root.iconbitmap('./tree.ico')

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 800
h = 600
root.geometry('{}x{}+{}+{}'.format(w, h,
									(screenWidth - w)//2, 
									(screenHeight - h)//2))
def star(n):
    return '*' * n

for i in range(1, 9):
    Label(root, 
        text=star(i),
        fg='white',
        bg='black',     
        font=('Arial', 10),     
        width=15,
        anchor='center').pack()
root.mainloop()