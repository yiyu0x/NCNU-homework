
# coding: utf-8

# In[5]:


# ch12_2.py - Listbox
from tkinter import * 
root = Tk()
root.geometry("300x180")
lb = Listbox(root)
for item in ['Banana', 'Watermelon', 'Pineapple']:
    lb.insert(END, item) # insert(index, item). END indicates the end of list. 
lb.pack(pady=10)
root.mainloop()


# In[7]:


# ch12_4.py - multiple selection
from tkinter import *
fruits = ["Banana", "Watermelon", "Pineapple",
         "Orange", "Grapes", "Mango"]
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=MULTIPLE) # Click each item which you want to selec for fruit in fruits:
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(pady=10)
root.mainloop()


# In[8]:


# ch12_5.py (modified from ch12_4.py) - selectmode=EXTENDED
# V
from tkinter import *
fruits = ["Banana", "Watermelon", "Pineapple",
         "Orange", "Grapes", "Mango"]
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=EXTENDED) # Shift-Click or Ctrl-Click for fruit in fruits:
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(pady=10)
root.mainloop()


# In[10]:


# ch12_6.py
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=EXTENDED)
fruits = ["Banana", "Watermelon", "Pineapple"] 
for fruit in fruits:
    lb.insert(END, fruit)
lb.insert(ACTIVE, "Orange", "Grapes", "Mango") #
lb.pack(pady=10) # Before you select an item, ACTIV
root.mainloop()


# In[13]:


# ch12_6a.py
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(ACTIVE, "Orange", "Grapes", "Mango", "Banana", "Watermelon", "Pineapple")
lb.pack(pady=10)
root.mainloop()


# In[14]:


# ch12_7.py (modified from ch12_5.py) - size()
from tkinter import *
fruits = ["Banana", "Watermelon", "Pineapple",
         "Orange", "Grapes", "Mango"]
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Orange", "Grapes", "Mango", "Banana", "Watermelon", "Pineapple") 
lb.pack(pady=10)
print("{} items.".format( lb.size() )) # size()
root.mainloop()


# In[17]:


# ch12_8.py - selection_set()
from tkinter import * 
root = Tk() 
root.geometry("300x180")
lb = Listbox(root)
lb.insert(ACTIVE, "Alice", "Emily")
lb.selection_set(1)
lb.pack()
lb.insert(ACTIVE, "Bob", "Carol", "Daniel") # ACTIVE==1, the selected item 
lb.insert(ACTIVE, "Here") 
root.mainloop()


# In[18]:


# ch12_9.py - select a range
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Orange", "Grapes", "Mango", "Banana", "Watermelon", "Pineapple") 
lb.pack(pady=10)
lb.selection_set(1, 3) # the second argument indicates the ending index 
root.mainloop()


# In[19]:


# ch12_10.py - delete an item
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo") 
lb.pack(pady=10)
lb.delete(1) # Remove "Bravo" from the list 
root.mainloop()


# In[22]:


# ch12_11.py - delete a range of items
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo") 
lb.pack(pady=10)
lb.delete(1, 3) # Remove "Bravo", "Charlie", "Delta" from the list 
root.mainloop()


# In[23]:


# ch12_12.py - access an item by index
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo") 
lb.pack(pady=10)
print( lb.get(1) )
root.mainloop()


# In[26]:


# ch12_13.py - access a range of items
from tkinter import *
root = Tk()
root.geometry("300x180")
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo") 
lb.pack(pady=10)
print( lb.get(3, 3) ) # those items are returned as a tuple 
root.mainloop()


# In[29]:


# ch12_14.py - curselection()
from tkinter import *
def callback():
    indexes = lb.curselection() # indexes of selected items for index in indexes:
    for index in indexes:
        print(lb.get(index))
root = Tk()
root.geometry("300x240")
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.pack(pady=10)
btn = Button(root, text="Print", command=callback)
btn.pack(pady=5)
root.mainloop()


