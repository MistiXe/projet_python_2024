from Controller import *
from tkinter import *



old=[None, None]

def créerGrille(root):
    c = Canvas(root, width = 920, height= 720)
    x = 5
    y = 5
    for i in range(12):
        for j in range(12):
            c.create_rectangle(x,y,x+45,y+45, outline='black')
            x=x+45
        y=y+45
        x=5        
    c.pack(anchor=CENTER, expand=False)


    générerPion(c,2,1)
    
   



   
   


def générerPion(cnv_pion, tailleX, tailleY):
   
             
     a = cnv_pion.create_rectangle(815.5,353,860,397, outline= 'black', width=2, fill='red', tags="pion")
     
     cnv_pion.tag_bind("pion", "<Button-1>", cliquePion)
     cnv_pion.tag_bind("pion", "<B1-Motion>", lambda event:move(event, can=cnv_pion, rect=a))


def cliquePion(event):
    old[0] = event.x
    old[1] = event.y
    print(event.x)

def move(event, can, rect):
    can.move(rect, event.x-old[0], event.y-old[1])
    old[0] = event.x
    old[1] = event.y






       


    
    
   
    
    
   

