import pygame
from pygame.locals import *
from constantes import *
import copy as c
from random import *


# CREATION DU NIVEAU

def initialisation_monde1(A, fenetre):
    ''' iniatilise le terrain'''
    n = len(A)
    mur = pygame.image.load("noir.jpg").convert_alpha()
    blanc = pygame.image.load("blanc.jpg").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("noir.jpg").convert_alpha()
    cle = pygame.image.load("cle.png").convert_alpha()
    porte = pygame.image.load("porte.png").convert_alpha()
    bonus_sym_h = pygame.image.load("vert.jpg").convert_alpha()
    bonus_sym_v = pygame.image.load("bleu.jpg").convert_alpha()
    inver = pygame.image.load("inver.png").convert_alpha()
    
    
    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                fenetre.blit(fond,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 4:
                fenetre.blit(cle,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 5:
                fenetre.blit(porte,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 6:
                fenetre.blit(bonus_sym_h, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 7:
                fenetre.blit(bonus_sym_v,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == -1:
                fenetre.blit(inver, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                
                
def initialisation_monde2(A, fenetre):
    ''' iniatilise le terrain'''
    n = len(A)
    mur = pygame.image.load("fond ciel 1.jpg").convert_alpha()
    blanc = pygame.image.load("fond ciel 2.jpg").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("fond ciel 1.jpg").convert_alpha()
    cle = pygame.image.load("cle.png").convert_alpha()
    porte = pygame.image.load("porte.png").convert_alpha()
    bonus_sym_h = pygame.image.load("vert.jpg").convert_alpha()
    bonus_sym_v = pygame.image.load("bleu.jpg").convert_alpha()
    inver = pygame.image.load("inver.png").convert_alpha()
    
    
    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                fenetre.blit(fond,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 4:
                fenetre.blit(cle,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 5:
                fenetre.blit(porte,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 6:
                fenetre.blit(bonus_sym_h, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 7:
                fenetre.blit(bonus_sym_v,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == -1:
                fenetre.blit(inver, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                
def initialisation_monde3(A, fenetre):
    ''' iniatilise le terrain'''
    n = len(A)
    mur = pygame.image.load("mur rocher.jpg").convert_alpha()
    blanc = pygame.image.load("caverne2.png").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("herbe2.png").convert_alpha()
    cle = pygame.image.load("cle.png").convert_alpha()
    porte = pygame.image.load("porte.png").convert_alpha()
    bonus_sym_h = pygame.image.load("symetrie verticale monde 3 (50 x 50).png").convert_alpha()
    bonus_sym_v = pygame.image.load("symetrie horizontale monde 3 (50 x 50).png").convert_alpha()
    inver = pygame.image.load("inver.png").convert_alpha()
    shield = pygame.image.load("shield (50 x 50).png")
    
    
    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                fenetre.blit(fond,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 4:
                fenetre.blit(cle,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 5:
                fenetre.blit(porte,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 6:
                fenetre.blit(bonus_sym_h, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 7:
                fenetre.blit(bonus_sym_v,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == -1:
                fenetre.blit(inver, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 8:
                fenetre.blit(shield, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                
def initialisation_monde3_bis(A, fenetre):
    ''' iniatilise le terrain'''
    n = len(A)
    mur = pygame.image.load("mur rocher.jpg").convert_alpha()
    blanc = pygame.image.load("caverne2.png").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("herbe2.png").convert_alpha()
    cle = pygame.image.load("cle.png").convert_alpha()
    porte = pygame.image.load("porte.png").convert_alpha()
    bonus_sym_h = pygame.image.load("symetrie verticale monde 3 (50 x 50).png").convert_alpha()
    bonus_sym_v = pygame.image.load("symetrie horizontale monde 3 (50 x 50).png").convert_alpha()
    inver = pygame.image.load("inver.png").convert_alpha()
    shield = pygame.image.load("shield (50 x 50).png")
    
    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                fenetre.blit(fond,(j*taille, i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(j*taille, i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc, (j*taille, i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(j*taille, i*taille))
            if A[i][j] == 4:
                fenetre.blit(cle,(j*taille, i*taille))
            if A[i][j] == 5:
                fenetre.blit(porte,(j*taille, i*taille))
            if A[i][j] == 6:
                fenetre.blit(bonus_sym_h, (j*taille, i*taille))
            if A[i][j] == 7:
                fenetre.blit(bonus_sym_v,(j*taille, i*taille))
            if A[i][j] == -1:
                fenetre.blit(inver, (j*taille, i*taille))
            if A[i][j] == 8:
                fenetre.blit(shield, (j*taille, i*taille))

def initialisation_monde4(A, fenetre, coord_initiale):
    ''' iniatilise le terrain'''
    
    n = len(A)
    mur = pygame.image.load("mur_lave.jpg").convert_alpha()
    blanc = pygame.image.load("terre_lave.jpg").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("mur_lave.jpg").convert_alpha()
    cle = pygame.image.load("cle.png").convert_alpha()
    porte = pygame.image.load("porte.png").convert_alpha()
    bonus_sym_h = pygame.image.load("bleu.jpg").convert_alpha()
    bonus_sym_v = pygame.image.load("vert.jpg").convert_alpha()
    inver = pygame.image.load("inver.png").convert_alpha()
    lave1 = pygame.image.load("lave1.png").convert_alpha()
    lave2 = pygame.image.load("lave2.png").convert_alpha()
    lave3 = pygame.image.load("lave3.png").convert_alpha()
    lave4 = pygame.image.load("lave4.png").convert_alpha()
    rouge = pygame.image.load("rouge.jpg").convert_alpha()
    noir = pygame.image.load("noir.jpg").convert_alpha()
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            r = randint(1,4)
            if A[i][j] == 0:
                fenetre.blit(fond,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 4:
                fenetre.blit(bonus_sym_h, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 7:
                fenetre.blit(bonus_sym_v,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == -1:
                fenetre.blit(inver, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 5:
                if r == 1 :
                    fenetre.blit(lave1, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                if r == 2 :
                    fenetre.blit(lave2, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                if r == 3 :
                    fenetre.blit(lave3, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                if r == 4 :
                    fenetre.blit(lave4, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 8:
                fenetre.blit(porte,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 9:
                fenetre.blit(cle,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 10:
                fenetre.blit(rouge,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 6:
                fenetre.blit(noir, (coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))
                

                

def initialisation(A, fenetre):
    ''' iniatilise le terrain'''
    n = len(A)
    mur = pygame.image.load("mur rocher.jpg").convert_alpha()
    blanc = pygame.image.load("caverne2.png").convert_alpha()
    bonus_transpo = pygame.image.load("Bloc T.png").convert_alpha()
    fond = pygame.image.load("herbe2.png").convert_alpha()
    
    coord_initiale = [taille*(24-n)/2, taille*(14-n)/2]
    
    for i in range(0,n):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                fenetre.blit(fond,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 1:
                fenetre.blit(mur,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 2:
                fenetre.blit(blanc,(coord_initiale[0] + j*taille, coord_initiale[1] + i*taille))
            if A[i][j] == 3:
                fenetre.blit(bonus_transpo,(coord_initiale[0] +j*taille, coord_initiale[1] + i*taille))

# CONDITIONS DE VICTOIRE

def nombre_cases_1(A):
    '''Calcul le nombre de cases encore restantes'''
    somme = 0
    n = len(A)
    N = len(A[0])
    for i in range(0,n):
        for j in range(0,N):
            if A[i][j] == 0:
                somme += 1
    return somme

# GESTION DU DEPLACEMENT + RECOLORIAGE

def deplacement_bh(i,j,a,A):
    ''' déplace le personnage à la case voulu'''    
    if (A[i+a][j] != 1):
        if(A[i][j] == 0):
            A[i][j] = 2
        return a
    return 0
    
def deplacement_dg(i,j,a,A):
    ''' déplace le personnage à la case voulu'''
    if (A[i][j+a] != 1):
        if(A[i][j] == 0):
            A[i][j] = 2
        return a
    return 0
    
# INTELLIGENCE ARTIFICIELLE
def pattern (i_ennemi, j_ennemi, A):
    '''déplacement aléatoire de l'ennemi'''
    L = [1,2,3,4]#liste contenant les déplacements possibles: 1=haut, 2=bas, 3=droite, 4=gauche
    if A[i_ennemi + 1][j_ennemi] == 1:
        L.remove(1)
    if A[i_ennemi - 1][j_ennemi] == 1:
        L.remove(2)
    if A[i_ennemi][j_ennemi + 1] == 1:
        L.remove(3)
    if A[i_ennemi][j_ennemi - 1] == 1:
        L.remove(4)
    a = choice(L)#l'ennemi se déplace à chaque tour dans une direction ou il peut aller, on enlève donc les direcions impossibles
    if a == 1:
        return(i_ennemi + 1, j_ennemi)
    if a == 2:
        return(i_ennemi - 1, j_ennemi)
    if a == 3:
        return(i_ennemi, j_ennemi + 1)
    if a == 4:
        return(i_ennemi, j_ennemi - 1)


def pattern_tete_chercheuse(A, iper, jper, it, jt):
    "pattern ennemi ia qui se dirige toujours vers le héros"
    L = [1,2,3,4]#liste contenant les déplacements possibles: 1=bas, 2=haut, 3=droite, 4=gauche
    if A[it + 1][jt] == 1:
        L.remove(1)
    if A[it - 1][jt] == 1:
        L.remove(2)
    if A[it][jt + 1] == 1:
        L.remove(3)
    if A[it][jt - 1] == 1:
        L.remove(4)
    dhaut = 10000
    dbas = 10000
    ddroite = 10000
    dgauche = 10000
    M=[]
    if L.count(1) != 0:
        dbas = ((it + 1 - iper)**2 + (jt - jper)**2) #distance au carré case fictive après avancée (dbas) et la case du héros à ce tour
        M.append([dbas, 1])
    if L.count(2) != 0:
        dhaut = ((it - 1 - iper)**2 + (jt - jper)**2) #distance au carré case fictive après avancée (haut) et la case du héros à ce tour
        M.append([dhaut, 2])
    if L.count(3) != 0:
        ddroite = ((it - iper)**2 + (jt + 1 - jper)**2) #distance au carré case fictive après avancée (droite) et la case du héros à ce tour
        M.append([ddroite, 3])
    if L.count(4) != 0:
        dgauche = ((it - iper)**2 + (jt -1 - jper)**2) #distance au carré case fictive après avancée (gauche) et la case du héros à ce tour
        M.append([dgauche, 4])
    m = M[0][0]
    for k in range(len(M)):
        if m > M[k][0]:
            m = M[k][0] #m est le min des distances
    for l in M:
        if l[0] == m:
            M = l
            break # on supprime les déplacements inninteressants
    direction = M[1]
    if direction == 1:
        return(it + 1, jt)
    if direction == 2:
        return(it - 1, jt)
    if direction == 3:
        return(it, jt + 1)
    if direction == 4:
        return(it, jt - 1)
    

def pattern_bouledefeu(A, ibo, jbo, tir):
    "deplacement boule de feu lancée par un magicien-2 cases par tour"
    if tir == 1:
        if A[ibo + 1][jbo] != 1:
            return(ibo + 1, jbo)
        else:
            tir = 0
            return(0,0)
    if tir == 2:
        if A[ibo - 1][jbo] != 1:
            return(ibo - 1, jbo)
        else:
            tir = 0
            return(0,0)
    if tir == 3:
        if A[ibo][jbo + 1] != 1:
            return(ibo, jbo + 1)
        else:
            tir = 0
            return(0,0)
    if tir == 4:
        if A[ibo][jbo - 1] != 1:
            return(ibo, jbo - 1)
        else:
            tir = 0
            return(0,0)

def pattern_magicien(A, iper, jper, imag, jmag, ibo, jbo):
    "pattern ennemi ia qui se dirige toujours vers le héros et lance des boules de feu (1 max)"
    L = [1,2,3,4]#liste contenant les déplacements possibles: 1=bas, 2=haut, 3=droite, 4=gauche
    if A[imag + 1][jmag] == 1:
        L.remove(1)
    if A[imag - 1][jmag] == 1:
        L.remove(2)
    if A[imag][jmag + 1] == 1:
        L.remove(3)
    if A[imag][jmag - 1] == 1:
        L.remove(4)
    dhaut = 10000
    dbas = 10000
    ddroite = 10000
    dgauche = 10000
    M=[]
    if L.count(1) != 0:
        dbas = ((imag + 1 - iper)**2 + (jmag - jper)**2) #distance au carré case fictive après avancée (bas) et la case du héros à ce tour
        M.append([dbas, 1])
    if L.count(2) != 0:
        dhaut = ((imag - 1 - iper)**2 + (jmag - jper)**2) #distance au carré case fictive après avancée (haut) et la case du héros à ce tour
        M.append([dhaut, 2])
    if L.count(3) != 0:
        ddroite = ((imag - iper)**2 + (jmag + 1 - jper)**2) #distance au carré case fictive après avancée (droite) et la case du héros à ce tour
        M.append([ddroite, 3])
    if L.count(4) != 0:
        dgauche = ((imag - iper)**2 + (jmag -1 - jper)**2) #distance au carré case fictive après avancée (gauche) et la case du héros à ce tour
        M.append([dgauche, 4])
    m = M[0][0]
    for k in range(len(M)):
        if m > M[k][0]:
            m = M[k][0] #m est le min des distances
    for l in M:
        if l[0] == m:
            M = l
            break # on supprime les déplacements inninteressants
    direction = M[1]
    if iper == imag and ibo == 0 and jbo == 0:
        if jper >= jmag and A[imag][jmag + 1] != 1:
            tir = 3 #(droite)
            return(imag, jmag, imag, jmag + 1, tir)
        if jper <= jmag and A[imag][jmag - 1] != 1:
            tir = 4 #(gauche)
            return(imag, jmag, imag, jmag - 1, tir)
    if jper == jmag and ibo == 0 and jbo == 0:
        if iper >= imag and A[imag + 1][jmag] != 1:
            tir = 1 #(bas)
            return(imag, jmag, imag + 1, jmag, tir)
        if iper <= imag and A[imag - 1][jmag] != 1:
            tir = 2 #(haut)
            return(imag, jmag, imag - 1, jmag, tir)
    if direction == 1:
        return(imag + 1, jmag, ibo, jbo, 0)
    if direction == 2:
        return(imag - 1, jmag, ibo, jbo, 0)
    if direction == 3:
        return(imag, jmag + 1, ibo, jbo, 0)
    if direction == 4:
        return(imag, jmag - 1, ibo, jbo, 0)
# OPERATIONS SUR LES MATRICES

def transpose(A):
    ''' Passe la matrice à la transposée '''
    n = len(A)
    
    B = c.deepcopy(A)
    
    for i in range(n):
        for j in range(n):
            B[i][j] = A[j][i]
    
    return B
    
def symetrie_horizontale(A):
    ''' fait une symétrie par rapport au centre'''
    n = len(A)
    
    B = c.deepcopy(A)
    
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][n-1-j]
    
    return B

def symetrie_verticale(A):
    ''' fait une symétrie par rapport au centre'''
    n = len(A)
    
    B = c.deepcopy(A)
    
    for i in range(n):
        for j in range(n):
            B[i][j] = A[n-1-i][j]
            
    return B
    
def remplissage(A, cl, deb, fin, boolean, num):
    ''' Remplit la colonne ou la ligne d'une matrice choisi'''

    if boolean == "ligne":  # SUR LA LIGNE
        for j in range(deb, fin+1):
            A[cl][j] = num
        
    if boolean == "colonne":  # SUR LA LIGNE
        for i in range(deb, fin+1):
            A[i][cl] = num

def remplir(A, ir, jr,  num):
    ''' Remplit tout sauf une case'''
    
    for i in range(0,len(A)):
        for j in range(0, len(A[0])):
            if i != ir or j != jr :
                A[i][j] = num
    