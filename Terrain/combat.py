from math import *
import random
from Deplacement import *
pdvjoueur1=3
pdvjoueur2=3
element1="lumiere"
element2="lumiere"
multiplicateur=1000
val = 0
grille1=[]
grille2=[]
grille3=[]
grille4=[]
listeVar= []
joueur = 1

def grilleBaseJ1(n):
    global grille1
    global grille2
    for x in range(n):
        for y in range(n):
            val = int(random.randint(1,4))
            grille2+=[val,]
        grille1+=[grille2,]
        grille2=[]   
    return grille1

def grilleBaseJ2(n):
    global grille3
    global grille4
    for x in range(n):
        for y in range(n):
            val = int(random.randint(1,4))
            grille4+=[val,]
        grille3+=[grille4,]
        grille4=[]
    return grille3

def affiche(grille):
    for x in range(len(grille)):
        for y in range(len(grille)):
            print(str(grille[x][y])," ",end="")
        print()


def joueurs():
    global joueur
    if joueur == 1:
        joueur = 2      
    elif joueur == 2:
        joueur = 1

def selection(grille1):
    global listeVar
    global joueur
    global element1
    global element2
    global multiplicateur
    global pdvjoueur1
    global pdvjoueur2
    x=0
    select= ""
    if pdvjoueur1>0 and pdvjoueur2>0:
        while joueur==1:
            print("\n Tour du joueur 1")
            while len(listeVar)<=35 and select != ("q" or "Q"):
                if len(listeVar) > 2:
                    affiche(grille1)
                    select = input("Entrez q pour quitter et c pour continuer")
                    if select == "q":
                        for x in range(len(grille1)):
                            for y in range(len(grille1)):
                                if grille1[x][y] == 0:
                                    grille1[x][y] = random.randint(1,4)
                        print("Grille joueur1")
                        affiche(grille1)
                        print("Grille joueur2")
                        affiche(grille3)
                        AttributionElement(joueurs,selection)
                        Multiplicateur(joueurs,selection,AttributionElement)
                        print("L'element du joueur 1 est:",element1)
                        print("L'element du joueur 2 est:",element2)
                        print("Le multiplicateur de degat:",multiplicateur)
                        degat(selection,joueur,AttributionElement,Multiplicateur)
                        print("Les pv du joueur 1:",pdvjoueur1)
                        print("Les pv du joueur 2:",pdvjoueur2)
                        listeVar.clear()
                        select = ""
                        joueurs()
                        return selection(grille1)
                        
                if len(listeVar)==0:
                    x = int(input("Selectionnez coordonné horizontal à supprimer: "))
                    y = int(input("Selectionnez coordonné vertical à supprimer: "))
                    z =  grille1[x][y]
                    listeVar += [z,]
                    grille1[x][y] = 0 
                affiche(grille1)
                print(listeVar)
                if len(listeVar)<=36:
                    a = int(input("Selectionnez coordonné horizontal à supprimer: "))
                    b = int(input("Selectionnez coordonné vertical à supprimer: "))
                    c =  grille1[a][b]
                    if c==z:
                        if a==x or (a-1)==x or (a+1)==x:
                            if b==y or (b-1)==y or (b+1)==y:
                                if a==x and b==y:
                                    print("Vous ne pouvez pas selectionner la même case")
                                else:
                                    x=a
                                    y=b
                                    z =  grille1[x][y]
                                    listeVar += [z,]
                                    grille1[x][y] = 0
                                    print(listeVar)
                            else:
                                print("Ordonné trop éloigné")
                        else:
                            print("Abscisse trop éloigné")
                    else:
                        print("La case selectionnée n'est pas = a la premiere")
            affiche(grille1)
        while joueur==2:
            print("\n Tour du joueur 2")
            while len(listeVar)<=35 and select != ("q" or "Q"):
                if len(listeVar) > 2:
                    affiche(grille3)
                    select = input("Entrez q pour quitter et c pour continuer")
                    if select == "q":
                        for x in range(len(grille1)):
                            for y in range(len(grille1)):
                                if grille3[x][y] == 0:
                                    grille3[x][y] = random.randint(1,4)
                        print("Grille joueur1")
                        affiche(grille1)
                        print("Grille joueur2")
                        affiche(grille3)
                        AttributionElement(joueurs,selection)
                        Multiplicateur(joueurs,selection,AttributionElement)
                        print("L'element du joueur 1 est:",element1)
                        print("L'element du joueur 2 est:",element2)
                        print("Le multiplicateur de degat:",multiplicateur)
                        degat(selection,joueur,AttributionElement,Multiplicateur)
                        print("Les pv du joueur 1:",pdvjoueur1)
                        print("Les pv du joueur 2:",pdvjoueur2)
                        listeVar.clear()
                        select = ""
                        joueurs()
                        return selection(grille1)
                if len(listeVar)==0:
                    x = int(input("Selectionnez coordonné horizontal à supprimer: "))
                    y = int(input("Selectionnez coordonné vertical à supprimer: "))
                    z =  grille3[x][y]
                    listeVar += [z,]
                    grille3[x][y] = 0 
                affiche(grille3)
                print(listeVar)
                if len(listeVar)<=36:
                    a = int(input("Selectionnez coordonné horizontal à supprimer: "))
                    b = int(input("Selectionnez coordonné vertical à supprimer: "))
                    c =  grille3[a][b]
                    if c==z:
                        if a==x or (a-1)==x or (a+1)==x:
                            if b==y or (b-1)==y or (b+1)==y:
                                if a==x and b==y:
                                    print("Vous ne pouvez pas selectionner la même case")
                                else:
                                    x=a
                                    y=b
                                    z =  grille3[x][y]
                                    listeVar += [z,]
                                    grille3[x][y] = 0
                                    print(listeVar)
                            else:
                                print("Ordonné trop éloigné")
                        else:
                            print("Abscisse trop éloigné")
                    else:
                        print("La case selectionnée n'est pas = a la premiere")
    elif pdvjoueur1<=0:
        print("Victoire du joueur 2")
    elif pdvjoueur2<=0:
        print("Victoire du joueur 1")


