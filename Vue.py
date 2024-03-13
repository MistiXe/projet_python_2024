from Controller import *
from tkinter import *

global liste_a_bouge

global a
liste_a_bouge =[]
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
    genererPionAuto(platforme)
    
    

   
    
    
  
  
   



def genererPionAuto(platforme):
    y = 50
    x= 50
    a = platforme.create_rectangle(50,50,80,80,fill="red") 
    platforme.bind("<Button-1>",lambda event:cliquePion(event, platforme, a))
    
     


def cliquePion(event, cnv, recta):
    global c
    c = (c+1)%2
    if(c == 1):
        old[0] = event.x
        old[1] = event.y
        cnv.bind("<Motion>", lambda event:move(event, can=cnv, rect=recta))
    else:
        cnv.unbind("<Motion>")
        deposer(event.x, event.y, can=cnv, rect=recta)
    
    
def move(event, can, rect):
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
    
   
    
    
    
    
  
        


def deposer(plateforme,a, event):
    x1, y1 = plateforme.coords(a)
   
    move = False
    for i in range(12):
        for j in range(12):
            if (12+i*50 <= event.x <= 12+(i+1)*50 and 12+j*50 <= event.y <= 12+(j+1)*50):
                plateforme.move(a,12+i*50-x1,12+j*50-y1)
                move = True 
                
               
                           
    if (move == False):
        plateforme.move(a,620-x1,30-y1)
        plateforme.unbind("<Motion>")
        






       


    
    
   
    
    
   

