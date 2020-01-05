# ch17_22.py - Spelling checker (with bugs)
from tkinter import *

def spellingCheck():
    text.tag_remove("spellErr", "1.0", END)
    textwords = text.get("1.0", END).split()
    print("Dictionary Contents\n", textwords)
    
    startChar = ("(")
    endChar = ('.', ',', '?', ')', '!', ':', ';')
    errorBox = {}
    start = "1.0"
    for word in textwords:
        if word[0] in startChar:
            word = word[1:]
        if word[-1] in endChar:
            word = word[:-1]
        if (word.lower() not in dicts):
            print("error", word)
            if word in errorBox:
                pos = text.search(word, errorBox[word], END)
            else:
                pos = text.search(word, start, END)
            text.tag_add("spellErr", pos, "%s+%dc" % (pos, len(word)))
            pos = "%s+%dc" % (pos, len(word))
            errorBox[word] = pos

def clrText():
    text.tag_remove("spellErr", "1.0", END)
    
root = Tk()
root.geometry("300x180")

# Toolbar
toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, padx=2, pady=1)

chkBtn = Button(toolbar, text="Check Spelling", command=spellingCheck)
clrBtn = Button(toolbar, text="Clear", command=clrText)
chkBtn.pack(side=LEFT, padx=5, pady=5)
clrBtn.pack(side=LEFT, padx=5, pady=5)

# Text
text = Text(root)
text.pack(fill=BOTH, expand=True)

text.insert(END, """This is a bok.
That is not a bok.
That is a caar.""")
text.tag_configure("spellErr", foreground="red")
with open("myDict.txt", "r") as infile:
    dicts = infile.read().split("\n")
dicts.append('a')
root.mainloop()
