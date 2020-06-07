## Importation de pygame

import pygame
from pygame.locals import *
from fonctions import *
from constantes import *
import time as t
from random import *
# import numpy as np

# initialisation de tous les modules
# ---------------------------
pygame.init()  


# creation d'une fenetre vide
# ---------------------------
fenetre = pygame.display.set_mode((1200, 900))    
# largeur 700, longueur 1200, et redimensionnable

fond = pygame.image.load("background.jpg").convert()

# convert_alpha() permet de coller l'image en conservant la transparence
# recupere les coordonnees du point en haut a gauche de l'image rectangulaire
# elles sont par defaut (0,0)
# Chargement du personnage



# perso = pygame.Surface((taille_image,taille_image))
perso = pygame.image.load("heros.png").convert_alpha()
position_perso = perso.get_rect()


## Boucle infinie

continuer = 1

# reglages lecture clavier
pygame.key.set_repeat(30, 30)

tir = 0
continuer = 1

son_menu = pygame.mixer.Sound("son_menu.wav")
son_monde1 = pygame.mixer.Sound("son_monde1.wav")
son_bug = pygame.mixer.Sound("son_bug.wav")
son_monde2 = pygame.mixer.Sound("son_monde2.wav")
son_monde3 = pygame.mixer.Sound("son_monde3.wav")
son_lave = pygame.mixer.Sound("son boss.wav")

accueil = pygame.image.load("accueil.jpg")
bouton_jouer = pygame.image.load("bouton_jouer.png").convert_alpha()
bouton_niveau = pygame.image.load("bouton_niveau.png").convert_alpha()
bouton_jouer_selec = pygame.image.load("bouton_jouer_selec.png").convert_alpha()
bouton_niveau_selec = pygame.image.load("bouton_niveau_selec.png").convert_alpha()

bouton_monde1 = pygame.image.load("bouton_monde1.png").convert_alpha()
bouton_monde1_selec = pygame.image.load("bouton_monde1_selec.png").convert_alpha()
bouton_monde2 = pygame.image.load("bouton_monde2.png").convert_alpha()
bouton_monde2_selec = pygame.image.load("bouton_monde2_selec.png").convert_alpha()
bouton_monde3 = pygame.image.load("bouton_monde3.png").convert_alpha()
bouton_monde3_selec = pygame.image.load("bouton_monde3_selec.png").convert_alpha()
bouton_monde4 = pygame.image.load("bouton_monde4.png").convert_alpha()
bouton_monde4_selec = pygame.image.load("bouton_monde4_selec.png").convert_alpha()

fond_monde4 = pygame.image.load("background_monde4.jpg").convert_alpha()

ennemi = pygame.image.load("chevalier.png").convert_alpha()
position_ennemi = perso.get_rect()


fenetre.blit(accueil, (0,0))
fenetre.blit(bouton_jouer, (500, 300))
fenetre.blit(bouton_niveau, (500, 500))

#Rafraichissement
pygame.display.flip()


