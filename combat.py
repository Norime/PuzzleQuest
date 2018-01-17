from math import *
import random

'''
    R = 1
    B = 2
    V = 3
    J = 4
'''

val = 0
liste=[]
liste2=[]
listeVar= []
joueur = 1

def grilleBase(n):
    global liste
    global liste2
    for x in range(n):
        for y in range(n):
            val = int(random.randint(1,4))
            liste2+=[val,]
        liste+=[liste2,]
        liste2=[]
    return liste

def grilleAdv(grille):
    return grille

#def affiche(grille, grille2):
def affiche(grille):
#    print("au tour du joueur \n")
    for x in range(len(grille)):
        for y in range(len(grille)):
            print(str(grille[x][y])," ",end="")
        print()

#Grille adversaire       
'''    print("\n \n")
    
    for x in range(len(grille2)):
        for y in range(len(grille2)):
            print(str(grille2[x][y])," ",end="")
        print()
'''
affiche(grilleBase(6))


def joueur():
    global joueur
    if joueur == 1:
        joueur = 2
        print("\n Tour du joueur 2 \n")        
    elif joueur == 2:
        joueur = 1
        print("\n Tour du joueur 1 \n")

def selection(grille):
    global listeVar
    global joueur
    x=0
    select= ""
    print(joueur)
    while len(listeVar)<=35 and select != ("q" or "Q"):
        if len(listeVar) > 2:
            affiche(liste)
            select = input("Entrez q pour quitter et c pour continuer")
            if select == "q":
                for x in range(len(grille)):
                    for y in range(len(grille)):
                        if liste[x][y] == 0:
                            liste[x][y] = random.randint(1,4)
                affiche(liste)
                joueur()
                print(joueur)
                
        if len(listeVar)==0:    
            x = int(input("Selectionnez coordonné horizontal à supprimer: "))
            y = int(input("Selectionnez coordonné vertical à supprimer: "))
            print("\n")
            z =  liste[x][y]
            listeVar += [z,]
            liste[x][y] = 0
            ##liste[x][y] = int(random.randint(1,4))  
        affiche(liste)
        print(listeVar)
        if len(listeVar)<=36:
            a = int(input("Selectionnez coordonné horizontal à supprimer: "))
            b = int(input("Selectionnez coordonné vertical à supprimer: "))
            print("\n")
            c =  liste[a][b]
            if c==z:
                if a==x or (a-1)==x or (a+1)==x:
                    if b==y or (b-1)==y or (b+1)==y:
                        if a==x and b==y:
                            print("vous ne pouvez pas selectionné la même case")
                        else:
                            x=a
                            y=b
                            z =  liste[x][y]
                            listeVar += [z,]
                            liste[x][y] = 0
                            ##liste[x][y] = int(random.randint(1,4))  
                            #affiche(liste)
                            print(listeVar)
                    else:
                        print("Ordonné trop éloigné")
                else:
                    print("Abscisse trop éloigné")
            else:
                print("la case selectionné n'est pas = a la premiere")
    affiche(liste)



    
selection(liste)
