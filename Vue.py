from Controller import *
from tkinter import *
from tkinter.ttk import *
from Variables import*
from tkinter import messagebox
from pygame import *
from timeit import default_timer

### Décalration des variables

old=[None, None]
global c 
c= 0
liste_couleur_selec = []
global moved
moved = []
global l_root
l_root = []
global score1
global score2
global secondes



secondes = 500
score1 = 0
score2 = 0

mixer.init()




### définition des matrices

matrice_rouge = [1]*144
matrice_rouge[0] = 2
matrice_rouge[132] = 2

matrice_bleu = [1]*144
matrice_bleu[11] = 2
matrice_bleu[143] = 2


### Gestion du clique
def click(event):
    global platforme
    global selected
    global dimensions
    global player
    global origins
    global laliste
    
    player = 0
    
    x,y = event.x , event.y


    ### On sélectionne des coordonnées du canvas
    selecteds = platforme.find_overlapping(x,y,x,y)


    ### On vérifie si ce qu'on sélectionne n'est pas déjà mis dans grille
    if(selecteds[0] not in moved):
     
        if selecteds:
            selected = selecteds[0]
            
            cord = platforme.coords(selected)
            origins = cord
            w = cord[2] - cord[0]
            h = cord[3] - cord[1]
            dimensions = [w, h]
                
            blocs = laliste 
            
            

            if selected in blocs[0]:
                player = 1

            elif selected in blocs[1]:
                player = 2

### Mouvement du pion 

def move(event):
    global selected
    global dimensions


    ### x et y sont les coordonnées du pointeur de la souris
    x,y = event.x , event.y

    ### Selected = le pion, on cherche la coordonnée du pion cliqué et on le bouge
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

### On vérifie si la pièce ne dépasse pas la grille
def depasser(L):
   
   if(L[2] <= 760 and L[3] <= 520):
       return True
   else:
       return False

    

def deposer(event):
    global  selected , grille , platforme , dimensions , player , checked , surface , player , matrice_bleu , matrice_rouge, tourP, mat_pion, score_inter, score1, score2
    x,y = event.x , event.y
    
    score_inter = 0
    
    mat_pion = []

    matrice = []

    ### On vérifie si c'est un tour pair ou impair
    if tourP%2==0 :
        matrice = matrice_rouge
        message = c2
        mat_pion = laliste[0]
        
        

        label_etat.config(text="Turn of the  " + message+"S")

    
    else:
        matrice = matrice_bleu
        message = c1
        mat_pion = laliste[1]
        label_etat.config(text="Turn of the : " + message+"S")
       

    
    
 
    for e in grille:
        
        if x >= e[0] and x<= e[2] and y>=e[1] and y <= e[3]:
            check = verifier(e[0],e[1], player)

            if check and selected in mat_pion  :
               platforme.coords(selected, e[0],e[1],e[0]+ dimensions[0] , e[1] + dimensions[1])
               for i in checked:
                   matrice_rouge[i] = 0
                   matrice_bleu[i] = 0

                   cord_grille = grille[i]
                   
                  ### Cobnditions de coins de chaque pions , on met 2 s'il y a un coin de disponible

                   if (cord_grille[0] == surface[0] or  cord_grille[1] == surface[1] or cord_grille[2] == surface[2] or cord_grille[3] == surface[3]) and depasser(surface) == True :
                        
                      
                            if i > 11 :
                                matrice[i-12] = 0

                            if i < 132 :
                                matrice[i+12] = 0

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
                     
               if player == 1:
                   matrice_rouge = matrice
               elif player == 2:
                   matrice_bleu = matrice 
               selected = None       
                 
                   
                   
                   
                
           
                ### Gestion du score
               score_inter+=len(checked) 
               
               if(matrice == matrice_rouge):
                   score1 = score1 + score_inter
                   label_s1.config(text="Score : " + str(score1)) 
               else:
                   score2 = score2 + score_inter
                   label_s2.config(text="Score : " + str(score2)) 
                         
               if player == 1:
                   matrice_rouge = matrice
               elif player == 2:
                   matrice_bleu = matrice 
               moved.append(selected)
               print(score_inter)
              
               
                        
               tourP = tourP +1
               print(matrice_bleu)
   
               
              

    else :
        platforme.coords(selected,origins)
        selected = None

       
### Rotation d'un pion
def rotate(event):
    global selected , platforme , dimensions
    x,y = event.x , event.y


    if selected:
        temp = dimensions[0]
        dimensions[0]= dimensions[1]
        dimensions[1] = temp
        platforme.coords(selected,  x , y , x+dimensions[0] , y + dimensions[1])


          

### Création du jeu

