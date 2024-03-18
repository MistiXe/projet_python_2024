from Controller import *
from tkinter import *
from Variables import *


old=[None, None]
global c 
c= 0





def creerJeu(root):
    global laliste
    global liste_bouge
    global lagrille_theorique
    liste_bouge = []
    platforme = Canvas(root, width=1200 , height=650)

    for i in range(12):
        x =   400 +30*i 
        for j in range(12):
            y = 160 + 30*j
            carré = platforme.create_rectangle(x,y,x+30,y+30)

    platforme.pack()
    laliste = genererPion(platforme)
    lagrille_theorique = genererGrille()
    
    platforme.bind("<Button-1>", lambda event:cliquePion(event, platforme, laliste))
    
    
def cliquePion(event, cnv, laliste):
    global c
    c = (c+1)%2
    recta  = 0
    for l in laliste:
        for p in l:
            cood_p = cnv.coords(p)
            if(cood_p[0] <= event.x <= cood_p[0] + cood_p[2] and cood_p[1] <= event.y <= cood_p[1] + cood_p[3]):
                recta = p
                
               
    if(recta != 0 and recta not in liste_bouge):  
        if(c == 1):
            old[0] = event.x
            old[1] = event.y
            cnv.bind("<Motion>", lambda event:move(event, cnv, recta))
        else:
            cnv.unbind("<Motion>")
            deposer(event.x,event.y,cnv, recta)
    
        
    
    
def move(event, can, rect):
    
    x1, y1, x2, y2 = can.coords(rect)
    move = False
    can.move(rect, event.x - x1, event.y - y1)

def deposer(x,y,can , rect):
    x1, y1, x2, y2= can.coords(rect)
    move = False
   

    for i in range(12):
        for j in range(12):
            if (400 +30*i  <= x<= 400+(i+1)*30 and 160 +30*j <= y <= 160+(j+1)*30):
                liste_ind = [i,j]
                majGrille(lagrille_theorique, liste_ind)
                
                can.move(rect,400+i*30-x1,160+j*30-y1)
                move = True
                liste_bouge.append(rect)
                print(lagrille_theorique)
 

   
        

    


           

                
                
    
    
   
    
    
    
    
  
        






       


    
    
   
    
    
   

