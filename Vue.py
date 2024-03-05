from Controller import *
from tkinter import *



old=[None, None]
global c 
c= 0

def créerGrille(root):
    c = Canvas(root, width = 1000, height= 650)
    for i in range(13):
        c.create_line(12,12+50*i,612,12+50*i)
        c.create_line(12+50*i,12,12+50*i,612)
    c.pack() 
    
    générerPion(c,2,1)
    
   



   
   


def générerPion(cnv_pion, tailleX, tailleY):
     
             
     a = cnv_pion.create_rectangle(1000,20,950,72,fill='red', outline = '')
     
     cnv_pion.bind("<Button-1>", lambda event:cliquePion(event, cnv=cnv_pion, recta=a))
     
     
     


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
    x1, y1, x2, y2 = can.coords(rect)
    for i in range(12):
        for j in range(12):
            if (12+i*50 <= x<= 12+(i+1)*50 and 12+j*50 <= y <= 12+(j+1)*50):
                can.move(rect,12+i*50-x1,12+j*50-y1)
                move = True 
               
                
    
    
                
    if (move == False):
        can.move(rect,620-x1,30-y1)
        can.unbind("<Motion>")
        






       


    
    
   
    
    
   