def creerJeu(root, couleur1, couleur2):
    global platforme
    global laliste
    global liste_bouge
    liste_bouge = []
    global grille
    global label_etat
    global label_s1
    global label_s2
    global laliste_theorique
    global c1
    global c2
    global tourP
    global score1
    global score2
    tourP =  0

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=5)
    
    c1 = couleur1
    c2= couleur2
   
    menubar = Menu(root,relief=FLAT,bd=10)

    

    mixer.music.unload()
    mixer.music.load("MVC/Songs/mario.wav")
    play_song_menu()
    
    
    
    #### Menu barre
    
    menubar.add_command(label='Règles du jeu', command=regles, font = ("Mono","50"))
    menubar.add_command(label='Version', command=version, font = ("Mono","50"))
    menubar.add_command(label='Rejouer', command=lambda: rejouer(root) , font = ("Mono","50"))
    menubar.add_command(label='Quitter le jeu', command=lambda: quitter(root) , font = ("Mono","50"))
    root.config(menu=menubar)
    
 
    message1_s = "Score : " + str(score1)
    message2_s = "Score : " + str(score2)


    label_s1 = Label(root,text =message1_s, font=("Arial",15),background=couleur1,foreground='white'  )
    label_s2 = Label(root,text =message2_s, font=("Arial", 15), background=couleur2,foreground='white' )
    
    label_etat = Label(root,text ="The game begins !", font=("Arial", 10) )
   
 

    platforme = Canvas(root, width=1600 , height=1000, background="GRAY")
   

 
  
    
   

    grille = []
    for i in range(12):
        
        y = 160 + 30*i
        for j in range(12):
            x =   400 +30*j
            carré = platforme.create_rectangle(x,y,x+30,y+30)
            grille.append(platforme.coords(carré))

           
    label_etat.pack(side=TOP, expand=True)
    label_s1.pack(side=LEFT, expand=True)
    label_s2.pack(side=RIGHT, expand=True)

    

    platforme.pack()

    laliste = genererPion(platforme)

    


    mettreCouleurPion(laliste, couleur1,couleur2,platforme)
    

  
    for i in laliste:
        for j in i :
            platforme.tag_bind(j,"<Button-1>", click )
             


    ### Gestion des évenements
   
    platforme.bind("<Button1-Motion>", move)
    platforme.bind("<ButtonRelease-1>" , deposer)
    platforme.bind("<Button-3>" , rotate)
    
    



   
   
    
    

    ############################# Menu #################################################

def setMenu(root):

    mixer.music.load('MVC/Songs/dofus_menu.wav')
    play_song_menu()




    global selected_color
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=5)
    liste_color = ["RED", "BLUE", "YELLOW", "CYAN", "IVORY", "GREEN", "BLACK"]

    d_1= Canvas(root, width=30, height=30, bg="WHITE")
    d_1.grid(column=3, row=0, sticky=W)

    d_2= Canvas(root, width=30, height=30, bg="WHITE")
    d_2.grid(column=3, row=1, sticky=W)

    v= Checkbutton(root, text="Ordinateur")
    v.grid(column=4, row=1, sticky=W)
 
    
    username_label = Label(root, text="Player 1:")
    username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)


    selected_color = StringVar()
    color1_entry = Combobox(root, textvariable=selected_color)
    color1_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)
    color1_entry['values'] = liste_color
    color1_entry['state'] = 'readonly'
    

    
    password_label = Label(root, text="Player 2 :")
    password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

    selected_color_2 = StringVar()
    color2_entry = Combobox(root, textvariable=selected_color_2)
    color2_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)
    color2_entry['values'] = liste_color
    color2_entry['state'] = 'readonly'
    
    # Valider 
    v_button =Button(root, text="Valider")
    v_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    
    

    v_button.bind("<Button-1>", lambda event:boutton_clic(event, root,couleur1= color1_entry.get(), couleur2=color2_entry.get()))
    color1_entry.bind('<<ComboboxSelected>>', lambda event:liste_carre(event, d_1, color1_entry.get()))
    color2_entry.bind('<<ComboboxSelected>>', lambda event:liste_carre(event, d_2, color2_entry.get()))

    root.mainloop()



### Méthode pour valider la saisie de l'utilisateur

def boutton_clic(event, root_m_, couleur1, couleur2):
    
   
   
    if((couleur1 != "" and couleur2 != "" ) and couleur1 != couleur2):
        root =  Tk()
        root.geometry("1210x580")
        creerJeu(root, couleur1, couleur2)
        root.mainloop()
        
       
        


        
        
### Configuartion des pions selon la couleur sélectionné
def liste_carre(event, car, couleur):
    car.configure(bg=couleur)


### Personalisation des pions
def mettreCouleurPion(laliste, couleur1, couleur2, cnv):
    
    for i in range(len(laliste)):
        for j in range(len(laliste[i])):
            if(i == 0):
                cnv.itemconfigure(laliste[i][j], fill=couleur1)
            else:
                cnv.itemconfigure(laliste[i][j], fill=couleur2)
        




### Méthode quitter
def quitter(root):
    root.quit()
  

### Méthode pour afficher les règles du blockus
   
def regles():
    message  = "- 1) Placement des pièces : Chaque joueur choisit une couleur et commence avec 21 pièces, allant de 1 à 5 blocs. Le premier joueur commence en plaçant une pièce dans son coin du plateau, et les joueurs suivants font de même. " + "\n" +  "- 2) Règle de connexion : Après le premier tour, chaque pièce que tu places doit toucher au moins une autre pièce de ta couleur, mais seulement par les coins. Les côtés ne peuvent pas se toucher." + "\n" + "- 3) Blocage : Tu peux et devrais essayer de bloquer tes adversaires en utilisant tes pièces pour les empêcher de développer leur territoire." + "\n" + "- 4) Fin de jeu et score : Le jeu se termine lorsque aucun joueur ne peut plus poser de pièce sur le plateau. Le score est calculé en soustrayant le nombre de carrés dans les pièces non placées de chaque joueur de son total. Un bonus est accordé si toutes les pièces sont placées, surtout si la plus petite pièce (le monomino) est placée en dernier."


    messagebox.showinfo("Règles du jeu", message)

### Méthode pour lire du son
def play_song_menu():
   mixer.music.set_volume(1)
   mixer.music.play(-1)


### Version
def version():
    message  = " Version 1.0"
    messagebox.showinfo("Version du jeu", message)



  
        






       


    
    
   
    
    
   

