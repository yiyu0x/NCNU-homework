from tkinter import *
import random

root = Tk()
# set window
root.title('Horse Racing')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 580
h = 250
root.geometry('{}x{}+{}+{}'.format(w, h,
									(screenWidth - w)//2, 
									(screenHeight - h)//2))
##################
# set labels
Horse = '~/-\\^'
Labels = []
inGame = True
for i in range(8):
    Labels.append(Label(root,
        text='{}'.format(Horse),
        font=('Arial', 20),
        width=15,
        anchor='w'))
    Labels[i].pack(fill='both') # fill='both' can fill all father widget(window)
msg = Label(root, text='', anchor='center')
msg.pack()
##################
def endGame(id):
    global msg, inGame
    msg.config(text='Horse ' + str(id+1) + ' wins!')
    inGame = False

def updateHorse(id, dis):
    global inGame
    if not inGame:
        return
    ran = random.randrange(1, 10, 2)
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

##################
for i in range(8):
    Labels[i].after(500, updateHorse, i, 0)
root.mainloop()