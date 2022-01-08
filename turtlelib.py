import turtle
discworld = turtle.Screen() #ecran
discworld.reset()
turtle.reset()
ATuin = turtle.Turtle()
ATuin.speed(0)
ATuin.shape("turtle")

ATuin.fillcolor("gray")
for i in range(nLignes):
    for k in range(nColonnes):
        ATuin.up() #évite de dessinner les déplacements
        ATuin.goto(50*i,-50*k) #fait aller la tortue à la position de la case
        ATuin.down() #commence à dessiner
        ATuin.begin_fill() #commence le remplissage des cases
        for x in range(4): # boucle qui dessine un carré
            ATuin.forward(40)
            ATuin.right(90)
        ATuin.end_fill() #termine le remplissage des cases

for i in range(len(mg)): # dessine les chiffres des colonnes
    ATuin.up()
    ATuin.goto(50*i+10,7)
    ATuin.down()
    ATuin.write(str(i), font=("Arial", 30, "normal"))
for k in range(len(mg[0])): # dessine les chiffres des lignes
    ATuin.up()
    ATuin.goto(-40,-50*k-43)
    ATuin.down()
    ATuin.write(str(k), font=("Arial", 30, "normal"))
    
def pointinterrogationtortue(y,x):
    """
    Prend des coordonnées en paramètre et dessine un point d'interrogation, refait la case avant pour être sûr qu'elle ne comporte pas déja un signe
    """
    ATuin.fillcolor("gray")
    ATuin.up() #évite de dessinner les déplacements
    ATuin.goto(50*x,-50*y) #fait aller la tortue à la position de la case
    ATuin.down() #commence à dessiner
    ATuin.begin_fill() #commence le remplissage des cases
    for z in range(4): # boucle qui dessine un carré
        ATuin.forward(40)
        ATuin.right(90)
    ATuin.end_fill() #termine le remplissage des cases

    ATuin.pencolor("red") # dessine le point d'interrogation
    ATuin.up()
    ATuin.goto(50*x+10,-50*y-43)
    ATuin.down()
    ATuin.write("?", font=("Arial", 30, "normal"))
    ATuin.pencolor("black")
    
def drapeautortue(y,x):
    """
    Prend des coordonnées en paramètre et dessine un drapeau, refait la case avant pour être sûr qu'elle ne comporte pas déja un signe
    """
    ATuin.fillcolor("gray")
    ATuin.up() #évite de dessinner les déplacements
    ATuin.goto(50*x,-50*y) #fait aller la tortue à la position de la case
    ATuin.down() #commence à dessiner
    ATuin.begin_fill() #commence le remplissage des cases
    for z in range(4): # boucle qui dessine un carré
        ATuin.forward(40)
        ATuin.right(90)
    ATuin.end_fill() #termine le remplissage des cases
    ATuin.fillcolor("red") #dessine un drapeau
    ATuin.up()
    ATuin.goto(50*x+20,-50*y-35)
    ATuin.down()
    ATuin.left(90)
    ATuin.forward(30)
    ATuin.begin_fill()
    ATuin.left(120)
    ATuin.forward(15)
    ATuin.left(120)
    ATuin.forward(15)
    ATuin.left(30)
    ATuin.end_fill()
    
def nombrebombestortue(y,x,nombre):
    """
    Prend des coordonnées et un nombre en paramètre et dessine un point ce chiffre, fait une case avec un remplissage blanc
    """
    ATuin.fillcolor("white")
    ATuin.up() #évite de dessinner les déplacements
    ATuin.goto(50*x,-50*y) #fait aller la tortue à la position de la case
    ATuin.down() #commence à dessiner
    ATuin.begin_fill() #commence le remplissage des cases
    for z in range(4): # boucle qui dessine un carré
        ATuin.forward(40)
        ATuin.right(90)
    ATuin.end_fill() #termine le remplissage des cases
    if nombre != 0: #si le nombre de bombes est différent de 0, dessine ce nombre
        ATuin.pencolor("blue")
        ATuin.up()
        ATuin.goto(50*x+10,-50*y-43)
        ATuin.down()
        ATuin.write(str(nombre), font=("Arial", 30, "normal"))
        ATuin.pencolor("black")
        
def casenormaleturtle(y,x):
    """
    Prend des coordonnées en paramètre et redessine la case en gris
    """
    ATuin.fillcolor("grey")
    ATuin.up() #évite de dessinner les déplacements
    ATuin.goto(50*x,-50*y) #fait aller la tortue à la position de la case
    ATuin.down() #commence à dessiner
    ATuin.begin_fill() #commence le remplissage des cases
    for z in range(4): # boucle qui dessine un carré
        ATuin.forward(40)
        ATuin.right(90)
    ATuin.end_fill() #termine le remplissage des cases