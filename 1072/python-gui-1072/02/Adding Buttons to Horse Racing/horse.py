from tkinter import *
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
Labels = []
inGame = True

##################
def init():
    for i in range(8):
        Labels[i].config(text='{}'.format(Horse + ' ' * 80 + '|'))
    msg.config(text='')
##################
def startGame():
    init()
    global inGame
    inGame = True
    for i in range(8):
        Labels[i].after(500, updateHorse, i, 0)
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
    ran = random.randrange(1, 20, 4)
    print('id:', id ,'ran:', ran, 'dis:', dis)
    dis += ran
    horse = dis * ' ' + Horse + (80 - dis) * ' ' + '|'
    if dis >= 80:
        horse = 80 * ' ' + Horse
        Labels[id].config(text=horse)
        endGame(id)
    else:
        Labels[id].config(text=horse)
        Labels[id].after(1000, updateHorse, id, dis)
def quit():
    root.destroy()
##################
for i in range(8):
    Labels.append(Label(root,
        text='{}'.format(Horse + ' ' * 80 + '|'),
        font=('Arial', 20),
        width=15,
        anchor='w'))
    Labels[i].pack(fill='both') # fill='both' can fill all father widget(window)
msg = Label(root, text='', anchor='center')
init()
msg.pack()
btn_Start = Button(root, text='Start', height=10, command=startGame)
btn_Start.pack(anchor=W)
btn_Restart = Button(root, text='Retart', height=10, command=startGame)
btn_Quit = Button(root, text='Quit', height=10, command=quit)
root.mainloop()