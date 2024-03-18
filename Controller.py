global tab_grille
tab_grille= []
LEN_JEU = 12

def genererGrille():
    for i in range(LEN_JEU):
        tab_grille.append([])
        for j in range(LEN_JEU):
            tab_grille[i].append(0)

    return tab_grille

def majGrille(L, listeindice):
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(listeindice)):
                    if(i == listeindice[k][0] and j == listeindice[k][1]):
                        i1 = listeindice[k][0]
                        i2 = listeindice[k][1]
                        L[i1][i2] = 1
    return L

def collision(liste_indice, L):

    for i in range(len(liste_indice)):
        if(L[liste_indice[i][0]][liste_indice[i][1]] == 1):
            return True
        else:
            return False
           
    
def genererIndiceduPion(x_depart, y_depart, len_x, len_y):
    l_indice_pion = []
    for x_depart in range(len_x):
        for y_depart in range(len_y):
            l_indice_pion.append([x_depart,y_depart])
    return l_indice_pion







     



