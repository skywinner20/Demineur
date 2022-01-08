# --- Ardi et Cédric ---
# Bienvenue dans le futur jeu vidéo du siècle, litéralement le GOTY 2022, on a déjà été contacté par EA, Sony, Microsoft et Microids Studios
#TODO: - Le Gameover, l'intégration de turtle


import random #Grande liste des imports
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
    affichage_col = "- "
    for i in range(nbcol):
        affichage_col += " {0} ".format(i)
    print(affichage_col)
    for i in range(nbligne):
        lignetexte = "|"
        for j in range(nbcol):
            lignetexte += "{0} |".format(magrille[i][j])
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
                try:
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
            print("Erreur: Nombre de paramètres faux") 

        try: #Bien des valeurs
            l_user = int(l_user)
            c_user = int(c_user)
            flag_nbr_mem = True
        except ValueError:
            print("Erreur: Nombre(s) incorrecte(s)")

        #if l_user.isdigit == True and c_user.isdigit == True: #Verif de nombres l et c légal
        if flag_nbr_mem == True:
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
    FBomb si un f a été placé sur une bombe, n si une case intouchable est touchée
    """
    DeathBomb = False
    FBomb = False
    l_user = int(l_user)
    c_user = int(c_user)
    grille = grilleJoueur.copy()
    FlagDebug = False
    n = False
    try:
        if action == "m":

            if grille[l_user][c_user] != "□" or grille[l_user][c_user] == "f" or grille[l_user][c_user] == "?": #Case innouvrable
                n = True

            elif grillescore[l_user][c_user] == "B": # Bombe
                grille[l_user][c_user] == "B"
                DeathBomb = True

            elif grillescore[l_user][c_user] == 0: # Zéro

                grille[l_user][c_user] = int(grillescore[l_user][c_user]) #Remplacer la case
                if flag_turtle == True:
                    tr.nombrebombestortue(l_user,c_user,int(grillescore[l_user][c_user]))

                #Maintenant, il faut montrer les 8 voisins

                if (l_user - 1) >= 0 and (c_user - 1) >= 0: #En haut à gauche
                    grille[l_user - 1][c_user - 1] = int(grillescore[l_user - 1][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user - 1,int(grillescore[l_user - 1][c_user - 1]))

                if (l_user - 1) >= 0: #En haut au milieu
                    grille[l_user - 1][c_user] = int(grillescore[l_user - 1][c_user])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user,int(grillescore[l_user - 1][c_user]))

                if (l_user - 1) >= 0 and (c_user + 1) < len(grille[0]): #En haut à droite
                    grille[l_user - 1][c_user + 1] = int(grillescore[l_user - 1][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user - 1,c_user + 1,int(grillescore[l_user - 1][c_user + 1]))

                if (c_user - 1) >= 0: #Au milieu à gauche
                    grille[l_user][c_user - 1] = int(grillescore[l_user][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user - 1,int(grillescore[l_user][c_user - 1]))
                
                if (c_user + 1) < len(grille[0]): #Au milieu à droite
                    grille[l_user][c_user + 1] = int(grillescore[l_user][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user + 1,int(grillescore[l_user][c_user + 1]))
                
                if (l_user + 1) < len(grille) and 0 <= (c_user - 1) < len(grille[0]): #En bas à gauche
                    grille[l_user + 1][c_user - 1] = int(grillescore[l_user + 1][c_user - 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user - 1,int(grillescore[l_user + 1][c_user - 1]))
                
                if (l_user + 1) < len(grille): #En bas au milieu
                    grille[l_user + 1][c_user] = int(grillescore[l_user + 1][c_user])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user,int(grillescore[l_user + 1][c_user]))
                
                if (l_user + 1) < len(grille) and (c_user + 1) < len(grille[0]): #En bas à droite
                    grille[l_user + 1][c_user + 1] = int(grillescore[l_user + 1][c_user + 1])
                    if flag_turtle == True:
                        tr.nombrebombestortue(l_user + 1,c_user + 1,int(grillescore[l_user + 1][c_user + 1]))
            
            else: #le reste 
                grille[l_user][c_user] = int(grillescore[l_user][c_user])
                if flag_turtle == True:
                        tr.nombrebombestortue(l_user,c_user,int(grillescore[l_user][c_user]))
        
        elif action == "f": #Drapeau
            
            if grille[l_user][c_user] == "f": #Pour enlever le drapeau
                #if grillescore[l_user][c_user] == "B": #Enlever le drapeau = décès. Ce jeu a pour but de ressembler à un simulateur réaliste de guerre.
                #    DeathBomb = True
                grille[l_user][c_user] = "□"
                if flag_turtle == True:
                        tr.casenormaleturtle(l_user,c_user)
            
            elif grillescore[l_user][c_user] == "B": #Si drapeau sur bombe
                FBomb = True
                grille[l_user][c_user] = "f"
                if flag_turtle == True:
                        tr.drapeautortue(l_user,c_user)
                
            else:
                grille[l_user][c_user] = "f"
                if flag_turtle == True:
                        tr.drapeautortue(l_user,c_user)

            
    
        elif action == "?":
            if grille[l_user][c_user] == "?":
                grille[l_user][c_user] = "□"
                if flag_turtle == True:
                        tr.casenormaleturtle(l_user,c_user)
                        
            else:
                grille[l_user][c_user] = "?"
                if flag_turtle == True:
                        tr.pointinterrogationtortue(l_user,c_user)

        elif action == "DEBUG":
            FlagDebug = True
            if grillescore[l_user][c_user] == "B": #Si drapeau sur bombe
                FBomb = True
                grille[l_user][c_user] = "f"
            else:
                grille[l_user][c_user] = "f"

            if grille[l_user][c_user] == "f": #Pour enlever le drapeau
                #if grillescore[l_user][c_user] == "B": #Enlever le drapeau = décès. Ce jeu a pour but de ressembler à un simulateur réaliste de guerre.
                #    DeathBomb = True
                grille[l_user][c_user] = "□"

        
        
        elif action == "DEBUG":
            FlagDebug = True
    except IndexError:
        print("Erreur: Case en dehors de la grille.")

    return grille, DeathBomb, FBomb, FlagDebug, n

def DebutGame():
    """
    Fait débuter la partie. Demande au user le nbr de lignes, colonnes et bombes, et retourne les valeurs lignes, colonnes et bombes
    """
    print("     ,--.!,\n  __/   -*-\n,d08b.  '|`\n0088MM\n`9MMP'   Démineur - Ardi et Cédric")
    print("Bienvenue dans le futur du Gaming et du divertissement, vous allez adorer ! Je ne vais pas vous faire l'affront de vous expliquer comment jouer.")

    flag_a = False
    flag_b = False
    flag_c = False
    flag_d = False
    flag_turtle = False

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
    
    while flag_a == False:
        try: #Lignes
            a = input("Combien de lignes voulez-vous ? (Facile: 10, Moyen: 20, Difficile: 50): ")

            if int(a) >= 5 and int(a) <= 70:
                a = int(a)
                flag_a = True
            else:
                print("Erreur: Nombres de lignes incorrectes")

        except ValueError:
            print("Erreur: Nombres de lignes incorrectes")
        
    while flag_b == False:
        try: #Colonnes
            b = input("Combien de colonnes voulez-vous ? (Facile: 10, Moyen: 20, Difficile: 50): ")

            if int(b) >= 5 and int(b) <= 70:
                b = int(b)
                flag_b = True
            else:
                print("Erreur: Nombres de colonnes incorrectes")

        except ValueError:
            print("Erreur: Nombres de colonnes incorrectes")
        
    while flag_c == False:
        try:
            c = input("Combien de bombes voulez-vous ? (Facile: 20, Moyen: 40, Difficile: 100): ")

            if int(c) <= (int(a)*int(b))/2 and int(c) >= 5:
                c = int(c)
                flag_c = True
            else:
                print("Erreur: Nombre de bombes incorrectes")
        
        except ValueError:
            print("Erreur: Nombre de bombes incorrectes")
        
    return a, b, c, flag_turtle

# - - - - - FIN DES FONCTIONS, MAINTENANT CA DEVIENT RÉEL - - - - - -

# - Début de l'EXPERIENCE
flag_jeu = False
while flag_jeu == False:
    nLignes, nColonnes, nBomb, flag_turtle = DebutGame()
    nLignes, nColonnes, nBomb = int(nLignes), int(nColonnes), int(nBomb)
    GrilleNbr = GrilleScore(putBomb(magrille(nLignes, nColonnes), nBomb)) #Génération de la grille avc toutes les infos

    GrilleJoueur = grille_cachee(GrilleNbr)

    flag_compteur_juste = 0
    TouchBomb = False

    printGrille(GrilleJoueur)

    if flag_turtle == True:
        import turtlelib as tr
        tr.grilleturtle(nLignes,nColonnes)

    while flag_compteur_juste < nBomb and TouchBomb == False: # Le JEU
        l_user, c_user, action_user = user_inter(GrilleNbr)
        grilleJoueur, TouchBomb, FlagBomb, FlagDebug, FlagNon = gameplay(l_user, c_user, action_user, GrilleJoueur, GrilleNbr)
        if FlagDebug == True:
            printGrille(GrilleNbr)
        if FlagBomb == True:
            flag_compteur_juste += 1
        if FlagNon == True:
            print("Case intouchable !")
        printGrille(GrilleJoueur)
        if TouchBomb == True:
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
        if flag_compteur_juste == nBomb:
            printGrille(GrilleNbr)
            if flag_turtle == True:
                for i in range(len(GrilleNbr)):
                    for k in range(len(GrilleNbr[i])):
                        if GrilleNbr[i][k] == "B":
                            tr.bombeturtle(i,k)
                        else:
                            tr.nombrebombestortue(i,k,GrilleNbr[i][k])
                        
            print("___________/|\n (__|||__) \| Bravo ! Vous avez gagné ! \n Merci d'avoir joué !")

    replay = False
    while replay == False:
        rejouer=input('Pour rejouer, apuyez sur "r", pour quitter le programme appuyez sur "q"')
        if rejouer == "r":
            replay = True
        if rejouer == "q":
            replay = True
            flag_jeu = True
    