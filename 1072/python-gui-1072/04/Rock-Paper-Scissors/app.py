from tkinter import *

def getComputerChoice():
    import random
    choices = ["Rock", "Paper", "Scissor"]
    i = random.randint(0, 2)
    return choices[i]

def play():
	global win, lose, even
	computer = getComputerChoice()
	info = '我出: ' + var.get() + '電腦出: ' + computer
	print('me:', var.get())
	print('computer:', computer)
	if computer == var.get():
		even += 1
		msg_info.configure(text='平手!' + info)
	elif var.get() == "Rock" and computer == "Scissor" or \
		 var.get() == "Paper" and computer == "Rock" or \
		 var.get() == "Scissor" and computer == "Paper" :
		win += 1
		msg_info.configure(text='贏了!' + info)
	else:
		lose += 1
		msg_info.configure(text='輸了!' + info)
	msg.configure(text='贏:'+str(win)+' '+'輸:'+str(lose)+' '+'平手:'+str(even))

win = 0
lose = 0
even = 0

root = Tk()
frameUpper = Frame(root, background="lightyellow")
frameUpper.pack()
Label(frameUpper, text="猜拳程式", fg="blue", bg="lightyellow", width=30).pack()

frameLower = LabelFrame(root, bg="lightblue", text='請選擇你的出牌')
frameLower.pack()


imgPaper = PhotoImage(file="paper.gif")
imgRock = PhotoImage(file="rock.gif")
imgScissors = PhotoImage(file="scissors.gif")

var = StringVar()

Radiobutton(frameLower, image=imgPaper, text="布布",compound=RIGHT,variable=var,value="Paper", command=play).pack()
Radiobutton(frameLower, image=imgRock, text="石頭",compound=RIGHT,variable=var,value="Rock", command=play).pack()
Radiobutton(frameLower, image=imgScissors, text="剪刀",compound=RIGHT,variable=var,value="Scissor", command=play).pack()
msg = Label(root, text='贏:'+str(win)+' '+'輸:'+str(lose)+' '+'平手:'+str(even))
msg_info = Label(root, text='')
msg_info.pack()
msg.pack()

Button(root, text="離開", command=lambda:root.quit()).pack()
root.mainloop()
