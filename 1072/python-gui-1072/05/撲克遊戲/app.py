from tkinter import *
from tkinter import messagebox
import random

root = Tk()
frame = Frame(root)
frame.pack()
cardFrame = Frame(root)
cardFrame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
# ♠2660 ♥2665 ♣2663 ♦2666

def ranCard():
    global myCards
    # print('in ranCard: ', myCards)
    card = ''
    while card in myCards:
        num = random.randint(1, 13) # 1~13
        color = random.randint(1, 4)
        if num == 1:
            num = 'A'
        elif num == 11:
            num = 'J'
        elif num == 12:
            num = 'Q'
        elif num == 13:
            num = 'K'
        if color == 1:
            color = '♠'
        elif color == 2:
            color = '♥'
        elif color == 3:
            color = '♣'
        elif color == 4:
            color = '♦'
        card = color + str(num)
    myCards.append(card)
    return card

def getCardColor(card):
    if card[0] in ['♠', '♣']:
        color = 'black'
    if card[0] in ['♥', '♦']:
        color = 'red'
    return color

def getAllCard():
    global myCards, pointInt, gameing
    cleanBox()
    myCards = ['']
    gameing = True
    color = ''
    # print('get all card: ', myCards)
    for i in range(5):
        card = ranCard()
        color = getCardColor(card)
        fiveCards[i].configure(text=card, fg=color)

    pointInt -= 10
    point.configure(text='點數: '+str(pointInt))
    giveCard.pack_forget()
    openCard.pack(side=LEFT)
    msg.configure(text='')
    # print('get all card: ', myCards)

def showChangeBtn():
    global gameing
    if gameing:
        changeCard.pack(side=LEFT)
    else:
        for i in radioBtnList:
            i.set(0)

def changeCard():
    global gameing
    gameing = False
    c = 0
    for i in radioBtnList:
        if i.get() == 1:
            card = ranCard()
            color = getCardColor(card)
            oldCard = fiveCards[c].cget("text")
            myCards.remove(oldCard)
            fiveCards[c].configure(text=card, fg=color)
        i.set(0)
        c += 1
    changeCard.pack_forget()
    openCard.pack()
    # print('changed card: ', myCards)

def setPoint(cardType):
    global pointInt, myCards
    pool = []
    pool_color = []
    pool_point = []
    for i in cardType:
        if cardType[i] != 0:
            pool.append(cardType[i])
    for i in myCards:
        pool_color.append(i[0])
        if i[1:] == 'A':
            pool_point.append(1)
        elif i[1:] == 'J':
            pool_point.append(11)
        elif i[1:] == 'Q':
            pool_point.append(12)
        elif i[1:] == 'K':
            pool_point.append(13)
        else:
            pool_point.append(int(i[1:]))


    pool_point = sorted(pool_point)
    print('點數:', pool_point)
    if len(set(pool_color)) == 1:
        if pool_point[0] + 1 == pool_point[1] and pool_point[0] + 2 == pool_point[2] and\
        pool_point[0] + 3 == pool_point[3] and pool_point[0] + 4 == pool_point[4]:
            msg.configure(text='同花順: +40點')
            pointInt += 40
        else:
            msg.configure(text='同花: +25點')
            pointInt += 25
    
    elif pool_point[0] + 1 == pool_point[1] and pool_point[0] + 2 == pool_point[2] and\
        pool_point[0] + 3 == pool_point[3] and pool_point[0] + 4 == pool_point[4]:
            msg.configure(text='順子: +20點')
            pointInt += 20

    elif 4 in pool:
        msg.configure(text='鐵支: +35點')
        pointInt += 35
    elif 3 in pool and 2 in pool:
        msg.configure(text='葫蘆: +30點')
        pointInt += 30
    elif 3 in pool:
        msg.configure(text='三條: +15點')
        pointInt += 15
    elif pool.count(2) == 2:
        msg.configure(text='兩對: +10點')
        pointInt += 10
    elif 2 in pool:
        msg.configure(text='一對: +5點')
        pointInt += 5
    
    point.configure(text='點數: '+str(pointInt))     

def cleanBox():
    for i in radioBtnList:
        i.set(0)

def showCard():
    cardType = {'A':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0,
               'J':0, 'Q':0, 'K':0}
    global myCards, pointInt, gameing
    gameing = False
    myCards.remove('')
    cleanBox()
    # set dic 
    for i in myCards:
        cardType[i[1:]] += 1
    setPoint(cardType)

    print('所有點數統計:', cardType)
    print('我拿到的牌:', myCards)

    giveCard.pack(side=LEFT)
    openCard.pack_forget()

    if pointInt < 10:
        messagebox.showinfo("QC","你輸了")
        giveCard.pack_forget()
    elif pointInt > 500:
        messagebox.showinfo("QC","你贏了")
        giveCard.pack_forget()

myCards = ['']
gameing = False
pointInt = 100
point = Label(frame, text='點數: '+str(pointInt))
point.pack()

radioBtnList = []
for i in range(5):
    radioBtnList.append(IntVar())
    radioBtnList[-1].set(0)

fiveCards = []
fiveBtn = []

c = 0
for i in range(5):
    l = Label(cardFrame, text='', width=5, heigh=10, relief="sunken", wraplengt=1)
    fiveCards.append(l)
    fiveCards[-1].grid(row=0, column=c, padx=10)
    r = Checkbutton(cardFrame, var=radioBtnList[c], offvalue=1, command=showChangeBtn)
    fiveBtn.append(r)
    fiveBtn[-1].grid(row=1, column=c, padx=10)
    c += 1

giveCard = Button(bottomframe, text='發牌', command=getAllCard)
giveCard.pack(side=LEFT)
openCard = Button(bottomframe, text='開牌', command=showCard)
openCard.pack_forget()
changeCard = Button(bottomframe, text='換牌', command=changeCard)
changeCard.pack_forget()
msg = Label(bottomframe, text='', fg='red')
msg.pack()
root.mainloop()