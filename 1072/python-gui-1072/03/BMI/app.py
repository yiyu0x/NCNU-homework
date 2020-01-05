from tkinter import *

def cal():
	w = int(weightE.get())
	h = float(heightE.get())
	BMI = round(w / (h * h), 2)
	print('BMI:', BMI)
	if BMI < 18.5:
		sign.config(text='BMI: ' + str(BMI) + ' you are too thin')
	elif BMI >= 24:
		sign.config(text='BMI: ' + str(BMI) + ' you are too heavy')
	else:
		sign.config(text='BMI: ' + str(BMI) + ' good!')


root = Tk()

heightL = Label(root, text="height(m)")
heightL.grid(row=0)

weightL = Label(root, text="weight(kg)")
weightL.grid(row=1)

heightE = Entry(root)
weightE = Entry(root)
heightE.grid(row=0, column=1)
weightE.grid(row=1, column=1)
submit = Button(root, text="submit", command=cal)
submit.grid(row=2)
sign = Label(root, text="")
sign.grid(row=2, column=1)
root.mainloop()

