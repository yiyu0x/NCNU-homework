from tkinter import *
import string

def shiftCase():
    global isShift, ogR1, newR1, R1_BOX, btnBox
    isShift = not isShift
    if isShift:
        for i in shiftBox: #colorful
            i.config(highlightbackground="yellow")
            i.config(bg="yellow")
        for i, j in zip(R1_BOX, newR1): #change R1
            i.config(text=j, command=lambda j=j: insert(j))
        for i in btnBox:
            if i['text'] == '[':
                i.config(text='{', command=lambda: insert('{'))
            elif i['text'] == ']':
                i.config(text='}', command=lambda: insert('}'))
            elif i['text'] == '\\':
                i.config(text='|', command=lambda: insert('|'))
            elif i['text'] == ';':
                i.config(text=':', command=lambda: insert(':'))
            elif i['text'] == '\'':
                i.config(text='"', command=lambda: insert('"')) 
            elif i['text'] == ',':
                i.config(text='<', command=lambda: insert('<'))
            elif i['text'] == '.':
                i.config(text='>', command=lambda: insert('>'))
            elif i['text'] == '/':
                i.config(text='?', command=lambda: insert('?'))
    else:
        for i in shiftBox:
            i.config(highlightbackground=OG_color)
            i.config(bg=OG_color)
        for i, j in zip(R1_BOX, ogR1):
            i.config(text=j, command=lambda j=j: insert(j))
        for i in btnBox:
            if i['text'] == '{':
                i.config(text='[', command=lambda: insert('['))
            elif i['text'] == '}':
                i.config(text=']', command=lambda: insert(']'))
            elif i['text'] == '|':
                i.config(text='\\', command=lambda: insert('\\')) 
            elif i['text'] == ':':
                i.config(text=';', command=lambda: insert(';'))
            elif i['text'] == '"':
                i.config(text='\'', command=lambda: insert('\''))
            elif i['text'] == '<':
                i.config(text=',', command=lambda: insert(','))
            elif i['text'] == '>':
                i.config(text='.', command=lambda: insert('.'))
            elif i['text'] == '?':
                i.config(text='/', command=lambda: insert('/'))
def case():
    global upperCase, btnBox, CL
    upperCase = not upperCase
    if upperCase:
        CL.config(highlightbackground="yellow")
        CL.config(bg="yellow")
        for i in btnBox:
            if i['text'] in string.ascii_lowercase:
                up = i['text'].upper()
                i.config(text=up)
    else:
        CL.config(highlightbackground=OG_color)
        CL.config(bg=OG_color)
        for i in btnBox:
            if i['text'] in string.ascii_uppercase:
                low = i['text'].lower()
                i.config(text=low)

def insert(ch):
    global l
    print('get ch:', ch)
    global upperCase
    ch = str(ch)
    if ch == '←':
        print('delete !')
        l['text'] = l['text'][:-1]
        # e.delete(len(e.get())-1)
    else:
        if upperCase and ch in string.ascii_lowercase:
            # e.insert('end', ch.upper())
            l['text'] = l['text'] + ch.upper()
        else:
            # e.insert('end', ch)
            l['text'] = l['text'] + ch

root = Tk()
# root.title('hello')

R0 = Frame(root)
R1 = Frame(root)
R2 = Frame(root)
R3 = Frame(root)
R4 = Frame(root)
R5 = Frame(root)
R0.pack()
R1.pack()
R2.pack()
R3.pack()
R4.pack()
R5.pack()

# e = Entry(R0, width=20)
# e.pack()
l = Label(R0, width=60, bg='green')
l.pack()
newR1 =  ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
ogR1 =   ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
R1_BOX = []
R1_BOX.append(Button(R1, text='`', borderwidth=2, relief="groove", width=3, command=lambda: insert('`')))
R1_BOX[-1].grid(row=0, column=0)
for i in range(1, 10):
    R1_BOX.append(Button(R1, text=i, borderwidth=2, relief="groove" , command=lambda i=i: insert(i)))
    R1_BOX[-1].grid(row=0, column=i)
R1_BOX.append(Button(R1, text='0', borderwidth=2, relief="groove" , command=lambda: insert('0')))
R1_BOX[-1].grid(row=0, column=10)
R1_BOX.append(Button(R1, text='-', borderwidth=2, relief="groove" , command=lambda: insert('-')))
R1_BOX[-1].grid(row=0, column=11)
R1_BOX.append(Button(R1, text='=', borderwidth=2, relief="groove" , command=lambda: insert('=')))
R1_BOX[-1].grid(row=0, column=12)
Button(R1, text='←', borderwidth=2, relief="groove" , command=lambda: insert('←')).grid(row=0, column=13)


upperCase = False
isShift = False
row2 = ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\']
counter = 0
btnBox = []
shiftBox = []
for i in row2:
    if counter == 0 or counter == 13:
        btnBox.append(Button(R2, text=i, borderwidth=2, relief="groove", width=4))
        btnBox[-1].grid(row=0, column=counter)
        OG_color = btnBox[-1].cget("bg")
    else:
        btnBox.append(Button(R2, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)))
        btnBox[-1].grid(row=0, column=counter)
    counter += 1

row3 = ['C.LOCK', 'a' , 's', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', ';', '\'', 'Enter']
counter = 0
for i in row3:
    if counter == 0 or counter == 13:
        if counter == 0:
            btnBox.append(Button(R3, text=i, borderwidth=2, relief="groove", width=5, command=case))
            btnBox[-1].grid(row=0, column=counter)
            CL = btnBox[-1]
        else:
            btnBox.append(Button(R3, text=i, borderwidth=2, relief="groove", width=5))
            btnBox[-1].grid(row=0, column=counter)
    else:
        btnBox.append(Button(R3, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)))
        btnBox[-1].grid(row=0, column=counter)
    counter += 1

row4 = ['Shift', 'z' , 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift']
counter = 0
for i in row4:
    if counter == 0 or counter == 11:
        btnBox.append(Button(R4, text=i, borderwidth=2, relief="groove", width=7, command=shiftCase))
        btnBox[-1].grid(row=0, column=counter)
        shiftBox.append(btnBox[-1])
    else:
        btnBox.append(Button(R4, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)))
        btnBox[-1].grid(row=0, column=counter)
    counter += 1

counter = 0 
row5 = ['Ctrl', 'Win' , 'Alt', '                        ', 'Alt', 'Win', 'Ctrl']
for i in row5:
    if counter == 3:
        btnBox.append(Button(R5, text=i, borderwidth=2, relief="groove", width=15, command=lambda: insert(' ')))
        btnBox[-1].grid(row=0, column=counter)
    else:
        btnBox.append(Button(R5, text=i, borderwidth=2, relief="groove", command=lambda i=i: insert(i)))
        btnBox[-1].grid(row=0, column=counter)
    counter += 1
root.mainloop()