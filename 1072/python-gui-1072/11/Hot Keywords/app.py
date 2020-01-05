from tkinter import *
from tkinter.font import Font
import random
root = Tk()
t = Text(root)
t.pack()

def random_color():
    color = "%06x" % random.randint(0, 0xFFFFFF)
    table = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    return '#' + color

def main():
    fn = input("Filename? ")
    dict = getWordFromFile(fn)
    showDict(dict)

def getWordFromFile(filename):
    import re
    import string
    dict = {}
    with open(filename) as infile:
        s = infile.read()
        s = re.sub('['+string.punctuation+']', ' ', s)
        for word in s.split():            
            if len(word) > 0:
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
    return dict

def showDict(d): 
    counter = 0
    for k in d:
        if d[k] > 1:
            ran_color = random_color()
            print('ran:', ran_color)
            t.tag_config(str(counter), foreground=str(ran_color), font=Font(size=10+d[k]*5))
            print(k, ':', d[k])
            t.insert(END, str(k) + ' ', str(counter))
            counter += 1
    
main()
root.mainloop()