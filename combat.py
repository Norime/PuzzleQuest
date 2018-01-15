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

def selection(grille):
    global listeVar
    x=0
    while len(listeVar)<=2:
        x = int(input("Selectionnez la 1ere case à supprimer: "))
        y = int(input("Selectionnez la 2eme case à supprimer: "))
        print("\n")
        z =  liste[x][y]
        listeVar += [z,]
        liste[x][y] = 0
        liste[x][y] = int(random.randint(1,4))   
    affiche(liste)
    print(listeVar)
