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
                    if(i == listeindice[0] and j == listeindice[1]):
                        i1 = listeindice[0]
                        i2 = listeindice[1]
                        L[i1][i2] = 1
    return L

def collision(x,y, L):
    if(L[x][y] == 1):
        return True
    else:
        return False
     



