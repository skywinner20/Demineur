#!/usr/bin/env python
# coding: utf-8

# # Journal de bord du projet
# 
# Voici le fichier qui va servir de journal de bord et de fichier de prototypage
# 
# ## Création de la grille
# 
# On va utiliser des liste imbriquées avec les valeurs suivantes pour représenter les différents cas

# Ci-dessous la liste des import nécessaires

# In[1]:


import random
import math
import OCI_TurtleMineur as tm

# In[2]:


def magrille(l,c):
    grille = []
    for i in range(l):
        grille.append([0]*c)
    return grille





# ## Fonction d'affichage de la grille

# In[5]:


def printGrille(magrille):
    nbligne = len(magrille)
    nbcol = len(magrille[0])
    
    tm.drawGrid(nbligne, nbcol, size = 10, space = 2)
    
    for i in range(nbligne):
        lignetexte = "|"
        for j in range(nbcol):
            lignetexte += "{0} |".format(magrille[i][j])
        print(lignetexte)


# In[6]:




# ## Placement des bombes
# 
# On veut choisir n élément parmis les positions

# In[ ]:





# Pour choisir les positions des bombes aléatoirement on commence par générer toutes les positions possibles puis on choisit le nombre souhaité parmis ces positions avec `random.sample` qui permet de ne pas choisir 2 fois la même position.

# In[7]:


def genPos(l,c):
    pos = []
    for i in range(l):
        for j in range(c):
            pos.append((i,j))
    return pos


# In[8]:


def putBomb(grille, nbBomb):
    nbligne = len(grille)
    nbcol = len(grille[0])
    pos = genPos(nbligne, nbcol)
    posBomb = random.sample(pos, nbBomb)
    for bomb in posBomb:
        grille[bomb[0]][bomb[1]] = "B"
    return grille


# In[9]:





# ## Nombre de bombes voisines
# 
# Les cases qui ne sont pas des bombes doivent afficher le nombre de bombes dans leur voisinage, i.e. les 8 cases autour dans le cas général.
# 
# La démarche proposé pour faire cela est la suivante :
# * Pour chaque case, obtenir les coordonnées de ses voisins valides (cas des bords et des coins)
# * Mettre le compteur de bombes à 0
# * Pour chacun des voisins valide, s'il s'agit d'une bombe incrémenter le compteur de 1
# * Inscrire la valeur du compteur de bombe à la position de la case examinée
# 
# Ainsi, la première étape consiste à obtenir les coordonnées des voisins valides.
# 
# ### Trouver les voisins
# 
# Pour une case de coordonnées x et y, les 8 voisins sont :
#  * x-1, y-1
#  * x-1, y
#  * x-1, y+1
#  * x, y-1
#  * x, y+1
#  * x+1, y-1
#  * x+1, y
#  * X+1, y+1

# In[10]:


def voisins(x,y, grille):
    """
    Trouve les coordonnées valides des voisins de x,y
    """
    voisins = []
    nbligne = len(grille)
    nbcol = len(grille[0])
    if x-1 in range(nbligne):
        voisins.append((x-1,y))
        if y-1 in range(nbcol):
            voisins.append((x-1,y-1))
        if y+1 in range(nbcol):
            voisins.append((x-1,y+1))
    if x+1 in range(nbligne):
        voisins.append((x+1,y))
        if y-1 in range(nbcol):
            voisins.append((x+1,y-1))
        if y+1 in range(nbcol):
            voisins.append((x+1,y+1))
    if y-1 in range(nbcol):
            voisins.append((x,y-1))
    if y+1 in range(nbcol):
            voisins.append((x,y+1))  
            
    return voisins



# ### Compter les bombes

# In[17]:


def countBombs(grille):
    nbligne = len(grille)
    nbcol = len(grille[0])
    pos = genPos(nbligne, nbcol)
    for x,y in pos :
        if grille[x][y] != "B":
            cptbomb = 0
            vs = voisins(x,y,grille)
            for i,j in vs:
                if grille[i][j] == "B":
                    cptbomb += 1
            grille[x][y] = cptbomb


# In[18]:





# In[19]:
if __name__ == "__main__":
    mg = magrille(10,10)
    mgB = putBomb(mg,21)
    countBombs(mgB)
    printGrille(mgB)


# In[ ]:




