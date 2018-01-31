#Gondet Loic
#L1-Informatique
#================================================================================================================================================================================================================
#===============================================================================Importation des différents modules===============================================================================================
#===============================================================================
from MapFonction import*
from Map import*
from combat import*
#================================================================================================================================================================================================================
#==============================================================================================================================================================================
#===============================================================================
gx=1
gy=0
gm=1
ggrille=[]

gmx1=0
gmy1=0

def terrain():
    global gm
    global ggrille
    Nm = gm
    print(Nm)
    if Nm==0:
        print("veuillez entrez un nombre correcte")
        terrain()
    elif Nm==32:
        print("Chargement de la Map 32")
        g=32
        ggrille = Mode(g)
    #Map de départ du joueurs
    elif Nm==41:
        print("Chargement de la Map 41")
        g=41
        ggrille = Mode(g)
    ################################
    elif Nm==2:
        print("Chargement de la Map 2")
        g=2
        ggrille = Mode(g)
    elif Nm==3:
        print("Chargement de la Map 3")
        g=3
        ggrille = Mode(g)
    elif Nm==4:
        print("Chargement de la Map 4")
        g=4
        ggrille = Mode(g)
    elif Nm==5:
        print("Chargement de la Map 5")
        g=5
        ggrille = Mode(g)
    elif Nm==6:
        print("Chargement de la Map 6")
        g=6
        ggrille = Mode(g)
    else:
        print("Impossible de charger la map, numero incorrect")
    return ggrille
   
    

def position(x,y,m):
    global gx
    gx = x
    global gy
    gy = y
    global gm
    gm = m
    print("test1" ,gx,gy,gm,)
    return gx,gy,gm

def monstre():
    global gmx1
    gmx1 = 6
    global gmy1
    gmy1 = 3
    global ggrille
    ggrille[gmx1][gmy1] = "M"
    return ggrille

def detection():
    global ggrille
    global gmx1
    global gmy1
    x = gmx1
    y = gmy1
    if ggrille[x-1][y] == "P":
        lancement()
        finCombat()
        deplacement()
    elif ggrille[x+1][y] == "P":
        lancement()
        finCombat()
        deplacement()
    elif ggrille[x][y-1] == "P":
        lancement()
        finCombat()
        deplacement()
    elif ggrille[x][y+1] == "P":
        lancement()
        finCombat()
        deplacement()
    else:
        deplacement()

def finCombat():
    global ggrille
    global gmx1
    global gmy1
    fin = finPartie()
    if fin == 1:
        ggrille[gmx1][gmy1] = "0"
        #geneMob()
        return ggrille
    elif fin == 2:
        print ("GameOver")
        quit()

'''def geneMob():
    global ggrille
    x = 0
    y = 0
    while x != 15:
        while y != 15:
            if ggrille[x][y] == "0":
                ggrille == "M"
                if y == 15:
                    x += 1
                else:
                    y += 1
    #return ggrille'''

###################################
###################################
def personnage():
    global gx
    global gy
    global ggrille
    ggrille[gx][gy] = "P"
    return ggrille

def choixDirection():#Récup la position du joueurs dans la fonction "position" et lui permet de ce déplacer dans les case adjacente.
    affiche(ggrille)
    global gx
    x = gx
    global gy
    y = gy
    global gm
    m = gm
    print("test2",gx,gy,gm,)
    direction=""
    while (direction!="h" and direction!="b" and direction!="g" and direction!="d"):
        direction=input("Voulez vous allez: En haut(h),En bas(b),Gauche(g),Droite(d)")
    print(x,y,m,direction,)
    grille=ggrille
    return x,y,m,direction

def deplacement():
    global ggrille
    grille = ggrille
    choix=choixDirection()
    x,y,m,d=choix[0],choix[1],choix[2],choix[3],
    if d=="h":
        grille=haut(grille,x,y,m)
    elif d=="b":
        grille=bas(grille,x,y,m)
    elif d=="g":
        grille=gauche(grille,x,y,m)
    elif d=="d":
        grille=droite(grille,x,y,m)
    ggrille=grille
    detection()
    deplacement()
    return ggrille


def haut(grille,x,y,m):
    global gx
    global gm
    if gx!=0: #x est au bord
        machin = grille[x-1][y]
        if machin != 0:
            print("chemin non praticable")
        else:
            grille[gx][gy]=0
            gx-=1
            grille[gx][gy] = "P"
    elif gx==0:
        print("Changement de map")
        #besoin d'un plan de la position des différentes map
        #plan actuelle 9*9
        gm-=9
        gx=14
        grille=terrain()
        personnage()
    else:
        print("erreur de deplacement")
    print("retourne")
    return grille

def bas(grille,x,y,m):
    global gx
    global gm
    if gx!=15: #x est au bord
        machin = grille[x+1][y]
        if machin != 0:
            print("chemin non praticable")
        else:
            grille[gx][gy]=0
            gx+=1
            grille[gx][gy] = "P"
    elif gx==15:
        print("Changement de map")
        gm+=9
        gx=15
        grille=terrain()
        personnage()
    else:
        print("erreur de deplacement")
    print("retourne")
    return grille
    
def gauche(grille,x,y,m):
    global gy
    global gm
    if gy!=0: #x est au bord
        machin = grille[x][y-1]
        if machin != 0:
            print("chemin non praticable")
        else:
            grille[gx][gy]=0
            gy-=1
            grille[gx][gy] = "P"
    elif gy==0:
        print("Changement de map")
        #besoin d'un plan de la position des différentes map
        #plan actuelle 9*9
        gm-=9
        gy=14
        grille=terrain()
        personnage()
    else:
        print("erreur de deplacement")
    print("retourne")
    return grille

def droite(grille,x,y,m):
    global gy
    global gm
    if gy!=15: #x est au bord
        machin = grille[x][y+1]
        if machin != 0:
            print("chemin non praticable")
        else:
            grille[gx][gy]=0
            gy+=1
            grille[gx][gy] = "P"
    elif gy==15:
        print("Changement de map")
        gm+=9
        gy=15
        grille=terrain()
        personnage()
    else:
        print("erreur de deplacement")
    print("retourne")
    return grille