while continuer:    
    
    continuer_accueil = 1
    fenetre.blit(accueil, (0,0))
    #Rafraichissement
    pygame.display.flip()

    son_menu.play()
    
    #BOUCLE D'ACCUEIL

    while continuer_accueil:
        #Limitation de vitesse de la boucle
        #Chargement et affichage de l'écran d'accueil
        
        
        
        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables 
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT:
                continuer_accueil = 0
                continuer = 0
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
            elif event.type == MOUSEMOTION  and event.pos[0] > 500 and event.pos[1] > 500 and event.pos[0] < 800 and event.pos[1] < 600 :
                fenetre.blit(bouton_niveau_selec, (500,500))
                pygame.display.flip()
            elif event.type == MOUSEBUTTONDOWN  and event.pos[0] > 500 and event.pos[1] > 500 and event.pos[0] < 800 and event.pos[1] < 600 : # MENU DES NIVEAUX
                continuer_niveau = 1
                continuer_accueil = 0
                
            # NIVEAU 1
                
            elif event.type == MOUSEMOTION and event.pos[0] > 500 and event.pos[1] > 300 and event.pos[0] < 800 and event.pos[1] < 400 :
                fenetre.blit(bouton_jouer_selec, (500,300))
                pygame.display.flip()
            elif event.type == MOUSEBUTTONDOWN and event.pos[0] > 500 and event.pos[1] > 300 and event.pos[0] < 800 and event.pos[1] < 400 :
                continuer_jeu1 = 1
                continuer_accueil = 0
                perso = pygame.image.load("heros.png").convert_alpha()
                position_perso = perso.get_rect()
                
                A = [[1,1,1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,2,2,2,2,0,0,0,0,0,1],
      [1,0,1,1,1,1,1,1,1,1,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1,1,1]]

                cases = nombre_cases_1(A)
                pygame.display.flip()
                i, j = 1, 1 # Position du héros
                n = len(A)
                coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                comptage = 1
                # Chargement du dialogue
                dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                fenetre.blit(dialogue, (0,700))

            else:
                fenetre.blit(bouton_jouer, (500, 300)) 
                fenetre.blit(bouton_niveau, (500, 500))
                pygame.display.flip()
                    
    while continuer_niveau :
        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables 
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT:
                continuer_niveau = 0
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_niveau = 0
            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 500 and event.pos[1] > 250 and event.pos[0] < 800 and event.pos[1] < 350):  # MONDE 1
                    continuer_jeu1 = 1
                    continuer_niveau = 0
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,2,2,2,2,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1]]
    
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    initialisation_monde1(A, fenetre)
                    comptage = 1
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                if (event.pos[0] > 500 and event.pos[1] > 400 and event.pos[0] < 800 and event.pos[1] < 500):  # MONDE 2
                    continuer_jeu6 = 1
                    continuer_niveau = 0
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,4,0,0,0,3,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,5,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]
                
                    i_ennemi, j_ennemi= 4, 1 #Position de l'ennemi (à tête chercheuse)
                    i_ennemi2, j_ennemi2=5,1
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    cle = 0
                    
                    comptage = 10
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                if (event.pos[0] > 500 and event.pos[1] > 550 and event.pos[0] < 800 and event.pos[1] < 650):   # MONDE 3
                    continuer_jeu3_1 = 1
                    continuer_niveau = 0
                    
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,1,1,2,2,2,1],
                        [1,0,1,0,1,0,1,1,1,1,2,1],
                        [1,0,1,0,1,0,1,1,1,1,2,1],
                        [1,0,1,0,1,0,1,1,1,1,1,1],
                        [1,0,1,4,1,0,1,1,1,1,1,1],
                        [1,1,1,1,1,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,0,1],
                        [1,2,1,1,1,1,0,0,0,0,0,1],
                        [1,2,1,1,1,1,0,1,1,1,1,1],
                        [1,2,2,2,1,1,0,0,0,0,5,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    n = len(A)
                    fenetre.blit(fond, (0,0))
                    initialisation_monde3(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 5, 1 # Position du héros
                    tir = 0
                    shield = 0
                    cle = 0
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
                    fenetre.blit(perso, position_perso)
                    
                    comptage = 16
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                    pygame.display.flip()
            
                if (event.pos[0] > 500 and event.pos[1] > 700 and event.pos[0] < 800 and event.pos[1] < 800):    # MONDE 4
                    continuer_jeu16 = 1
                    continuer_niveau = 0
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
                    
                    n = len(A)
                    coord_initiale = [0, taille*(14-n)/2]
                    fenetre.blit(fond_monde4, (0,0))
                    initialisation_monde4(A, fenetre, coord_initiale)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 6, 1 # Position du héros

                    comptage = 20
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                    
            elif event.type == MOUSEMOTION  and event.pos[0] > 500 and event.pos[1] > 250 and event.pos[0] < 800 and event.pos[1] < 350 :
                fenetre.blit(bouton_monde1_selec, (500,250))
                pygame.display.flip()
            elif event.type == MOUSEMOTION  and event.pos[0] > 500 and event.pos[1] > 400 and event.pos[0] < 800 and event.pos[1] < 500 :
                fenetre.blit(bouton_monde2_selec, (500,400))
                pygame.display.flip()
            elif event.type == MOUSEMOTION  and event.pos[0] > 500 and event.pos[1] > 550 and event.pos[0] < 800 and event.pos[1] < 650 :
                fenetre.blit(bouton_monde3_selec, (500,550))
                pygame.display.flip()
            elif event.type == MOUSEMOTION  and event.pos[0] > 500 and event.pos[1] > 700 and event.pos[0] < 800 and event.pos[1] < 800 :
                fenetre.blit(bouton_monde4_selec, (500,700))
                pygame.display.flip()
                
                
            else:
                fenetre.blit(accueil, (0,0))
                fenetre.blit(bouton_monde1, (500,250))
                fenetre.blit(bouton_monde2, (500,400))
                fenetre.blit(bouton_monde3, (500,550))
                fenetre.blit(bouton_monde4, (500,700))
                pygame.display.flip()
        
        
    son_menu.stop()
    # BOUCLE DE JEU
    son_monde1.play()

    # # NIVEAU TEST1

   #   while continuer_jeu_test1 :
    #     # Demarrage de la boucle
    #     for event in pygame.event.get() :
    #         # gestion des evenements
    #         if event.type == QUIT :
    #         # quitter la fenetre
    #             continuer_jeu_test1 = 0
    #             continuer_accueil = 1
    #         if event.type == KEYDOWN :
    #             # appui sur une touche du clavier
    #             if event.key == K_DOWN:
    #                 ir, jr = i, j
    #                 i += deplacement_bh(i,j,1, A)
    #             if event.key == K_UP:
    #                 ir, jr = i, j
    #                 i += deplacement_bh(i,j,-1, A)
    #             if event.key == K_RIGHT:
    #                 ir, jr = i, j
    #                 j += deplacement_dg(i,j,1, A)
    #             if event.key == K_LEFT:
    #                 ir, jr = i, j
    #                 j += deplacement_dg(i,j,-1, A)
    #             ie, je = pattern_tete_chercheuse(A, ir, jr, ie, je)[0], pattern_tete_chercheuse(A, ir, jr, ie, je)[1]
    #             im, jm = pattern_magicien(A, ir, jr, im, jm, ib, jb)[0], pattern_magicien(A, ir, jr, im, jm, ib, jb)[1]
    #             t =  pattern_magicien(A, ir, jr, im, jm, ib, jb)[4]
    #             c = 0
    #             if t != 0:
    #                 tir = t
    #                 c = 1
    #             else:
    #                 c = 0
    #             if tir !=0 and c == 1:
    #                 ib, jb = pattern_magicien(A, ir, jr, im, jm, ib, jb)[2], pattern_magicien(A, ir, jr, im, jm, ib, jb)[3] 
    #             if tir != 0 and c == 0:
    #                 ib, jb = pattern_bouledefeu(A, ib, jb, tir)
    #             if i == ib and j == jb :
    #                 continuer_jeu = 0
    #                 continuer_accueil = 1
    #             if tir != 0 and c == 0:
    #                 ib, jb = pattern_bouledefeu(A, ib, jb, tir)    
    #             i_ennemi, j_ennemi = pattern(i_ennemi, j_ennemi, A)                
    #             if(A[i][j] == 3):
    #                 A[i][j] = 2
    #                 A = transpose(A)
    #                 i_ennemi, j_ennemi= j_ennemi, i_ennemi
    #                 ie, je = je, ie
    #                 ib, jb= jb, ib
    #                 im, jm = jm, im
    #             
    #             # Changement du terrain
    #             
    #             initialisation(A, fenetre)
    #             cases = nombre_cases_1(A)

   #       position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
    #     fenetre.blit(perso, position_perso)
    # 
    # 
    #     position_ennemi = (coord_initiale[0] + j_ennemi*taille, coord_initiale[1] + i_ennemi*taille)
    #     fenetre.blit(ennemi, position_ennemi)
    #     position_tete_chercheuse = (coord_initiale[0] + je*taille, coord_initiale[1] + ie*taille)
    #     fenetre.blit(tete_chercheuse, position_tete_chercheuse)
    #     position_magicien = (coord_initiale[0] + jm*taille, coord_initiale[1] + im*taille)
    #     fenetre.blit(magicien, position_magicien)
    #     position_boule = (coord_initiale[0] + jb*taille, coord_initiale[1] + ib*taille)
    #     fenetre.blit(boule, position_boule)
    #     
    #     if i == i_ennemi and j == j_ennemi :
    #         continuer_jeu_test1 = 0
    #         continuer_accueil = 1
    #         
    #     if i == ie and j == je :
    #         continuer_jeu_test1 = 0
    #         continuer_accueil = 1
    #         
    #     if i == im and j == jm :
    #         continuer_jeu_test1 = 0
    #         continuer_accueil = 1
    #         
    #     if i == ib and j == jb :
    #         continuer_jeu_test1 = 0
    #         continuer_accueil = 1
    #                         
    #     if(cases == 0):
    #         continuer_jeu_test1 = 0
    #         continuer_accueil = 1
    # 
    #     # rafraichissement de l'image
    #     pygame.display.flip()
   
#     # NIVEAU 1
   
    while continuer_jeu1 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu1 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu1 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A[i][j] = 2
                    A = transpose(A)
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
                
                
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        
        if cases == 0:  # Initialisation du level 2
            continuer_jeu2 = 1
            continuer_jeu1 = 0
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,1,1,1,1,2,1,1,1,0,1],
    [1,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1],
    [1,3,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

            initialisation_monde1(A, fenetre)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 1, 1 # Position du héros
            n = len(A)
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            fenetre.blit(fond, (0,0))
            initialisation_monde1(A, fenetre)
            comptage = 2
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
        
            
        
        # rafraichissement de l'image
        pygame.display.flip()
   
    # NIVEAU 2
   
    while continuer_jeu2 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu2 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu2 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
                
                
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)

        # rafraichissement de l'image
        pygame.display.flip()
        
        if cases == 0:  # Initialisation du level 3
            continuer_jeu2 = 0
            continuer_jeu3 = 1
            
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                [1,5,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,0,1,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,3,1],
                [1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,0,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,3,0,0,0,0,0,0,0,0,4,1],
                [1,1,1,1,1,1,1,1,1,1,1,1]]
            
            initialisation_monde1(A, fenetre)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 1, 1 # Position du héros
            n = len(A)
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            fenetre.blit(fond, (0,0))
            initialisation_monde1(A, fenetre)
            comptage = 3
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            
            cle = 0 #  item pour finir le niveau
            
    # NIVEAU 3
   
    while continuer_jeu3 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                if(A[i][j] == 5) and cle == 1:  # Passage au niveau 4
                    continuer_jeu3 = 0
                    continuer_jeu4 = 1
                    
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,2,2,2,2,2,1,0,0,0,4,1],
                        [1,2,2,2,2,2,1,6,0,0,0,1],
                        [1,2,2,2,7,2,1,0,0,0,0,1],
                        [1,2,2,2,2,2,1,0,0,0,0,1],
                        [1,2,2,2,2,1,1,0,0,0,0,1],
                        [1,2,2,2,2,1,1,1,1,1,1,1],
                        [1,2,2,2,2,1,0,7,0,0,0,1],
                        [1,2,2,2,2,1,0,0,0,0,0,1],
                        [1,2,2,2,2,1,0,0,0,0,0,1],
                        [1,5,2,2,6,1,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    
                    i_ennemi, j_ennemi= 8, 7 #Position de l'ennemi (basique)
                    
                    
                    initialisation_monde1(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    comptage = 4
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    cle = 0
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)

        # rafraichissement de l'image
        pygame.display.flip()
    
    # NIVEAU 4
    
    while continuer_jeu4 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu4 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu4 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                    i_ennemi, j_ennemi= j_ennemi, i_ennemi
                if(A[i][j] == 6):
                    A = symetrie_horizontale(A)
                    i_ennemi, j_ennemi= i_ennemi, n-1-j_ennemi
                if(A[i][j] == 7):
                    A = symetrie_verticale(A)
                    i_ennemi, j_ennemi= n-1-i_ennemi, j_ennemi
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu4 = 0
                    continuer_jeu5 = 1
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,-1,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    
                    i_ennemi, j_ennemi= 8, 7 #Position de l'ennemi (basique)
                    
                    
                    initialisation_monde1(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    comptage = 5
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
                
                i_ennemi, j_ennemi = pattern(i_ennemi, j_ennemi, A)                

        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        
        position_ennemi = (coord_initiale[0] + j_ennemi*taille, coord_initiale[1] + i_ennemi*taille)
        fenetre.blit(ennemi, position_ennemi)
        
        if i == i_ennemi and j == j_ennemi :
            continuer_jeu4 = 0
            continuer_accueil = 1

        # rafraichissement de l'image
        pygame.display.flip()

    # NIVEAU 5
    
    while continuer_jeu5 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu5 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu5 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == (-1)):
                    continuer_jeu5 = 0
                    continuer_jeu5_fin = 1
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    
                    i_ennemi, j_ennemi= 8, 7 #Position de l'ennemi (basique)
                    
                    
                    initialisation_monde1(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    comptage = 6
                    # Chargement du dialogue
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))

                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
             

        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)



        # rafraichissement de l'image
        pygame.display.flip()
    
    son_monde1.stop()
    son_bug.play()


    while continuer_jeu5_fin :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu5_fin = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu5_fin = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                if int(comptage) == 10:
                    continuer_jeu5_fin = 0
                    continuer_jeu6 = 1
                
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,4,0,0,0,3,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,5,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]
                
                    i_ennemi, j_ennemi = 4, 1 #Position de l'ennemi (à tête chercheuse)
                    i_ennemi2, j_ennemi2 = 5, 1 
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    cle = 0
                    
                    comptage = 10
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                comptage += 0.05
                
                if int(comptage) == 7:
                    dialogue = pygame.image.load(str(int(comptage)) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                if int(comptage) == 8:
                    dialogue = pygame.image.load(str(int(comptage)) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (200,50))
                if int(comptage) == 9:
                    dialogue = pygame.image.load(str(int(comptage)) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (500,500))
            
        # rafraichissement de l'image
        pygame.display.flip()

    son_bug.stop()
    son_monde2.play()
    
# MONDE 2
# NIVEAU 6

    while continuer_jeu6 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu6 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu6 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A[i][j] = 2
                    A = transpose(A)
                    i_ennemi, j_ennemi,i_ennemi2, j_ennemi2 = j_ennemi, i_ennemi,j_ennemi2, i_ennemi2
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                
                
                
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu6 = 0
                    continuer_jeu7 = 1
                
                
        
        
        
        
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,3,1,3,2,2,2,2,2,1],
                    [1,1,1,1,1,1,1,1,2,2,2,1],
                    [1,0,0,0,0,3,1,1,5,2,2,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,4,0,0,0,0,0,3,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,0,0,0,0,0,3,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,3,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]

                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    
                    cle = 0
                    
                    comptage = 11
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde2(A, fenetre)
                cases = nombre_cases_1(A)
                   
                i_ennemi, j_ennemi = pattern(i_ennemi, j_ennemi,A)
                i_ennemi2, j_ennemi2 = pattern(i_ennemi2, j_ennemi2,A)
                
        
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)  
        
        position_ennemi = (coord_initiale[0] + j_ennemi*taille, coord_initiale[1] + i_ennemi*taille)
        fenetre.blit(ennemi, position_ennemi)
        
        position_ennemi2 = (coord_initiale[0] + j_ennemi2*taille, coord_initiale[1] + i_ennemi2*taille)
        fenetre.blit(ennemi, position_ennemi2)
        
        if i == i_ennemi and j == j_ennemi :
            continuer_jeu6 = 0
            continuer_accueil = 1
  
        if i == i_ennemi2 and j == j_ennemi2 :
            continuer_jeu6 = 0
            continuer_accueil = 1
        
        # rafraichissement de l'image
        pygame.display.flip()
    
