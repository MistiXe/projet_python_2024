global tab_grille
tab_grille= []
LEN_JEU = 12

from random import *
import time

def genererGrille():
    for i in range(LEN_JEU):
        tab_grille.append([])
        for j in range(LEN_JEU):
            tab_grille[i].append(1)

    return tab_grille


def majGrille(L, matrice):
    matrice_bis = transGrille(matrice)
    
    for i in L:
        for j in range(len(i)):
            for k in matrice_bis:
                for l in range(len(k)):
                    if(k[l] == 0):
                        i[j] = 0    
                       
    return L


           
def transGrille(matrice):
    matrice_double_dimension = []
    mat = []
    for i in range(len(matrice)):
        mat.append(matrice[i])
        if(len(mat) == 12):
            matrice_double_dimension.append(mat)
            mat = []
    return matrice_double_dimension













     



