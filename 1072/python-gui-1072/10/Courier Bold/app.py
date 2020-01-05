# ch17_8.py (modified from ch17_7.py) - Font Weight
from tkinter import *
from tkinter.font import Font

def familyChanged(event):
    f = Font(family=familyVar.get(), weight=weightVar.get())
    text.configure(font=f)
def weightChanged(event):
    f = Font(family=familyVar.get(), weight=weightVar.get())
    text.configure(font=f)
    
root = Tk()
root.geometry("300x180")

# Toolbar
toolbar = Frame(root, relief=RAISED, borderwidth=1)
toolbar.pack(side=TOP, fill=X, padx=2, pady=1)

# Font Family
fontFamilies = ("Arial", "Times", "Courier")
familyVar = StringVar(toolbar, fontFamilies[0])
family = OptionMenu(toolbar, familyVar, *fontFamilies, command=familyChanged)
family.pack(pady=2, side=LEFT)

# Font Weight
weightFamilies = ("normal", "bold")
weightVar = StringVar(toolbar, weightFamilies[0])
weight = OptionMenu(toolbar, weightVar, *weightFamilies, command=weightChanged)
weight.pack(pady=3, side=LEFT)

# Text
text = Text(root)
text.pack(fill=BOTH, expand=True, padx=3, pady=2)
text.focus_set()

root.mainloop()
