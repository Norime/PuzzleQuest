"""
Jeu PuzzleGame
Jeu dans lequel on doit déplacer notre hero dans plusieur map pour qu'il récupère sont poulet.

Script Python
Fichiers :  Game.py,Deplacement.py, Map.py, MapFonction.py, n1, n2 + images
"""
import pygame
from pygame.locals import *
#from Game import*
#from Deplacement import*
#from Map import*
#from MapFonction import*

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((640, 480))
#Icone
icone = pygame.image.load("background.jpg")
pygame.display.set_icon(icone)
fenetre.blit(icone, (0,0))
#Titre
#pygame.display.set_caption(titre_fenetre)#Puzzle quest, je te retrouverai poulet!

#Rafraîchissement de l'écran
pygame.display.flip()


#Limitation de vitesse de la boucle
#30 frames par secondes suffisent
#pygame.time.Clock().tick(30)
fin = 1
GameMenu = 1
Jeu = 0
while fin:
    pygame.time.Clock().tick(30)
    while GameMenu == 1:
        pygame.time.Clock().tick(30)
        from Game import*
    while Jeu == 1:
        pygame.time.Clock().tick(30)
        #import la grille
        if ggrille[x][y]==1:
            print("dessin montagne")
        if ggrille[x][y]==2:
            print("dessin lac")
        if ggrille[x][y]==3:
            print("dessin arbre")
            #import le personnage
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            #perssonage
            persso = pygame.image.load("dk_bas.png").convert_alpha()#_alpha pour garder la transparence
            fenetre.blit(persso, (x,y))
            #
            if event.type == KEYDOWN:
                if  event.key == K_LEFT:
                    x-=1
                if  event.key == K_RIGHT:
                    x+=1
                if  event.key == K_UP:
                    y+=1
                if  event.key == K_DOWN:
                    y-=1
                if event.key == K_ESCAPE:
                    var_1, var_2, var_3, var_4 = "Menu", "Pause", "Quitter", "Autre"
    if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
pygame.quit()
