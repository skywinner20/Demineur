#      ,--.!,
#   __/   -*-
# ,d08b.  '|`
# 0088MM
# `9MMP'  --- Ardi et Cédric, Démineur ---
# Bienvenue dans le futur jeu vidéo du siècle, litéralement le GOTY 2022, on a déjà été contacté par EA, Sony, Microsoft et Microids Studios

import random #Les imports
import math

# - - - - - DÉBUT DES FONCTIONS - - - - - -

def magrille(l,c):
    """
    Prends nbr de lignes et de colonnes et retourne une matrice (liste de liste) de la grille
    """
    grille = []
    for i in range(l):
        grille.append([0]*c)
    return grille

def printGrille(magrille):
    """
    Prends la grille et retourne un bel affichage pour le user
    """
    nbligne = len(magrille)
    nbcol = len(magrille[0])
    affichage_col = "-  "
    for i in range(nbcol):
        if i < 10:
            affichage_col += " {0} ".format(i)
        else:
            affichage_col += "{0} ".format(i)
    print(affichage_col)
    for i in range(nbligne):
        lignetexte = "|"
        for j in range(nbcol):
                lignetexte += "{0} |".format(magrille[i][j])
        if i < 10:
            print("{0}  {1}".format(i, lignetexte))
        else:
            print("{0} {1}".format(i, lignetexte))

def genPos(l,c):
    """
    Prends le nbr de lignes et de colonnes et génère une liste de positions aléatoire (pour les bombes)
    """
    pos = []
    for i in range(l):
        for j in range(c):
            pos.append((i,j))
    return pos

def putBomb(grille, nbBomb):
    """
    Prends la liste représentant la grille et le nb de bombes, et les places aléatoirement dans la grille
    """
    nbligne = len(grille)
    nbcol = len(grille[0])
    pos = genPos(nbligne, nbcol)
    posBomb = random.sample(pos, nbBomb)
    for bomb in posBomb:
        grille[bomb[0]][bomb[1]] = "B"
    return grille

def GrilleScore(grille_bombee): #Entendre par là: la grille avec les bombes placées et rien de plus
    """
    Prends la grille bombée et mets les numéros en testant chaque case avec ses 8 voisins
    """

    for i in range(len(grille_bombee)):
        for k in range(len(grille_bombee[i])): #Préciser de quelle liste on parle | Envisager le try ? -> Seule manière possible mais c'est PAS BEAU.
            n = 0
            if grille_bombee[i][k] == "B":
                n = "B"     #Nbr de bombes voisins
            else:
                try: #Enchainement de try
                    if grille_bombee[i - 1][k - 1] == "B" and i != 0 and k != 0: #En haut à gauche
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i][k - 1] == "B" and k != 0: #En haut au milieu
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i + 1][k - 1] == "B" and k != 0 and i != len(grille_bombee[i]): #En haut à droite
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i - 1][k] == "B" and i != 0: #Au milieu à gauche
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i + 1][k] == "B" and i != len(grille_bombee[i]) : #Au milieu à droite
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i - 1][k + 1] == "B" and i != 0 and k != len(grille_bombee[k]): #En bas à gauche
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i][k + 1] == "B" and k != len(grille_bombee[k]): #En bas au milieu
                        n += 1
                except IndexError:
                    pass
                try:
                    if grille_bombee[i + 1][k + 1] == "B" and k != len(grille_bombee[k]) and i != len(grille_bombee[i]): #En bas à droite
                        n += 1
                except IndexError:
                    pass
            
            grille_bombee[i][k] = n
    return(grille_bombee)

def grille_cachee(liste_b): #Le but de cette matrice est d'être remplacé par la liste GrilleScore avec les appels du joueur
    """
    Prends la grille bombée et numerotée, et retourne une grille cachée
    """
    grille = []
    for i in range(len(liste_b)): 
        grille.append(list("□"*len(liste_b[0]))) #IL FALLAIT JUSTE TRANSFORMER LITERABLE EN LISTE JE VAIS DEVENIR FOU
    return grille