# NIVEAU 7

    while continuer_jeu7 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu7 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu7 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                        
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu7 = 0
                    continuer_jeu8 = 1
                
                
        
        
        
        
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,1,0,0,0,0,0,1],
                    [1,0,1,1,0,0,0,1,0,1,0,1],
                    [1,0,0,0,1,1,1,0,0,1,0,1],
                    [1,1,0,1,1,0,0,0,1,0,0,1],
                    [1,0,0,1,0,5,1,1,0,0,0,1],
                    [1,0,1,0,0,1,0,0,0,0,1,1],
                    [1,1,0,0,1,0,0,1,1,0,1,1],
                    [1,0,0,1,0,0,1,0,0,0,0,1],
                    [1,1,0,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,4,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]

                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    
                    cle = 0
                    
                    comptage = 12
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde2(A, fenetre)
                cases = nombre_cases_1(A)   
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)  
        
        
        # rafraichissement de l'image
        pygame.display.flip()    
        
# NIVEAU 8

    while continuer_jeu8 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu8 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu8 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu8 = 0
                    continuer_jeu9 = 1
                
                
        
        
        
        
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,2,7,1,6,2,2,2,1,2,7,1],
                    [1,6,2,1,2,2,2,6,1,2,6,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,7,2,1,7,1,1,3,2,2,2,1],
                    [1,2,2,1,5,1,1,2,2,7,2,1],
                    [1,2,2,1,2,1,1,1,1,2,1,1],
                    [1,2,7,1,2,1,2,2,2,2,7,1],
                    [1,1,1,1,1,1,2,2,1,1,1,1],
                    [1,2,2,2,6,1,2,2,1,6,2,1],
                    [1,6,2,2,2,1,6,2,1,4,2,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]

                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    
                    cle = 0
                    
                    comptage = 13
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde2(A, fenetre)
                cases = nombre_cases_1(A)   
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)  
        
        
        # rafraichissement de l'image
        pygame.display.flip()    
        
# NIVEAU 9

    while continuer_jeu9 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu9 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu9 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                if(A[i][j] == 7):
                    A = symetrie_horizontale(A)
                if(A[i][j] == 6):
                    A = symetrie_verticale(A)
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu9 = 0
                    continuer_jeu10 = 1
                
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,2,6,2,2,6,3,3,7,2,2,1],
                    [1,7,2,2,7,2,7,2,3,2,2,1],
                    [1,2,2,7,2,7,2,6,2,7,7,1],
                    [1,3,6,2,6,2,7,3,7,2,3,1],
                    [1,7,3,7,2,7,2,7,2,2,2,1],
                    [1,2,6,3,7,3,6,4,6,3,7,1],
                    [1,2,2,6,2,6,3,7,3,6,3,1],
                    [1,6,2,7,7,3,6,2,2,7,2,1],
                    [1,2,7,2,3,6,2,6,7,2,2,1],
                    [1,3,2,6,2,2,7,2,3,2,5,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]

                    initialisation_monde2(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    n = len(A)
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    fenetre.blit(fond, (0,0))
                    initialisation_monde2(A, fenetre)
                    
                    
                    cle = 0
                    
                    comptage = 14
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde2(A, fenetre)
                cases = nombre_cases_1(A)   
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)  
        
        
        # rafraichissement de l'image
        pygame.display.flip() 
    
