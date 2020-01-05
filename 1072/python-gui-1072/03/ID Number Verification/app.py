from tkinter import *
import string

table = {
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15,
	'G': 16,
	'H': 17,
	'J': 18,
	'K': 19,
	'L': 20,
	'M': 21,
	'N': 22,
	'P': 23,
	'Q': 24,
	'R': 25,
	'S': 26,
	'T': 27,
	'U': 28,
	'V': 29,
	'X': 30,
	'Y': 31,
	'W': 32,
	'Z': 33,
	'I': 34,
	'O': 35
}
W = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
def val():
	s = heightE.get()
	if s[0] not in string.ascii_uppercase:
		sign.config(text="invalid")
		return
	if s[1] not in ['1', '2']:
		sign.config(text="invalid")
		return

	for i in range(1, 10):
		if s[i] not in string.digits:
			sign.config(text="invalid")
			return

	checksum = 0
	s = str(table[s[0]]) + s[1:]
	print(s)
	for i in range(11):
		checksum += int(s[i]) * W[i]
		print(s[i], '*', W[i])
	if checksum % 10 == 0:
		sign.config(text="valid!!!")
	else:
		sign.config(text="invalid")
	print('checksum:', checksum)

def checkLen(P):
	print(P)
	if len(P) is 10:
		submit['state'] = 'normal'
	else:
		submit['state'] = 'disabled'
	return True

root = Tk()
reg = root.register(checkLen)
IDL = Label(root, text="ID number")
IDL.grid(row=0)

heightE = Entry(root, validate='key', validatecommand=(reg, "%P"))
heightE.grid(row=0, column=1)
submit = Button(root, text="submit", state=DISABLED, command=val)
submit.grid(row=2)
sign = Label(root, text="")
sign.grid(row=2, column=1)
root.mainloop()