from tkinter import *
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert( value)
    def inOrderTraversal(self):
        self.root.inOrder(center)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
               self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    def inOrder(self, center, i=0):
        if self.left != None:
            self.left.inOrder([center[0]-degree[i], center[1]+50], i+1)
            canvas.create_line(center[0]+15, center[1]+30, center[0]-degree[i]+15, center[1]+50)
        
        # print(self.value)
        print('im ', self.value, 'my x,y:', center[0], center[1])
        canvas.create_rectangle(center[0], center[1], center[0]+30, center[1]+30, fill='white', outline='black')
        canvas.create_text(center[0]+15, center[1]+15, fill="darkblue",font="Times 20", text=str(self.value))
        
        if self.right != None:
            self.right.inOrder([center[0]+degree[i], center[1]+50], i+1)
            canvas.create_line(center[0]+15, center[1]+30, center[0]+degree[i]+15, center[1]+50)

center = [600, 10]
degree = [300, 75, 37.5, 18.75, 9.375, 4.687, 2.343] 
root = Tk()
canvas = Canvas(root, width=1200+400, heigh=800)
canvas.pack()
t = Tree()
for i in [4, 2, 6, 1, 3, 5, 7]:
    t.insert(i)
t.inOrderTraversal()
root.mainloop()