# NIVEAU 10

    while continuer_jeu10 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu10 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu10 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                if(A[i][j] == 7):
                    A = symetrie_horizontale(A)
                if(A[i][j] == 6):
                    A = symetrie_verticale(A)
                if(A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                
                if(A[i][j] == 5) and cle == 1:
                    continuer_jeu10 = 0
                    continuer_jeu3_1 = 1
                    
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,1,1,2,2,2,1],
                        [1,0,1,0,1,0,1,1,1,1,2,1],
                        [1,0,1,0,1,0,1,1,1,1,2,1],
                        [1,0,1,0,1,0,1,1,1,1,1,1],
                        [1,0,1,4,1,0,1,1,1,1,1,1],
                        [1,1,1,1,1,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,0,1],
                        [1,2,1,1,1,1,0,0,0,0,0,1],
                        [1,2,1,1,1,1,0,1,1,1,1,1],
                        [1,2,2,2,1,1,0,0,0,0,5,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    n = len(A)
                    fenetre.blit(fond, (0,0))
                    initialisation_monde3(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 5, 1 # Position du héros
                    tir = 0
                    shield = 0
                    cle = 0
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
                    fenetre.blit(perso, position_perso)
                    pygame.display.flip()
                    
                    comptage = 15
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde2(A, fenetre)
                cases = nombre_cases_1(A)   
            
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)  
        
        
        # rafraichissement de l'image
        pygame.display.flip() 
        
    son_monde2.stop()
    # MONDE 3
    
    # NIVEAU 11
    
    son_monde3.play()
    
    while continuer_jeu3_1 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3_1 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3_1 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if (A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                initialisation_monde3(A, fenetre)
                cases = nombre_cases_1(A)
                
                position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)                         
                fenetre.blit(perso, position_perso)        
        
                if A[i][j] == 5 and cle == 1:
                    continuer_jeu3_1= 0
                    continuer_jeu3_2 = 1
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    
                    ennemi1 = pygame.image.load("chevalier.png").convert_alpha()
                    position_ennemi1 = perso.get_rect()
                    ennemi2 = pygame.image.load("chevalier.png").convert_alpha()
                    position_ennemi2 = perso.get_rect()
                    tete_chercheuse = pygame.image.load("squelette 50.png").convert_alpha()
                    position_tete_chercheuse = perso.get_rect()
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,3,0,0,1,0,1,1,0,0,1],
                        [1,0,0,0,1,1,0,1,1,1,0,1],
                        [1,0,0,1,1,1,0,1,1,0,0,1],
                        [1,1,1,1,0,0,0,0,0,0,0,1],
                        [1,1,4,0,0,0,0,0,1,1,0,1],
                        [1,1,1,1,0,0,0,0,1,1,3,1],
                        [1,1,0,1,1,1,1,1,1,0,0,1],
                        [1,5,0,0,1,1,1,0,0,0,1,1],
                        [1,1,0,0,0,0,0,0,1,1,1,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1]]
                    n = len(A)
                    initialisation_monde3(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 7, 6 # Position du héros
                    i_ennemi1, j_ennemi1 = 4, 6 #Position de l'ennemi (basique)
                    i_ennemi2, j_ennemi2 = 5, 8 #Position de l'ennemi (basique)
                    ie, je = 6, 3 #Position de l'ennemi (tête chercheuse)
                    tir = 0
                    shield = 0
                    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
                    cle = 0      
                                  
                    comptage = 16
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
                    
                # rafraichissement de l'image
                pygame.display.flip()
        
    # NIVEAU 12
            
    while continuer_jeu3_2 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3_2 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3_2 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                    
                deplacement_t = pattern_tete_chercheuse(A, ir, jr, ie, je)
                ie, je = deplacement_t[0], deplacement_t[1]
                deplacement_ennemi1 = pattern(i_ennemi1, j_ennemi1, A)
                i_ennemi1, j_ennemi1 = deplacement_ennemi1[0], deplacement_ennemi1[1]
                deplacement_ennemi2 = pattern(i_ennemi2, j_ennemi2, A)
                i_ennemi2, j_ennemi2 = deplacement_ennemi2[0], deplacement_ennemi2[1]
                
                if (A[i][j] == 4):
                    cle = 1
                    A[i][j] = 2
                    
                if(A[i][j] == 3):
                    A[i][j] = 0
                    A = transpose(A)
                    i_ennemi1, j_ennemi1= j_ennemi1, i_ennemi1
                    i_ennemi2, j_ennemi2= j_ennemi2, i_ennemi2
                    ie, je = je, ie

                initialisation_monde3(A, fenetre)
                cases = nombre_cases_1(A)
                
            

        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)                         
        fenetre.blit(perso, position_perso)
    
    
        position_ennemi1 = (coord_initiale[0] +j_ennemi1*taille,coord_initiale[1] +  i_ennemi1*taille)
        fenetre.blit(ennemi1, position_ennemi1)
        position_ennemi2 = (coord_initiale[0] +j_ennemi2*taille, coord_initiale[1] + i_ennemi2*taille)
        fenetre.blit(ennemi2, position_ennemi2)
        position_tete_chercheuse = (coord_initiale[0] +je*taille,coord_initiale[1] +  ie*taille)
        fenetre.blit(tete_chercheuse, position_tete_chercheuse)
        
        if i == i_ennemi1 and j == j_ennemi1 and shield == 0:
            continuer_jeu3_2= 0
            continuer_accueil = 1
        if i == i_ennemi1 and j == j_ennemi1 and shield == 1:
            shield = 0
            
        if i == i_ennemi2 and j == j_ennemi2 and shield == 0:
            continuer_jeu3_2= 0
            continuer_accueil = 1
        if i == i_ennemi2 and j == j_ennemi2 and shield == 1:
            shield = 0
            
        if i == ie and j == je and shield == 0:
            continuer_jeu3_2= 0
            continuer_accueil = 1
        if i == ie and j == je and shield == 1:
            shield = 0
   
        if (A[i][j] == 5 and cle == 1):
            continuer_jeu3_3 = 1
            continuer_jeu3_2 = 0
            
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            
            ennemi1 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi1 = perso.get_rect()
            ennemi2 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi2 = perso.get_rect()
            ennemi3 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi3 = perso.get_rect()
            tete_chercheuse = pygame.image.load("squelette 50.png").convert_alpha()
            position_tete_chercheuse = perso.get_rect()
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,0,0,0,1,1,0,1],
                [1,0,1,0,0,0,0,0,0,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,1,1,0,0,0,0,1],
                [1,0,0,0,0,1,1,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,0,0,0,0,0,0,1,0,1],
                [1,0,1,1,0,0,0,0,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1]]
            n = len(A)
            initialisation_monde3(A, fenetre)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 7, 7 # Position du héros
            i_ennemi1, j_ennemi1 = 8, 3 #Position de l'ennemi (basique)
            i_ennemi2, j_ennemi2 = 8, 8 #Position de l'ennemi (basique)
            i_ennemi3, j_ennemi3 = 3, 8 #Position de l'ennemi (basique)
            ie, je = 1, 1 #Position de l'ennemi (tête chercheuse)
            tir = 0
            shield = 0
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]   
                             
            comptage = 17
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
    
    
        # rafraichissement de l'image
        pygame.display.flip()
    
    # NIVEAU 13
    
    while continuer_jeu3_3 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3_3 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3_3 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if ((A[i][j] == 8)):
                    A[i][j] = 0
                    shield += 1
                    
                deplacement_t = pattern_tete_chercheuse(A, ir, jr, ie, je)
                ie, je = deplacement_t[0], deplacement_t[1]
                deplacement_ennemi1 = pattern(i_ennemi1, j_ennemi1, A)
                i_ennemi1, j_ennemi1 = deplacement_ennemi1[0], deplacement_ennemi1[1]
                deplacement_ennemi2 = pattern(i_ennemi2, j_ennemi2, A)
                i_ennemi2, j_ennemi2 = deplacement_ennemi2[0], deplacement_ennemi2[1]
                deplacement_ennemi3 = pattern(i_ennemi3, j_ennemi3, A)
                i_ennemi3, j_ennemi3 = deplacement_ennemi3[0], deplacement_ennemi3[1]
                
                initialisation_monde3(A, fenetre)
                cases = nombre_cases_1(A)
                
                
            

        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
    
    
        position_ennemi1 = (coord_initiale[0] +j_ennemi1*taille, coord_initiale[1] +i_ennemi1*taille)
        fenetre.blit(ennemi1, position_ennemi1)
        position_ennemi2 = (coord_initiale[0] +j_ennemi2*taille,coord_initiale[1] + i_ennemi2*taille)
        fenetre.blit(ennemi2, position_ennemi2)
        position_ennemi3 = (coord_initiale[0] +j_ennemi3*taille, coord_initiale[1] + i_ennemi3*taille)
        fenetre.blit(ennemi3, position_ennemi3)
        position_tete_chercheuse = (coord_initiale[0] +je*taille, coord_initiale[1] + ie*taille)
        fenetre.blit(tete_chercheuse, position_tete_chercheuse)
        
        if i == i_ennemi1 and j == j_ennemi1 and shield == 0:
            continuer_jeu3_3= 0
            continuer_accueil = 1
        if i == i_ennemi1 and j == j_ennemi1 and shield == 1:
            shield = 0
            
        if i == i_ennemi2 and j == j_ennemi2 and shield == 0:
            continuer_jeu3_3= 0
            continuer_accueil = 1
        if i == i_ennemi2 and j == j_ennemi2 and shield == 1:
            shield = 0
            
        if i == i_ennemi3 and j == j_ennemi3 and shield == 0:
            continuer_jeu3_3= 0
            continuer_accueil = 1
        if i == i_ennemi3 and j == j_ennemi3 and shield == 1:
            shield = 0
            
        if i == ie and j == je and shield == 0:
            continuer_jeu3_3= 0
            continuer_accueil = 1
        if i == ie and j == je and shield == 1:
            shield = 0
   
        if(cases == 0):
            continuer_jeu3_4 = 1
            continuer_jeu3_3 = 0
            
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            
            ennemi1 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi1 = perso.get_rect()
            ennemi2 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi2 = perso.get_rect()
            ennemi3 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi3 = perso.get_rect()
            magicien = pygame.image.load("magicien 50.png").convert_alpha()
            position_magicien = perso.get_rect()
            boule= pygame.image.load("boule de feu 50.png").convert_alpha()
            position_boule = perso.get_rect()
            shield_image = pygame.image.load("shield (50 x 50).png")
            position_shield_image = perso.get_rect()
            mur_couvrant = pygame.image.load("mur rocher.jpg").convert_alpha()
            position_mur = perso.get_rect()
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,1,8,1,0,0,0,1],
                [1,0,1,1,0,0,0,0,0,1,0,1],
                [1,0,1,0,0,0,0,0,0,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,0,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,1,0,1,0,0,7,1],
                [1,6,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,0,1,0,0,0,0,1],
                [1,0,1,0,0,0,0,0,0,1,1,1],
                [1,0,0,0,0,1,8,1,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1]]
            n = len(A)
            initialisation_monde3(A, fenetre)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 8, 10 # Position du héros
            i_ennemi1, j_ennemi1 = 3, 1 #Position de l'ennemi (basique)
            i_ennemi2, j_ennemi2 = 4, 6 #Position de l'ennemi (basique)
            i_ennemi3, j_ennemi3 = 8, 1 #Position de l'ennemi (basique)
            ib, jb = 0, 0 #Position de l'ennemi (boule de feu lancée par le magicien)
            im, jm = 10, 10 #Position de l'ennemi (magicien)
            tir = 0
            shield = 0
            
            comptage = 18
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (500,500))
            
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            
            position_perso = (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille)
            fenetre.blit(perso, position_perso)
        
        
            position_ennemi1 = (coord_initiale[0] +j_ennemi1*taille, coord_initiale[1] + i_ennemi1*taille)
            fenetre.blit(ennemi1, position_ennemi1)
            position_ennemi2 = (coord_initiale[0] +j_ennemi2*taille, coord_initiale[1] + i_ennemi2*taille)
            fenetre.blit(ennemi2, position_ennemi2)
            position_ennemi3 = (coord_initiale[0] +j_ennemi3*taille, coord_initiale[1] + i_ennemi3*taille)
            fenetre.blit(ennemi3, position_ennemi3)
            position_magicien = (coord_initiale[0] +jm*taille, coord_initiale[1] + im*taille)
            fenetre.blit(magicien, position_magicien)
            position_boule = (coord_initiale[0] +jb*taille, coord_initiale[1] +ib*taille)
            fenetre.blit(boule, position_boule)
            position_mur = position_boule
            fenetre.blit(mur_couvrant, position_mur)
            
            comptage = 18
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            
            # rafraichissement de l'image
            pygame.display.flip()

        # rafraichissement de l'image
        pygame.display.flip()
    
    # NIVEAU 14

    while continuer_jeu3_4 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3_4 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3_4 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if ((A[i][j] == 8)):
                    A[i][j] = 0
                    shield += 1
                    
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                
                if i == ib and j == jb and shield != 0:
                    shield += -1
                    
                deplacement_m = pattern_magicien(A, ir, jr, im, jm, ib, jb)
                im, jm = deplacement_m[0], deplacement_m[1]
                test_tir =  deplacement_m[4]
                
                if test_tir != 0:
                    tir = test_tir
                    ib, jb = deplacement_m[2], deplacement_m[3]
                if test_tir == 0 and tir != 0:
                    deplacement_b = pattern_bouledefeu(A, ib, jb, tir)
                    ib, jb, = deplacement_b[0], deplacement_b[1]
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == ib and j == jb and shield != 0:
                    shield += -1
                if test_tir == 0 and tir != 0:
                    deplacement_b = pattern_bouledefeu(A, ib, jb, tir)
                    ib, jb, = deplacement_b[0], deplacement_b[1]
                    
                deplacement_ennemi1 = pattern(i_ennemi1, j_ennemi1, A)
                i_ennemi1, j_ennemi1 = deplacement_ennemi1[0], deplacement_ennemi1[1]
                deplacement_ennemi2 = pattern(i_ennemi2, j_ennemi2, A)
                i_ennemi2, j_ennemi2 = deplacement_ennemi2[0], deplacement_ennemi2[1]
                deplacement_ennemi3 = pattern(i_ennemi3, j_ennemi3, A)
                i_ennemi3, j_ennemi3 = deplacement_ennemi3[0], deplacement_ennemi3[1]
                
                initialisation_monde3(A, fenetre)
                cases = nombre_cases_1(A)
                
                
                if(A[i][j] == 6):
                    A[i][j] = 0
                    A = symetrie_horizontale(A)
                    j_ennemi1= 11 - j_ennemi1
                    j_ennemi2= 11 - j_ennemi2
                    j_ennemi3= 11 - j_ennemi3
                    jm = 11 - jm
                    
                if(A[i][j] == 7):
                    A[i][j] = 0
                    A = symetrie_verticale(A)
                    i_ennemi1= 11 - i_ennemi1
                    i_ennemi2= 11 - i_ennemi2
                    i_ennemi3= 11 - i_ennemi3
                    im = 11 - im
                
                print(shield)

                position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
                if shield != 0:
                    fenetre.blit(shield_image, position_perso)
                fenetre.blit(perso, position_perso)
            
            
                position_ennemi1 = (coord_initiale[0] +j_ennemi1*taille, coord_initiale[1] +i_ennemi1*taille)
                fenetre.blit(ennemi1, position_ennemi1)
                position_ennemi2 = (coord_initiale[0] +j_ennemi2*taille, coord_initiale[1] +i_ennemi2*taille)
                fenetre.blit(ennemi2, position_ennemi2)
                position_ennemi3 = (coord_initiale[0] +j_ennemi3*taille, coord_initiale[1] +i_ennemi3*taille)
                fenetre.blit(ennemi3, position_ennemi3)
                position_magicien = (coord_initiale[0] +jm*taille,coord_initiale[1] + im*taille)
                fenetre.blit(magicien, position_magicien)
                position_boule = (coord_initiale[0] +jb*taille, coord_initiale[1] +ib*taille)
                fenetre.blit(boule, position_boule)
                
                if ib == 0 and jb == 0:
                    position_mur = (jb*taille, ib*taille)
                    fenetre.blit(mur_couvrant, position_mur)
                
                if i == i_ennemi1 and j == j_ennemi1 and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == i_ennemi1 and j == j_ennemi1 and shield != 0:
                    shield  += -1
                
                if i == i_ennemi2 and j == j_ennemi2 and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == i_ennemi2 and j == j_ennemi2 and shield != 0:
                    shield  += -1
                
                if i == i_ennemi3 and j == j_ennemi3 and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == i_ennemi3 and j == j_ennemi3 and shield != 0:
                    shield  += -1
                    
                if i == im and j == jm and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == im and j == jm and shield != 0:
                    shield += -1    
                    
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_4= 0
                    continuer_accueil = 1
                if i == ib and j == jb and shield != 0:
                    shield += -1
                                    
                if(cases == 0):
                    continuer_jeu3_4= 0
                    continuer_jeu3_5 = 1
                    
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    
                    ennemi = pygame.image.load("chevalier.png").convert_alpha()
                    position_ennemi = perso.get_rect()
                    tete_chercheuse = pygame.image.load("squelette 50.png").convert_alpha()
                    position_tete_chercheuse = perso.get_rect()
                    magicien = pygame.image.load("magicien 50.png").convert_alpha()
                    position_magicien = perso.get_rect()
                    boule= pygame.image.load("boule de feu 50.png").convert_alpha()
                    position_boule = perso.get_rect()
                    shield_image = pygame.image.load("shield (50 x 50).png")
                    position_shield_image = perso.get_rect()
                    mur_couvrant = pygame.image.load("mur rocher.jpg").convert_alpha()
                    position_mur = perso.get_rect()
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                        [1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
                        [1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1],
                        [1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1],
                        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                        [1,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
                        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1],
                        [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1],#10
                        [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
                        [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
                    initialisation_monde3_bis(A, fenetre)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 1, 1 # Position du héros
                    i_ennemi, j_ennemi = 8, 7 #Position de l'ennemi (basique)
                    ie, je = 12, 22 #Position de l'ennemi (tête chercheuse)
                    ib, jb = 0, 0 #Position de l'ennemi (boule de feu lancée par le magicien)
                    im, jm = 2, 11 #Position de l'ennemi (magicien)
                    tir = 0
                    
                    shield = 0
                    position_perso = (j*taille, i*taille)
                    fenetre.blit(perso, position_perso)
                    
                
                    position_ennemi = (j_ennemi*taille, i_ennemi*taille)
                    fenetre.blit(ennemi, position_ennemi)
                    position_tete_chercheuse = (je*taille, ie*taille)
                    fenetre.blit(tete_chercheuse, position_tete_chercheuse)
                    position_magicien = (jm*taille, im*taille)
                    fenetre.blit(magicien, position_magicien)
                    position_boule = (jb*taille, ib*taille)
                    fenetre.blit(boule, position_boule)
                    position_mur = position_boule
                    fenetre.blit(mur_couvrant, position_mur)
                    pygame.display.flip()
                    
                    comptage = 19
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
            
                # rafraichissement de l'image
                pygame.display.flip()
    
   
    # NIVEAU 15

    while continuer_jeu3_5 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu3_5 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu3_5 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if ((A[i][j] == 8)):
                    A[i][j] = 0
                    shield += 1
                    
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                
                if i == ib and j == jb and shield != 0:
                    shield += -1
                    
                deplacement_t = pattern_tete_chercheuse(A, ir, jr, ie, je)
                ie, je = deplacement_t[0], deplacement_t[1]
                deplacement_m = pattern_magicien(A, ir, jr, im, jm, ib, jb)
                im, jm = deplacement_m[0], deplacement_m[1]
                test_tir =  deplacement_m[4]
                
                if test_tir != 0:
                    tir = test_tir
                    ib, jb = deplacement_m[2], deplacement_m[3]
                if test_tir == 0 and tir != 0:
                    deplacement_b = pattern_bouledefeu(A, ib, jb, tir)
                    ib, jb, = deplacement_b[0], deplacement_b[1]
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                if i == ib and j == jb and shield != 0:
                    shield += -1
                if test_tir == 0 and tir != 0:
                    deplacement_b = pattern_bouledefeu(A, ib, jb, tir)
                    ib, jb, = deplacement_b[0], deplacement_b[1]
                deplacement_ennemi = pattern(i_ennemi, j_ennemi, A)
                i_ennemi, j_ennemi = deplacement_ennemi[0], deplacement_ennemi[1]
                
                initialisation_monde3_bis(A, fenetre)
                cases = nombre_cases_1(A)
                
                
                if(A[i][j] == 3):
                    A[i][j] = 0
                    A = transpose(A)
                    i_ennemi, j_ennemi= j_ennemi, i_ennemi
                    ie, je = je, ie
                    ib, jb= jb, ib
                    im, jm = jm, im
                    
                position_perso = (j*taille,i*taille)
                if shield != 0:
                    fenetre.blit(shield_image, position_perso)
                fenetre.blit(perso, position_perso)
            
            
                position_ennemi = (j_ennemi*taille, i_ennemi*taille)
                fenetre.blit(ennemi, position_ennemi)
                position_tete_chercheuse = (je*taille,ie*taille)
                fenetre.blit(tete_chercheuse, position_tete_chercheuse)
                position_magicien = (jm*taille, im*taille)
                fenetre.blit(magicien, position_magicien)
                position_boule = (jb*taille,ib*taille)
                fenetre.blit(boule, position_boule)
                
                if ib == 0 and jb == 0:
                    position_mur = (jb*taille, ib*taille)
                    fenetre.blit(mur_couvrant, position_mur)
                    
                print(shield)
                if i == i_ennemi and j == j_ennemi and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                if i == i_ennemi and j == j_ennemi and shield != 0:
                    shield  += -1
                    
                if i == ie and j == je and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                if i == ie and j == je and shield != 0:
                    shield += -1
                    
                if i == im and j == jm and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                if i == im and j == jm and shield != 0:
                    shield += -1    
                    
                if i == ib and j == jb and shield == 0:
                    continuer_jeu3_5= 0
                    continuer_accueil = 1
                if i == ib and j == jb and shield != 0:
                    shield += -1
                                    
                if(cases == 0):
                    continuer_jeu3_5= 0
                    continuer_jeu16 = 1
                    perso = pygame.image.load("heros.png").convert_alpha()
                    position_perso = perso.get_rect()
                    A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
                    
                    n = len(A)
                    coord_initiale = [0, taille*(14-n)/2]
                    fenetre.blit(fond_monde4, (0,0))
                    initialisation_monde4(A, fenetre, coord_initiale)
                    cases = nombre_cases_1(A)
                    pygame.display.flip()
                    i, j = 6, 1 # Position du héros
                    
                    comptage = 20
                    dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
                    fenetre.blit(dialogue, (0,700))
            
                # rafraichissement de l'image
                pygame.display.flip()
    
    son_monde3.stop()
    
    
    # MONDE 4
    
    a = t.time()
    # NIVEAU 16
    
    son_lave.play()
    
    while continuer_jeu16:
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu16 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu16 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)
                if(A[i][j] == 5):
                    continuer_jeu16 = 0
       
       
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        
        if(t.time() - a > 0.5):
            a = t.time()
            initialisation_monde4(A, fenetre, coord_initiale)
        
        # rafraichissement de l'image
        pygame.display.flip()

        if cases == 0:  # Initialisation du level 17
            continuer_jeu16 = 0
            continuer_jeu17 = 1
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,5,5,5,5,1],
            [1,0,1,1,1,1,0,5,5,9,5,1],
            [1,0,1,1,1,1,0,5,5,1,5,1],
            [1,0,1,1,1,1,0,0,5,1,5,1],
            [1,0,1,1,1,1,2,0,0,1,5,1],
            [1,0,1,1,1,1,2,1,0,0,0,1],
            [1,0,1,1,1,1,2,1,1,1,0,1],
            [1,0,0,0,0,0,2,0,0,0,0,1],
            [1,0,3,0,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,8,1],
            [1,1,1,1,1,1,1,1,1,1,1,1]]
            
            n = len(A)
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            fenetre.blit(fond_monde4, (0,0))
            initialisation_monde4(A, fenetre, coord_initiale)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 1, 1 # Position du héros

            comptage = 21
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            
    
    # NIVEAU 17
    
    a = t.time()

    while continuer_jeu17:
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu17 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu17 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                if(A[i][j] == 5):
                    continuer_jeu17 = 0
                if(A[i][j] == 3):
                    A = transpose(A)
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)
                
        if(t.time() - a > 0.5):
            a = t.time()
            initialisation_monde4(A, fenetre, coord_initiale)
   
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        
        # rafraichissement de l'image
        pygame.display.flip()
            
        if A[i][j] == 8:  # Initialisation du level 17
            continuer_jeu17 = 0
            continuer_jeu18 = 1
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,1],
            [1,1,1,1,1,1,1,1,1,1,2,1],
            [1,2,2,2,2,2,2,2,2,1,2,1],
            [1,2,1,1,1,1,1,1,2,1,2,1],
            [1,2,1,2,2,2,2,1,2,1,2,1],
            [1,2,1,2,1,1,8,1,2,1,2,1],
            [1,2,1,2,1,1,1,1,2,1,2,1],
            [1,2,1,2,2,2,2,2,2,1,2,1],
            [1,2,1,1,1,1,1,1,1,1,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,1],
            [1,1,1,1,1,1,1,1,1,1,1,1]]
            
            n = len(A)
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            fenetre.blit(fond_monde4, (0,0))
            initialisation_monde4(A, fenetre, coord_initiale)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 1, 1 # Position du héros
            comptage = 22
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            compteur = 0
    
    # NIVEAU 18

    a = t.time()

    while continuer_jeu18:
        pygame.time.Clock().tick(40)
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu18 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu18 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                if(A[i][j] == 3):
                    A = transpose(A)
                
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)

        if(A[i][j] == 5):
            continuer_jeu18 = 0
        if t.time() - a > 1 and compteur == 0 :
            a = t.time()
            remplissage(A, 1, 1, n-2, "ligne",10)
            compteur = 1
        if t.time() - a > 0.9 and compteur == 1:
            a = t.time()
            remplissage(A, 1, 1, n-2, "ligne",5)
            remplissage(A, n-2, 1, n-2, "colonne", 10)
            compteur = 2
        if t.time() - a > 0.8 and compteur == 2:
            a = t.time()
            remplissage(A, n-2, 1, n-2, "colonne", 5)
            remplissage(A, n-2, 1, n-2, "ligne",10)
            compteur = 3
        if t.time() - a > 0.7 and compteur == 3:
            a = t.time()
            remplissage(A, n-2, 1, n-2, "ligne",5)
            remplissage(A, 1, 3, n-2, "colonne", 10)
            compteur = 4
        if t.time() - a > 0.6 and compteur == 4:
            a = t.time()
            remplissage(A, 1, 3, n-2, "colonne", 5)
            remplissage(A, 3, 1, n-4, "ligne",10)
            compteur = 5
        if t.time() - a > 0.5 and compteur == 5:
            a = t.time()
            remplissage(A, 3, 1, n-4, "ligne",5)
            remplissage(A, n-4, 3, n-4, "colonne", 10)
            compteur = 6
        if t.time() - a > 0.4 and compteur == 6:
            a = t.time()
            remplissage(A, n-4, 3, n-4, "colonne", 5)
            remplissage(A, n-4, 3, n-4, "ligne",10)
            compteur = 7
        if t.time() - a > 0.3 and compteur == 7:
            a = t.time()
            remplissage(A, n-4, 3, n-4, "ligne",5)
            remplissage(A, 3, 5, n-5, "colonne", 10)
            compteur = 8
        if t.time() - a > 0.2 and compteur == 8:
            a = t.time()
            remplissage(A, 3, 5, n-5, "colonne", 5)
            remplissage(A, 5, 3, n-6, "ligne",10)
            compteur = 9
        if t.time() - a > 0.2 and compteur == 9: 
            remplissage(A, 5, 3, n-6, "ligne",5)
        
        
        if(A[i][j] == 5):
            continuer_jeu18 = 0
        initialisation_monde4(A, fenetre, coord_initiale)
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        
        # rafraichissement de l'image
        pygame.display.flip()
            
        if A[i][j] == 8:  # Initialisation du level 19
            continuer_jeu18 = 0
            continuer_jeu19 = 1
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            ennemi = pygame.image.load("ennemi_face.png").convert_alpha()
            
            A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            
            n = len(A)
            coord_initiale = [0, taille*(14-n)/2]
            fenetre.blit(fond_monde4, (0,0))
            initialisation_monde4(A, fenetre, coord_initiale)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 6, 1 # Position du héros
            ib, jb = len(A)//2 , len(A[0])-2

            comptage = 23
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            
            compteur = 0
    
    a = t.time()
    
    while continuer_jeu19:
        pygame.time.Clock().tick(40)
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu19 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu19 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                    ib += deplacement_bh(ib,jb,1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                    ib += deplacement_bh(ib,jb,-1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                    jb += deplacement_dg(ib,jb,1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                    jb += deplacement_dg(ib,jb,-1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                if(A[i][j] == 3):
                    A = transpose(A)
                
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)
        if(A[i][j] == 5):
            continuer_jeu19 = 0
        
        if (t.time() - a > 1) and compteur == 0 :
            a = t.time()
            comptage = 24
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            compteur = 1
        if (t.time() - a > 0.5) and compteur == 1:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 14, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 2
        if (t.time() - a > 1) and compteur == 2:
            a = t.time()
            remplissage(A, il, 1, 14, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            il2 = i
            jl2 = j
            remplissage(A, il2, 1, 14, "ligne",10)
            remplissage(A, jl2, 1, 10, "colonne",10)
            compteur = 3
        if (t.time() - a > 1) and compteur == 3:
            a = t.time()
            remplissage(A, il2, 1, 14, "ligne",5)
            remplissage(A, jl2, 1, 10, "colonne",5)
            compteur = 4
        if (t.time() - a > 2) and compteur == 4:
            a = t.time()
            remplissage(A, il, 1, 14, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            remplissage(A, il2, 1, 14, "ligne",2)
            remplissage(A, jl2, 1, 10, "colonne",2)
            compteur = 5
            comptage = 25
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
        if (t.time() - a > 2) and compteur == 5:
            a = t.time()
            r = randint(2,9)
            for il in range(1,r):
                remplissage(A, il, 1, 14, "ligne",10)
            for il in range(r+1,11):
                remplissage(A, il, 1, 14, "ligne",10)
            compteur = 6
        if (t.time() - a > 1.5) and compteur == 6:
            a = t.time()
            for il in range(1,r):
                remplissage(A, il, 1, 14, "ligne",5)
            for il in range(r+1,11):
                remplissage(A, il, 1, 14, "ligne",5)
            compteur = 7
        if (t.time() - a > 1.5) and compteur == 7:
            a = t.time()
            for il in range(1,r):
                remplissage(A, il, 1, 14, "ligne",2)
            for il in range(r+1,11):
                remplissage(A, il, 1, 14, "ligne",2)
            compteur = 8
            comptage = 26
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
        if (t.time() - a > 1) and compteur == 8:
            a = t.time()
            r = randint(2,13)
            for jl in range(1,r):
                remplissage(A, jl, 1, 10, "colonne",10)
            for jl in range(r+1,15):
                remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 9
        if (t.time() - a > 1.5) and compteur == 9:
            a = t.time()
            for jl in range(1,r):
                remplissage(A, jl, 1, 10, "colonne",5)
            for jl in range(r+1,15):
                remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 10
        if (t.time() - a > 1) and compteur == 10:
            a = t.time()
            for jl in range(1,r):
                remplissage(A, jl, 1, 10, "colonne",2)
            for jl in range(r+1,15):
                remplissage(A, jl, 1, 10, "colonne",2)
            compteur = 11
            
        if (t.time() - a > 1) and compteur == 11:
            
            continuer_jeu19 = 0
            continuer_jeu20 = 1
            A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            
            n = len(A)
            coord_initiale = [0, taille*(14-n)/2]
            fenetre.blit(fond_monde4, (0,0))
            initialisation_monde4(A, fenetre, coord_initiale)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            
            ennemi1 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi1 = perso.get_rect()
            ennemi2 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi2 = perso.get_rect()
            ennemi3 = pygame.image.load("chevalier.png").convert_alpha()
            position_ennemi3 = perso.get_rect()
            tete_chercheuse = pygame.image.load("squelette 50.png").convert_alpha()
            position_tete_chercheuse = perso.get_rect()
            
            i_ennemi1, j_ennemi1 = 2, 2 #Position de l'ennemi (basique)
            i_ennemi2, j_ennemi2 = 8, 8 #Position de l'ennemi (basique)
            i_ennemi3, j_ennemi3 = 9, 9 #Position de l'ennemi (basique)
            ie, je = 1, 1 #Position de l'ennemi (tête chercheuse)
            
            comptage = 27
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            compteur = 0
        
        initialisation_monde4(A, fenetre, coord_initiale)
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        position_ennemi = (coord_initiale[0] + (jb)*taille, coord_initiale[1] + (ib)*taille)
        fenetre.blit(ennemi, position_ennemi)

        # rafraichissement de l'image
        pygame.display.flip()
    
    a = t.time()
    
    while continuer_jeu20:
        pygame.time.Clock().tick(40)
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu20 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                ir, jr = i, j
                if event.key == K_ESCAPE:
                    continuer_jeu20 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                    ib += deplacement_bh(ib,jb,1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                    ib += deplacement_bh(ib,jb,-1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                    jb += deplacement_dg(ib,jb,1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                    jb += deplacement_dg(ib,jb,-1, A)
                    ennemi = pygame.image.load("ennemi_gauche.png").convert_alpha()
                    
                deplacement_t = pattern_tete_chercheuse(A, ir, jr, ie, je)
                ie, je = deplacement_t[0], deplacement_t[1]
                deplacement_ennemi1 = pattern(i_ennemi1, j_ennemi1, A)
                i_ennemi1, j_ennemi1 = deplacement_ennemi1[0], deplacement_ennemi1[1]
                deplacement_ennemi2 = pattern(i_ennemi2, j_ennemi2, A)
                i_ennemi2, j_ennemi2 = deplacement_ennemi2[0], deplacement_ennemi2[1]
                    
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                if(A[i][j] == 3):
                    A = transpose(A)
                
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)
                
        
        if i == i_ennemi1 and j == j_ennemi1 and shield == 0:
            continuer_jeu20= 0
            continuer_accueil = 1
        if i == i_ennemi2 and j == j_ennemi2 and shield == 0:
            continuer_jeu20= 0
            continuer_accueil = 1
        if i == ie and j == je and shield == 0:
            continuer_jeu20= 0
            continuer_accueil = 1
        if(A[i][j] == 5):
            continuer_jeu20 = 0
            
        if (t.time() - a > 1) and compteur == 0:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 1
        if (t.time() - a > 0.6) and compteur == 1:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 2
        if (t.time() - a > 1.5) and compteur == 2:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 3
        if (t.time() - a > 0.6) and compteur == 3:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 4
        if (t.time() - a > 1.5) and compteur == 4:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 4
        if (t.time() - a > 0.6) and compteur == 4:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 5
        if (t.time() - a > 1.5) and compteur == 5:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 6
        if (t.time() - a > 0.6) and compteur == 6:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 7
        if (t.time() - a > 1.5) and compteur == 7:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 8
        if (t.time() - a > 0.6) and compteur == 8:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 9
        if (t.time() - a > 1.5) and compteur == 9:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",2)
            remplissage(A, jl, 1, 10, "colonne",2)
            il = i
            jl = j
            remplissage(A, il, 1, 15, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 10
        if (t.time() - a > 0.6) and compteur == 10:
            a = t.time()
            remplissage(A, il, 1, 15, "ligne",5)
            remplissage(A, jl, 1, 10, "colonne",5)
            compteur = 11
        if (t.time() - a > 1) and compteur == 11:
            continuer_jeu20 = 0
            continuer_jeu21 = 1
            A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            
            n = len(A)
            coord_initiale = [0, taille*(14-n)/2]
            fenetre.blit(fond_monde4, (0,0))
            initialisation_monde4(A, fenetre, coord_initiale)
            cases = nombre_cases_1(A)
            pygame.display.flip()
            
            
            comptage = 28
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
            compteur = 0
            
        
        
        # rafraichissement de l'image
        initialisation_monde4(A, fenetre, coord_initiale)
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        position_ennemi = (coord_initiale[0] + (jb)*taille, coord_initiale[1] + (ib)*taille)
        fenetre.blit(ennemi, position_ennemi)    
        
        position_ennemi1 = (coord_initiale[0] +j_ennemi1*taille,coord_initiale[1] +  i_ennemi1*taille)
        fenetre.blit(ennemi1, position_ennemi1)
        position_ennemi2 = (coord_initiale[0] +j_ennemi2*taille, coord_initiale[1] + i_ennemi2*taille)
        fenetre.blit(ennemi2, position_ennemi2)
        position_tete_chercheuse = (coord_initiale[0] +je*taille,coord_initiale[1] +  ie*taille)
        fenetre.blit(tete_chercheuse, position_tete_chercheuse)
        
        pygame.display.flip()
        
    a = t.time()
    
    while continuer_jeu21:
        pygame.time.Clock().tick(40)
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu21 = 0
                continuer_accueil = 1
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu21 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                # Changement du terrain
                fenetre.blit(fond_monde4, (0,0))
                if(A[i][j] == 3):
                    A = transpose(A)
                
                initialisation_monde4(A, fenetre, coord_initiale)
                cases = nombre_cases_1(A)
                
        if(A[i][j] == 6):
            continuer_jeu21 = 0
        
        if (t.time() - a > 1) and compteur == 0:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 1
        if (t.time() - a > 0.6) and compteur == 1:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 2
        if (t.time() - a > 1.5) and compteur == 2:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 3
        if (t.time() - a > 0.6) and compteur == 3:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 4
        if (t.time() - a > 1.5) and compteur == 4:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 4
        if (t.time() - a > 0.6) and compteur == 4:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 5
        if (t.time() - a > 1.5) and compteur == 5:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 6
        if (t.time() - a > 0.6) and compteur == 6:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 7
        if (t.time() - a > 1.5) and compteur == 7:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 8
        if (t.time() - a > 0.6) and compteur == 8:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 9
        if (t.time() - a > 1.5) and compteur == 9:
            a = t.time()
            il = i
            jl = j
            remplissage(A, il, 1, 16, "ligne",10)
            remplissage(A, jl, 1, 10, "colonne",10)
            compteur = 10
        if (t.time() - a > 0.6) and compteur == 10:
            a = t.time()
            remplissage(A, il, 1, 16, "ligne",6)
            remplissage(A, jl, 1, 10, "colonne",6)
            compteur = 11
        if(t.time() - a > 1.5) and compteur == 11:
            a = t.time()
            A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,6,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            compteur = 12
        if(t.time() - a > 1) and compteur == 12:
            a = t.time()
            ir = randint(3,12)
            jr = randint(3,8)
            remplir(A, ir, jr, 10)         
            compteur = 13
        if(t.time() - a > 1.6) and compteur == 13:
            a = t.time()
            remplir(A, ir, jr, 6)
            compteur = 14
        if(t.time() - a > 1) and compteur == 14:
            a = t.time()
            remplir(A, ir, jr, 2)
            compteur = 15
        if(t.time() - a > 1) and compteur == 15:
            ib, jb = 6, 21
            A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,6,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,6,6,2,2,1,6,6,6,6,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,6,6,6,6,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,1,6,6,6,6,2,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            comptage = 29
            # Chargement du dialogue
            dialogue = pygame.image.load(str(comptage) + "_dia.jpg").convert()
            fenetre.blit(dialogue, (0,700))
        
        # rafraichissement de l'image
        initialisation_monde4(A, fenetre, coord_initiale)
        
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        position_ennemi = (coord_initiale[0] + (jb)*taille, coord_initiale[1] + (ib)*taille)
        fenetre.blit(ennemi, position_ennemi)  
        pygame.display.flip()
    
        if(i == ib and j == jb):
            continuer_jeu21 = 0
            continuer_jeu22 = 1
            perso = pygame.image.load("heros.png").convert_alpha()
            position_perso = perso.get_rect()
            
            A = [[1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,3,1],
    [1,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,1],
    [1,3,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

            cases = nombre_cases_1(A)
            pygame.display.flip()
            i, j = 2, 1 # Position du héros
            n = len(A)
            coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
            fenetre.blit(fond, (0,0))
            initialisation_monde1(A, fenetre)
            comptage = 1
            compteur = 0
    son_lave.stop()
    
    a = t.time()
    
    while continuer_jeu22 :
        # Demarrage de la boucle
        for event in pygame.event.get() :
            # gestion des evenements
            if event.type == QUIT :
            # quitter la fenetre
                continuer_jeu22 = 0
            if event.type == KEYDOWN :
                # appui sur une touche du clavier
                if event.key == K_ESCAPE:
                    continuer_jeu22 = 0
                if event.key == K_DOWN:
                    i += deplacement_bh(i,j,1, A)
                    perso = pygame.image.load("heros_face.png").convert_alpha()
                if event.key == K_UP:
                    i += deplacement_bh(i,j,-1, A)
                    perso = pygame.image.load("heros_dos.png").convert_alpha()
                if event.key == K_RIGHT:
                    j += deplacement_dg(i,j,1, A)
                    perso = pygame.image.load("heros_droite.png").convert_alpha()
                if event.key == K_LEFT:
                    j += deplacement_dg(i,j,-1, A)
                    perso = pygame.image.load("heros_gauche.png").convert_alpha()
                
                if(A[i][j] == 3):
                    A = transpose(A)
                # Changement du terrain
                fenetre.blit(fond, (0,0))
                initialisation_monde1(A, fenetre)
                cases = nombre_cases_1(A)
        position_perso = (coord_initiale[0] + j*taille, coord_initiale[1] + i*taille)
        fenetre.blit(perso, position_perso)
        pygame.display.flip()
        
        if t.time() - a > 5 and compteur == 0:
            a = t.time()
            fin = pygame.image.load("fin.jpg").convert()
            fenetre.blit(fin, (0,700))
            compteur = 1
        if t.time() - a > 20 and compteur == 1:
            continuer_jeu22 = 0

