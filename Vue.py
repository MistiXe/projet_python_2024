from Controller import *
from tkinter import *
from Variables import*



old=[None, None]
global c 
c= 0

matrice_rouge = [1]*144

matrice_rouge[0] = 2
matrice_rouge[132] = 2

matrice_bleu = [1]*144
matrice_bleu[11] = 2
matrice_bleu[143] = 2



def click(event):
    global platforme
    global selected
    global dimensions
    global player
    global origins
    global laliste
    global couleur_joueur
    player = 0
    
    x,y = event.x , event.y

    selecteds = platforme.find_overlapping(x,y,x,y)
    if selecteds :
        selected = selecteds[0]
        cord = platforme.coords(selected)
        origins = cord
        w = cord[2] - cord[0]
        h = cord[3] - cord[1]
        dimensions = [w, h]
        
        blocs = laliste 
        

        if selected in blocs[0]:
           
           player = 1
           message = "RED"
           
           label_etat.config(text="Autour des : " + message)
        elif selected in blocs[1]:
         
           player = 2
           message = "BLUE"
           label_etat.config(text="Autour des : " + message)



def move(event):
    global selected
    global dimensions

    x,y = event.x , event.y

    if selected:
       platforme.coords(selected,x,y,x+dimensions[0],y+dimensions[1])

def verifier(x,y,player):
    global selected , platforme , dimensions , grille , matrice_bleu , matrice_bleu , matrice_rouge ,  checked , surface
    matrice = []
    if player == 1 :
        matrice = matrice_rouge
    
    elif player == 2:
        matrice = matrice_bleu


    surface = [x,y ,x+dimensions[0] , y + dimensions[1]]
    i =0
    check1 = True
    check2 = False
    checked = []
    while i<len(grille) and check1 == True:
        e = grille[i]
        
     
        if e[0]>= surface[0] and e[2]<= surface[2] and e[1]>=surface[1] and e[3] <= surface[3]:
            checked.append(i)
            if matrice[i] == 0:
                check1 = False

            if matrice[i] == 2:
                check2 = True

    
        i = i+1
        


    return check1 and check2




    

def deposer(event):
    global  selected , grille , platforme , dimensions , player , checked , surface , player , matrice_bleu , matrice_rouge
    x,y = event.x , event.y
    

    matrice = []

    
 
    for e in grille:
        if x >= e[0] and x<= e[2] and y>=e[1] and y <= e[3]:
            check = verifier(e[0],e[1], player)
            if check :
               platforme.coords(selected, e[0],e[1],e[0]+ dimensions[0] , e[1] + dimensions[1])
               for i in checked:
                   matrice_rouge[i] = 0
                   matrice_bleu[i] = 0

                   cord_grille = grille[i]

                   if cord_grille[0] == surface[0] or  cord_grille[1] == surface[1] or cord_grille[2] == surface[2] or cord_grille[3] == surface[3] :
                       if i > 11 :
                           matrice[i-12] = 0

                       if i < 132 :
                           matrice[i+11] = 0

                       if i % 12 != 0  :
                           matrice[i-1] = 0

                       if i% 12 != 11 :
                           matrice[i+1] = 0

                        
                       if cord_grille[0] == surface[0] and   cord_grille[1] == surface[1] and i % 12 != 0  and i > 11:
                           matrice[i-13] = 2

                       if cord_grille[2] == surface[2] and   cord_grille[1] == surface[1] and i % 12 != 11 and i > 11 :
                           matrice[i-11] = 2

                       if cord_grille[0] == surface[0] and   cord_grille[3] == surface[3] and i % 12 != 0  and  i < 132:
                           matrice[i+11] = 2

                       if cord_grille[2] == surface[2] and   cord_grille[3] == surface[3] and i % 12 != 11   and  i < 132:
                           matrice[i+13] = 2

                           
               
                        
               


            else :
                platforme.coords(selected,origins)
                selected = None



def rotate(event):
    global selected , platforme , dimensions
    x,y = event.x , event.y


    if selected:
        temp = dimensions[0]
        dimensions[0]= dimensions[1]
        dimensions[1] = temp
        platforme.coords(selected,  x , y , x+dimensions[0] , y + dimensions[1])


          



def creerJeu(root):
    global platforme
    global laliste
    global liste_bouge
    liste_bouge = []
    global grille
    global label_etat
    label_etat = Label(root,text ="Autour des : ", font=("Arial", 25) )

    platforme = Canvas(root, width=1600 , height=1000)
    grille = []
    for i in range(12):
        
        y = 160 + 30*i
        for j in range(12):
            x =   400 +30*j
            carré = platforme.create_rectangle(x,y,x+30,y+30)
            grille.append(platforme.coords(carré))

           
    label_etat.pack()
    platforme.pack()
    
    laliste = genererPion(platforme)
    

  
    for i in laliste:
        for j in i :
             platforme.tag_bind(j,"<Button-1>", click )

   
    platforme.bind("<Button1-Motion>", move)
    platforme.bind("<ButtonRelease-1>" , deposer)
    platforme.bind("<Button-3>" , rotate) 








  
        






       


    
    
   
    
    
   

