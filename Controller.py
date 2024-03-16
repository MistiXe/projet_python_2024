global tab_grille
tab_grille= []
LEN_JEU = 12

def genererGrille(LEN):
    for i in range(LEN):
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

def collision(x,y, L):
    if(L[x][y] == 1 or (L[x-1][y] == 1 ) or (L[x+1][y] == 1 ) or (L[x][y+1] == 1 )or (L[x][y-1] == 1) ):
        return True
    else:
        return False
     


L= genererGrille(12)
l_ind = [[0,0], [0,1],[0,2]]
print(majGrille(L, l_ind))