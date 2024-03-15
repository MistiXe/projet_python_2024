from Controller import *
from tkinter import *
from Variables import *

global liste_a_bouge

global laliste
old=[None, None]
global c 
c= 0



def créerGrille(root):
    platforme = Canvas(root, width=1200 , height=650)

    for i in range(12):
        x =   400 +30*i 
        for j in range(12):
            y = 160 + 30*j
            carré = platforme.create_rectangle(x,y,x+30,y+30)

    platforme.pack()
    laliste = genererPion(platforme)
    
    for i in range(len(laliste)):
        for j in range(len(laliste)):
            platforme.bind("<Button-1>", lambda event:cliquePion(event, platforme, laliste[i][j]))
    
    
def cliquePion(event, cnv, recta):
    global c
    c = (c+1)%2
    if(c == 1):
        old[0] = event.x
        old[1] = event.y
        cnv.bind("<Motion>", lambda event:move(event, cnv, recta))
    else:
        cnv.unbind("<Motion>")
        
    
    
def move(event, can, rect):
   
    old[0] = event.x
    old[1] = event.y
    x1, y1 , x2, y2 = can.coords(rect)
    move = False
    if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
        can.move(rect, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y

def deposer(x, y , can , rect):
    x1, y1= can.coords(rect)
    for i in range(12):
        for j in range(12):
            if (12+i*50 <= x<= 12+(i+1)*50 and 12+j*50 <= y <= 12+(j+1)*50):
                can.move(rect,12+i*50-x1,12+j*50-y1)
                move = True 
               
                
    
    
                
    if (move == False):
        can.move(rect,620-x1,30-y1)
        can.unbind("<Motion>")
    
   
    
    
    
    
  
        






       


    
    
   
    
    
   