def user_inter(liste_grille): # Interaction user
    """
    Prends la liste de la grille, demande les variables lignes colonnes action au user pour savoir ce qu'il veut faire et retourne l_user, c_user et action tq. l_user = ligne choisie, c_user = colonne choisie et action = action choisie
    
    action possible: m, f, ?
    """
    flag_nbr = False #Flag pour les nombres
    flag_action = False #Flag pour l'action
    flag_nbr_mem = False #Flag de mémoire pour les nombres

    while flag_nbr == False or flag_action == False: #Testeurs pour savoir si les variables sont légales ou pas
        try:    
            l_user, c_user, action = input("Que voulez-vous faire? (ligne colonne action, action possibles: m(Marcher), f(Drapeau), ?): ").split(" ")
        except ValueError:
            print("Erreur: Nombre de paramètres faux") #Cette erreur est retournée si input().split() reçoit trop d'arguments

        try: #Bien des valeurs et pas autre chose
            l_user = int(l_user)
            c_user = int(c_user)
            flag_nbr_mem = True
        except ValueError: #Erreur retournée si int() impossible
            print("Erreur: Nombre(s) incorrecte(s)")

        if flag_nbr_mem == True: #Verif de nombres l et c légal
            if 0 <= l_user <= len(liste_grille) and 0 <= c_user <= len(liste_grille[0]): #Si les valeurs existent
                l_user = int(l_user)
                c_user = int(c_user)
                flag_nbr = True
            else:
                print("Erreur: Nombres impossibles, ils ne sont pas dans la grille")
        
        try: #Verif action légal
            if action == "m":
                flag_action = True
            elif action == "f":
                flag_action = True
            elif action == "?":
                flag_action = True
            elif action == "DEBUG":
                flag_action = True
            else:
                print("Erreur: Action incorrecte")
        except ValueError:
            print("Erreur: Action incorrecte")
            
    
    return l_user, c_user, action

