import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert() #use .convert for optimisation
fenetre.blit(fond, (0,0))

#perssonage
x=200
y=300
persso = pygame.image.load("perso.png").convert_alpha()#_alpha pour garder la transparence
fenetre.blit(persso, (x,y))
#Rafraîchissement de l'écran
pygame.display.flip()


#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == KEYDOWN:
            if  event.key == K_SPACE:
                print("Espace")
            if  event.key == K_LEFT:
                x-=1
                print("Gauche")
            if  event.key == K_RIGHT:
                x+=1
                print("Droite")
            if  event.key == K_UP:
                y+=1
                print("Haut")
            if  event.key == K_DOWN:
                y-=1
                print("bas")
        fenetre.blit(persso,(x,y))
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
pygame.quit()
