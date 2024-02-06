from Controller import *
from tkinter import *

def créerGrille(root):
    c = Canvas(root, width = 620, height= 620)
    x = 5
    y = 5
    for i in range(12):
        for j in range(12):
            c.create_rectangle(x,y,x+45,y+45, outline='black')
            x=x+45
        y=y+45
        x=5        
    c.pack(anchor=CENTER, expand=False)



    