def gameplay(l_user, c_user, action, grilleJoueur, grillescore): #Là ou va se jouer le GAMING (interaction userinput et grille)
    """
    Prends les valeurs l_user, c_user, action, grille que modifie le joueur, la grille scorée, et retourne la grille modifiée en circonstance, DeathBomb si une bombe est touchée,
    FBomb si un f a été placé sur une bombe, n si une case intouchable est touchée, FlagFlag tq. 0 = pas de drapeau posé, 1 = drapeau ajouté, 2 = drapeau retiré, 3 = drapeau retiré sur une bombe
    """
    DeathBomb = False #Si true -> Bombe touchée, Game Over
    FBomb = False #Si true -> Case minée flaguée
    l_user = int(l_user) #Simplifier ce cambouilli
    c_user = int(c_user)
    grilleJoueur = grilleJoueur.copy() #Juste moi qui panique, techniquement cette commande est redondante, mais j'ose pas l'enlever par peur de tout casser
    FlagDebug = False #Si true -> Active Debug: Affiche la grille
    n = False #Si true -> Erreur, ne fais rien a la grille et relance le joueur
    FlagFlag = 0 #Si 1 -> drapeau posé, si 2 -> drapeau retiré, si 3 -> drapeau retiré alors qu'il est juste
    try:
        if action == "m": #Si action Marcher

            if grilleJoueur[l_user][c_user] != "□" or grilleJoueur[l_user][c_user] == "f" or grilleJoueur[l_user][c_user] == "?": #Case innouvrable
                n = True

            elif grillescore[l_user][c_user] == "B": #Marcher sur Bombe
                grilleJoueur[l_user][c_user] == "B"
                DeathBomb = True

            elif grillescore[l_user][c_user] == 0: #Marcher sur Zéro

                grilleJoueur[l_user][c_user] = int(grillescore[l_user][c_user]) #Remplacer la case
                if flag_turtle == True:
                    tr.nombrebombestortue(l_user,c_user,int(grillescore[l_user][c_user]))

                # - - - Maintenant, il faut montrer les 8 voisins - - -

                if (l_user - 1) >= 0 and (c_user - 1) >= 0: #En haut à gauche
                    grilleJoueur[l_user - 1][c_user - 1] = int(grillescore[l_user - 1][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user - 1,int(grillescore[l_user - 1][c_user - 1]))
                    if grillescore[l_user - 1][c_user - 1] == 0:
                        gameplay(l_user - 1, c_user - 1, "m", grilleJoueur, grillescore) #0 en cascades

                if (l_user - 1) >= 0: #En haut au milieu
                    grilleJoueur[l_user - 1][c_user] = int(grillescore[l_user - 1][c_user])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user,int(grillescore[l_user - 1][c_user]))
                    if grillescore[l_user - 1][c_user] == 0:
                        gameplay(l_user - 1, c_user, "m", grilleJoueur, grillescore) #0 en cascades

                if (l_user - 1) >= 0 and (c_user + 1) < len(grilleJoueur[0]): #En haut à droite
                    grilleJoueur[l_user - 1][c_user + 1] = int(grillescore[l_user - 1][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user + 1,int(grillescore[l_user - 1][c_user + 1]))
                    if grillescore[l_user - 1][c_user + 1] == 0:
                        gameplay(l_user - 1, c_user + 1, "m", grilleJoueur, grillescore) #0 en cascades

                if (c_user - 1) >= 0: #Au milieu à gauche
                    grilleJoueur[l_user][c_user - 1] = int(grillescore[l_user][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user - 1,int(grillescore[l_user][c_user - 1]))
                    if grillescore[l_user][c_user - 1] == 0:
                        gameplay(l_user, c_user - 1, "m", grilleJoueur, grillescore) #0 en cascades
                
                if (c_user + 1) < len(grilleJoueur[0]): #Au milieu à droite
                    grilleJoueur[l_user][c_user + 1] = int(grillescore[l_user][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user + 1,int(grillescore[l_user][c_user + 1]))
                    if grillescore[l_user - 1][c_user - 1] == 0:
                        gameplay(l_user, c_user + 1, "m", grilleJoueur, grillescore) #0 en cascades
                
                if (l_user + 1) < len(grilleJoueur) and 0 <= (c_user - 1) < len(grilleJoueur[0]): #En bas à gauche
                    grilleJoueur[l_user + 1][c_user - 1] = int(grillescore[l_user + 1][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user - 1,int(grillescore[l_user + 1][c_user - 1]))
                    if grillescore[l_user + 1][c_user - 1] == 0:
                        gameplay(l_user + 1, c_user - 1, "m", grilleJoueur, grillescore) #0 en cascades
                
                if (l_user + 1) < len(grilleJoueur): #En bas au milieu
                    grilleJoueur[l_user + 1][c_user] = int(grillescore[l_user + 1][c_user])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user,int(grillescore[l_user + 1][c_user]))
                    if grillescore[l_user + 1][c_user] == 0:
                        gameplay(l_user + 1, c_user, "m", grilleJoueur, grillescore) #0 en cascades
                
                if (l_user + 1) < len(grilleJoueur) and (c_user + 1) < len(grilleJoueur[0]): #En bas à droite
                    grilleJoueur[l_user + 1][c_user + 1] = int(grillescore[l_user + 1][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user + 1,int(grillescore[l_user + 1][c_user + 1]))
                    if grillescore[l_user + 1][c_user + 1] == 0:
                        gameplay(l_user + 1, c_user + 1, "m", grilleJoueur, grillescore) #0 en cascades
            
            else: #le reste 
                grilleJoueur[l_user][c_user] = int(grillescore[l_user][c_user])
                if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user,int(grillescore[l_user][c_user]))
        
        elif action == "f": #Drapeau
            
            FlagFlag = 1 #Drapeau posé
            if grilleJoueur[l_user][c_user] == "f": #Pour enlever le drapeau
                grilleJoueur[l_user][c_user] = "□"
                if flag_turtle == True:
                        tr.casenormaleturtle(l_user,c_user)
                if grillescore[l_user][c_user] == "B": #Si drapeau retiré sur case minée
                    FlagFlag = 3
                    
            
            elif grillescore[l_user][c_user] == "B": #Si drapeau sur bombe
                FBomb = True
                grilleJoueur[l_user][c_user] = "f"
                if flag_turtle == True:
                        tr.drapeautortue(l_user,c_user)
                
            else: #Drapeau sur case vide
                grilleJoueur[l_user][c_user] = "f"
                if flag_turtle == True:
                        tr.drapeautortue(l_user,c_user)
                FlagFlag = 2

            
    
        elif action == "?": #Interrogation
            if grilleJoueur[l_user][c_user] == "?":
                grilleJoueur[l_user][c_user] = "□"
                if flag_turtle == True:
                        tr.casenormaleturtle(l_user,c_user)       
            else:
                grilleJoueur[l_user][c_user] = "?"
                if flag_turtle == True:
                        tr.pointinterrogationtortue(l_user,c_user)
        
        elif action == "DEBUG": #Debug
            FlagDebug = True
    except IndexError:
        print("Erreur: Case en dehors de la grille.")

    return grilleJoueur, DeathBomb, FBomb, FlagDebug, n, FlagFlag, grillescore

def DebutGame():
    """
    Fait débuter la partie. Demande au user le nbr de lignes, colonnes et bombes, et retourne les valeurs lignes, colonnes et bombes
    """

    # - - - Présentation - - -
    print("     ,--.!,\n  __/   -*-\n,d08b.  '|`\n0088MM\n`9MMP'   Démineur - Ardi et Cédric")
    print("Bienvenue dans le futur du Gaming et du divertissement, vous allez adorer ! Je ne vais pas vous faire l'affront de vous expliquer comment jouer.")

    # - - - Les Flags - - -
    flag_a = False #Flag Bombes
    flag_b = False #Flag Colonnes
    flag_c = False #Flag lignes
    flag_d = False #Flag Input Turtle o/n
    flag_turtle = False #Flag Turtle

    # - - - Flag Turtle - - -
    while flag_d == False:
        try: #turtle ou pas
            d = input("Voulez-vous jouer avec les graphisems turtle ? (oui ou non): ")
            
            if d == "oui":
                flag_turtle = True
                flag_d = True
            elif d == "non":
                flag_d = True
            else:
                print('La réponse doit être "oui" ou "non".')
        except ValueError:
            print('La réponse doit être "oui" ou "non".')
    
    # - - - Flag Lignes - - -
    while flag_a == False:
        try: #Lignes
            a = input("Combien de lignes voulez-vous ? (Facile: 5, Moyen: 10, Difficile: 15): ")

            if int(a) >= 5 and int(a) <= 70:
                a = int(a)
                flag_a = True
            else:
                print("Erreur: Le nombre de ligne doit être entre 5 et 70")

        except ValueError:
            print("Erreur: Le nombre de ligne doit être entre 5 et 70")
        
    # - - - Flag Colonnes - - -
    while flag_b == False:
        try: #Colonnes
            b = input("Combien de colonnes voulez-vous ? (Facile: 5, Moyen: 10, Difficile: 15): ")

            if int(b) >= 5 and int(b) <= 70:
                b = int(b)
                flag_b = True
            else:
                print("Erreur: Le nombre de colonnes doit être entre 5 et 70.")

        except ValueError:
            print("Erreur: Le nombre de colonnes doit être entre 5 et 70.")
        
    # - - - Flag Bombes - - -
    while flag_c == False:
        try:
            c = input("Combien de bombes voulez-vous ? (Facile: 5, Moyen: 20, Difficile: 50): ")

            if int(c) <= (int(a)*int(b))/2 and int(c) >= 5:
                c = int(c)
                flag_c = True
            else:
                print("Erreur: Il doit y avoir entre 5 et la moitié du nombre de cases de bombes.")
        
        except ValueError:
            print("Erreur: Il doit y avoir entre 5 et la moitié du nombre de cases de bombes.")
        
    return a, b, c, flag_turtle

# - - - - - FIN DES FONCTIONS, MAINTENANT CA DEVIENT RÉEL - - - - - -

# - Début de l'EXPERIENCE
flag_jeu = False
while flag_jeu == False: #permet de rejouer
    nLignes, nColonnes, nBomb, flag_turtle = DebutGame()
    nLignes, nColonnes, nBomb = int(nLignes), int(nColonnes), int(nBomb)
    GrilleNbr = GrilleScore(putBomb(magrille(nLignes, nColonnes), nBomb)) #Génération de la grille avc toutes les infos

    GrilleJoueur = grille_cachee(GrilleNbr) #Création de la grille du joueur

    flag_compteur_juste = 0 #Compteur de drapeaux justes
    TouchBomb = False #Boolean si une bombe est touchée
    FlagFlag = 0 #Pointeur (? pas sûr du terme) pour savoir si un drapeau a été mis ou retiré
    FlagCounter = 0 #Compteur de drapeaux
    FlagDrapeau = False #Flag pour les drapeaux

    printGrille(GrilleJoueur)

    if flag_turtle == True:
        import turtlelib as tr
        tr.grilleturtle(nLignes,nColonnes)

    while not flag_compteur_juste == FlagCounter == nBomb and TouchBomb == False: # Le JEU
        # - - - Interaction User - - -
        l_user, c_user, action_user = user_inter(GrilleNbr)
        # - - - Fonction Gameplay - - -
        grilleJoueur, TouchBomb, FlagBomb, FlagDebug, FlagNon, FlagFlag, GrilleNbr = gameplay(l_user, c_user, action_user, GrilleJoueur, GrilleNbr)
        # - - - Comparaison des variables - - -
        if FlagDebug == True: #Active le Debug
            printGrille(GrilleNbr)
        # - - -
        if FlagBomb == True: #Compteur de drapeau bien mis
            flag_compteur_juste += 1
        # - - -
        if FlagNon == True: #Case impossible à modifier
            print("Case intouchable !")
        # - - -  
        printGrille(GrilleJoueur)
        # - - -
        if FlagFlag > 0: #Compteur de drapeau | Éviter de pouvoir gagner en mettant des drapeaux sur des cases vides
            if FlagFlag == 1: #Drapeau posé
                FlagCounter += 1
                if FlagBomb == True: #Drapeau posé sur bombe
                    flag_compteur_juste += 1
            elif FlagFlag == 2: #Drapeau retirée
                FlagCounter = FlagCounter - 1
            elif FlagFlag == 3: #Drapeau retirée d'une bombe
                flag_compteur_juste = flag_compteur_juste - 1
                FlagCounter = FlagCounter - 1
        # - - -
        print("Il reste {0} bombe(s).".format(nBomb - FlagCounter))
        # - - -
        if TouchBomb == True: #Écran de game over
            print("     ,--.!,\n  __/   -*-\n,d08b.  '|`\n0088MM\n`9MMP'   Game Over. C'était une bombe.")
            print("Voici la grille complète:")
            printGrille(GrilleNbr)
            if flag_turtle == True:
                for i in range(len(GrilleNbr)):
                    for k in range(len(GrilleNbr[i])):
                        if GrilleNbr[i][k] == "B":
                            tr.bombeturtle(i,k)
                        else:
                            tr.nombrebombestortue(i,k,GrilleNbr[i][k])
            print("Rééssayez !")
        # - - -

        if flag_compteur_juste == nBomb: #Victoire
            printGrille(GrilleNbr)
            if flag_turtle == True:
                for i in range(len(GrilleNbr)):
                    for k in range(len(GrilleNbr[i])):
                        if GrilleNbr[i][k] == "B":
                            tr.bombeturtle(i,k)
                        else:
                            tr.nombrebombestortue(i,k,GrilleNbr[i][k])
                        
            print("___________/|\n (__|||__) \| Bravo ! Vous avez gagné ! \n Merci d'avoir joué !")
    # - - -
    if flag_turtle == True:
        tr.discworld.reset()

    # - - - Replay - - -
    replay = False
    while replay == False:
        rejouer=input('Pour rejouer, entrez "r". Pour quitter le programme, entrez "q".')
        if rejouer == "r":
            replay = True
        if rejouer == "q":
            replay = True
            flag_jeu = True
    