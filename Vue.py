from Controller import *
from tkinter import *



old=[None, None]


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


def generateZoneJ1(root):
    c = Canvas(root, width = 280,height = 610, background='ivory')
    c.place(y=50)
    c.create_text(50,40, font=40,text = "Joueur A", anchor=CENTER, fill='black')
    générerPion(c)
    
   


def generateZoneJ2(root):
    c = Canvas(root, width = 280,height = 610, background='green')
    c.create_text(50,40, font=40,text = "Joueur B", anchor=CENTER, fill='white')  
    c.place(x = 930,y=50)
   
   


def générerPion(cnv_pion):
       
     a = cnv_pion.create_rectangle(25,100,100,175, outline= 'white', width=4, fill='black', tags="pion")
     cnv_pion.tag_bind("pion", "<Button-1>", cliquePion)
     

  
     
    
     
     
    
     
     
     
     

def cliquePion(event):
    old[0] = event.x
    old[1] = event.y
    print(event.x)
    



    