# In[30]:


# ch12_14a.py - curselection()
from tkinter import *
def callback():
    indexes = lb.curselection() # indexes of selected items 
    print( indexes ) # returned as a tupple
root = Tk()
root.geometry("300x240")
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.pack(pady=10)
btn = Button(root, text="Print", command=callback)
btn.pack(pady=5)
root.mainloop()


# In[32]:


# ch12_15.py - check whether an item is selected
from tkinter import * 
def callback():
    print(lb.selection_includes(3))
root = Tk()
root.geometry("300x240")
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.pack(pady=10)
btn = Button(root, text="Check", command=callback)
btn.pack(pady=5)
root.mainloop()


# In[33]:


# ch12_16.py - <ListboxSelect> event
from tkinter import * 
def itemSelected(event):
    obj = event.widget
    index = obj.curselection()
    var.set(obj.get(index))
root = Tk()
root.geometry("300x240")
var = StringVar()
lab = Label(root, textvariable=var)
lab.pack(pady=5)
lb = Listbox(root)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack(pady=10)
root.mainloop()


# In[35]:


# ch12_18.py - multiple selection with <ListboxSelect> event
from tkinter import * 
def itemSelected(event):
    obj = event.widget
    indexes = obj.curselection() 
    for index in indexes:
        print(obj.get(index)) 
        print("-"*10)
root = Tk()
root.geometry("300x240")
var = StringVar()
lab = Label(root, textvariable=var)
lab.pack(pady=5)
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack(pady=10)
root.mainloop()


# In[36]:


# ch12_18a.py - Exercise: multiple selection with <ListboxSelect> event
from tkinter import * 
def itemSelected(event):
    obj = event.widget
    indexes = obj.curselection()
    s = ",".join([obj.get(i) for i in indexes])
    var.set(s) # Shown in label, rather than printing out.
root = Tk()
root.geometry("300x240")
var = StringVar()
lab = Label(root, textvariable=var)
lab.pack(pady=5)
lb = Listbox(root, selectmode=EXTENDED)
lb.insert(END, "Alpha", "Bravo", "Charlie", "Delta", "Foxtrot", "Echo")
lb.bind("<<ListboxSelect>>", itemSelected)
lb.pack(pady=10)
root.mainloop()


# In[39]:


# ch12_19.py
# V
from tkinter import * 
def addItem():
    varAdd = entry.get()
    if (len(varAdd.strip()) == 0):
        return
    lb.insert(END, varAdd)
    entry.delete(0, END) # Clear the entry
def deleteItem():
    index = lb.curselection() 
    if (len(index) == 0):
        return
    lb.delete(index)
root = Tk()
entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
btnAdd = Button(root, text="Add", width=10, command=addItem)
btnAdd.grid(row=0, column=1, padx=5, pady=5)
lb = Listbox(root)
lb.grid(row=1, column=0, columnspan=2, padx=5, sticky=W)
btnDel = Button(root, text="Delete", width=10, command=deleteItem)
btnDel.grid(row=1, column=1, padx=5, pady=5, sticky=W)
root.mainloop()


# In[42]:


# ch12_20.py - sort items in a listbox
from tkinter import *
def sortItems():
    if (var.get() == True):
        revBool = True 
    else:
        revBool = False
    listTmp = list(lb.get(0, END))
    sortedList = sorted(listTmp, reverse=revBool) 
    lb.delete(0, END) # delete all
    for item in sortedList: # and then insert
        lb.insert(END, item)
fruits = ['Banana', 'Watermelon', 'Pineapple',
              'Orange', 'Grapes', 'Mango']
root = Tk()
lb = Listbox(root) 
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack(padx=10, pady=5)
btn = Button(root, text="Sort", command=sortItems)
btn.pack(side=LEFT, padx=10, pady=5)
var = BooleanVar()
cb = Checkbutton(root, text="Descending", variable=var)
cb.pack(side=LEFT)
root.mainloop()