def AttributionElement(joueurs,selection):
    global element1
    global element2
    if joueur==1:
        if listeVar[0]==1:
            element1="feu"
        elif listeVar[0]==2:
            element1="eau"
        elif listeVar[0]==3:
            element1="plante"
        elif listeVar[0]==4:
            element1="lumiere"
    elif joueur==2:
        if listeVar[0]==1:
            element2="feu"
        elif listeVar[0]==2:
            element2="eau"
        elif listeVar[0]==3:
            element2="plante"
        elif listeVar[0]==4:
            element2="lumiere"

def Multiplicateur(joueurs,selection,AttributionElement):
    global multiplicateur
    global element1
    global element2
    if joueur==1:
        if element1 == "feu":
            if element2== "plante":
                multiplicateur = 2
            elif element2=="eau":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element1 == "eau":
            if element2== "feu":
                multiplicateur = 2
            elif element2=="plante":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element1 == "plante":
            if element2== "eau":
                multiplicateur = 2
            elif element2=="feu":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element1=="lumiere":
            multiplicateur=1
    elif joueur==2:
        if element2 == "feu":
            if element1== "plante":
                multiplicateur = 2
            elif element1=="eau":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element2 == "eau":
            if element1== "feu":
                multiplicateur = 2
            elif element1=="plante":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element2 == "plante":
            if element1== "eau":
                multiplicateur = 2
            elif element1=="feu":
                multiplicateur = 0.5
            else:
                multiplicateur = 1
        if element2 == "lumiere":
            multiplicateur=1

def degat(selection,joueur,AttributionElement,Multiplicateur):
    global pdvjoueur1
    global pdvjoueur2
    if joueur==1:
        if element1=="eau" or element1=="feu" or element1=="plante":
            if len(listeVar)>=10:
                pdvjoueur2=pdvjoueur2-(20*multiplicateur)
            elif len(listeVar)>=7:
                pdvjoueur2=pdvjoueur2-(10*multiplicateur)            
            elif len(listeVar)>=5:
                pdvjoueur2=pdvjoueur2-(5*multiplicateur)
            elif len(listeVar)>=3:
                pdvjoueur2=pdvjoueur2-(3*multiplicateur)
        elif element1=="lumiere":
            if len(listeVar)>=10:
                pdvjoueur1=pdvjoueur1+20
            elif len(listeVar)>=7: 
                pdvjoueur1=pdvjoueur1+10
            elif len(listeVar)>=5:
                pdvjoueur1=pdvjoueur1+5
            elif len(listeVar)>=3:
                pdvjoueur1=pdvjoueur1+3
    if joueur==2:
        if element2=="eau" or element2=="feu" or element2=="plante":
            if len(listeVar)>=10:
                pdvjoueur1=pdvjoueur1-(20*multiplicateur)
            elif len(listeVar)>=7:
                pdvjoueur1=pdvjoueur1-(10*multiplicateur)            
            elif len(listeVar)>=5:
                pdvjoueur1=pdvjoueur1-(5*multiplicateur)
            elif len(listeVar)>=3:
                pdvjoueur1=pdvjoueur1-(3*multiplicateur)
        elif element2=="lumiere":
            if len(listeVar)>=10:
                pdvjoueur2=pdvjoueur2+20
            elif len(listeVar)>=7: 
                pdvjoueur2=pdvjoueur2+10
            elif len(listeVar)>=5:
                pdvjoueur2=pdvjoueur2+5
            elif len(listeVar)>=3:
                pdvjoueur2=pdvjoueur2+3


def finPartie():
    global pdvjoueur1
    global pdvjoueur2
    if pdvjoueur1 <= 0:
        return 2
    elif pdvjoueur2 <= 0:
        return 1                        
    
def accordement(grilleBaseJ1,grilleBaseJ2):
    print("Grille joueur1")
    affiche(grilleBaseJ1(6))
    print("Grille joueur2")
    affiche(grilleBaseJ2(6))
    print("L'element du joueur 1 est:",element1)
    print("L'element du joueur 2 est:",element2)
    selection(grille1)

def lancement():
    accordement(grilleBaseJ1,grilleBaseJ2)


