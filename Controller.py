from tkinter import *
import os
import time
import sys


def test_fin_jeu():
    global matrice
    fin=False
    cpt=0
    for i in range(len(matrice)):
        if matrice[i]==2 :
            cpt+=1
    if cpt ==0 :
        fin=True
    return fin




def verifier_etat_jeu(platforme, score1, score2):
    if test_fin_jeu()==True:
            platforme.destroy()
            
            if S[0]==S[1]:
                egalite=Label(platforme,text='Fin de la partie \n EGALITE rejouer pour designer qui est le champion' ,bg="gray", fg="white", font=("Georgia", 20))
                egalite.place(x=250,y=250)
            elif score2>score1:
                gagne2=Label(platforme,text="Fin de la partie \n Dommage la machine a gagne essayz de \n se venger en cliquant sur le boutton en dessous" ,bg="white", fg="black", font=("Georgia", 20))
                gagne2.place(x=220,y=250)
            elif score1>score2:
                gagne1=Label(platforme,text="Fin de la partie \n  felicitations vous avez gagne" , bg="black", fg="white", font=("Georgia", 20))
                gagne1.place(x=330,y=250)        
            boutton=Button(platforme,command=rejouer,width=295,height=150)
            boutton.place(x=375,y=400)  #boutton  pour recommancer le jeu il s'affiche qu'a la fin de la partie

### Boutton rejouer, on éteint le processus puis on en recrée un autre
def rejouer(root):
    print("haya")
    root.destroy()
    time.sleep(1)
    os.execl(sys.executable, sys.executable,*sys.argv )












        