# In[45]:


# ch12_20a.py
from tkinter import *
def sortItems():
    if (var.get() == True):
        revBool = True 
    else:
        revBool = False
    sortedList = sorted(list(lb.get(0, END)), reverse=revBool) 
    lb.delete(0, END)
    lb.insert(END, *sortedList) # insert all items in a single statement
fruits = ['Banana', 'Watermelon', 'Pineapple',
          'Orange', 'Grapes', 'Mango']
root = Tk()
lb = Listbox(root)
lb.insert(END, *fruits) # insert all items in a single statement 
lb.pack(padx=10, pady=5)
btn = Button(root, text="Sort", command=sortItems)
btn.pack(side=LEFT, padx=10, pady=5)
var = BooleanVar()
cb = Checkbutton(root, text="Descending", variable=var)
cb.pack(side=LEFT)
root.mainloop()


# In[47]:


# ch12_21.py
from tkinter import * 
def getIndex(event):
    lb.index = lb.nearest(event.y) 
def drag(event):
    newIndex = lb.nearest(event.y)
    if newIndex < lb.index: # move upward
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex+1, x) 
        lb.index = newIndex
    elif newIndex > lb.index: # move downward x = lb.get(newIndex) lb.delete(newIndex) lb.insert(newIndex-1, x)
        lb.index = newIndex
root = Tk()
aList = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"] 
lb = Listbox(root)
for item in aList:
    lb.insert(END, item)
lb.bind("<Button-1>", getIndex)
lb.bind("<B1-Motion>", drag)
lb.pack(padx=10, pady=10)
root.mainloop()


# In[50]:


# ch12_21a.py
from tkinter import * 
def getIndex(event):
    lb.i = lb.nearest(event.y) # Don't override List.index()
def drag(event):
    newIndex = lb.nearest(event.y) 
    print(lb.i, lb.curselection()) 
    if newIndex < lb.i:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex+1, x) 
        lb.i = newIndex
    elif newIndex > lb.i:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex-1, x) 
        lb.i = newIndex
root = Tk()
aList = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"] 
lb = Listbox(root)
for item in aList:
    lb.insert(END, item)
lb.bind("<Button-1>", getIndex)
lb.bind("<B1-Motion>", drag)
lb.pack(padx=10, pady=10)
root.mainloop()


# In[52]:


# ch12_21b.py
from tkinter import *
def drag(event):
    oldIndex = lb.curselection()[0] # curselection() returns the index of the sel 
    newIndex = lb.nearest(event.y)
    if newIndex < oldIndex:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex+1, x)
    elif newIndex > oldIndex:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex-1, x)
root = Tk()
aList = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"] 
lb = Listbox(root)
lb.insert(END, *aList)
lb.bind("<B1-Motion>", drag)
lb.pack(padx=10, pady=10)
root.mainloop()


# In[54]:


# ch12_21c.py - listvariable
from tkinter import *
def drag(event):
    oldIndex = lb.curselection()[0] 
    newIndex = lb.nearest(event.y) 
    if newIndex < oldIndex:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex+1, x)
    elif newIndex > oldIndex:
        x = lb.get(newIndex) 
        lb.delete(newIndex) 
        lb.insert(newIndex-1, x)
root = Tk()
aList = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"] 
var = StringVar()
lb = Listbox(root, listvariable=var)
#lb.insert(END, *aList)
var.set( " ".join(aList) ) # set("A B C")
                           # get() returns "('A', 'B', 'C')
lb.bind("<B1-Motion>", drag)
lb.pack(padx=10, pady=10)
root.mainloop()


# In[55]:


# ch12_22.py - Scrollbar
# V
from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
lb = Listbox(root, yscrollcommand=scrollbar.set) # Set yscrollcommand to the .set 
for i in range(50):
    lb.insert(END, "Line " + str(i)) 
lb.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=lb.yview) # Set the command option of the scroll bar to 
root.mainloop()

