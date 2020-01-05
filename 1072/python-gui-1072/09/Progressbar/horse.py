from tkinter import *
from tkinter.ttk import *
import random

root = Tk()
# set window
root.title('Horse Racing')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 520
h = 320
root.geometry('{}x{}+{}+{}'.format(w, h,
									(screenWidth - w)//2, 
									(screenHeight - h)//2))
##################
# set labels
Horse = '~/-\\^'
# Labels = []
inGame = True

##################
def init():
    for i in range(8):
        P[i].config(value=0, maximum=100)
    msg.config(text='')
##################
def startGame():
    init()
    global inGame
    inGame = True
    for i in range(8):
        P[i].after(500, updateHorse, i, 0)
    btn_Start.pack_forget()
    btn_Restart.config(state='disable')
    # print(123)
##################

def endGame(id):
    global inGame
    msg.config(text='Horse ' + str(id+1) + ' wins!')
    inGame = False
    btn_Restart.config(state='normal')
    btn_Restart.pack(anchor=W, side='left')
    btn_Quit.pack(anchor=W, side='left')

def updateHorse(id, dis):
    global inGame
    if not inGame:
        return
    ran = random.randrange(1, 30, 5)
    print('id:', id ,'value', P[id]['value'])
    v = P[id]['value']
    P[id]['value'] += ran
    if P[id]['value'] >= 100:
        endGame(id)
    else:
        P[id].after(1000, updateHorse, id, dis)
def quit():
    root.destroy()
##################
P = []
for i in range(8):
    P.append(Progressbar(root, length=200))
    P[i].pack() # fill='both' can fill all father widget(window)
msg = Label(root, text='', anchor='center')
init()
msg.pack()
btn_Start = Button(root, text='Start', command=startGame)
btn_Start.pack(anchor=W)
btn_Restart = Button(root, text='Retart', command=startGame)
btn_Quit = Button(root, text='Quit', command=quit)
root.mainloop()