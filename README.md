# Demineur
Le meilleur démineur en python, dévelopé avec amour par Ardi Cerkini et Cédric Brunner.

## Comment jouer ?
Téléchargez les fichiers turtlelib.py et demineur.py, et mettez dans le même dossier.

Lancez le fichier demineur.py.

>python ./demineur.py

Choisissez si vous souhaitez avoir l'interface graphique. Ensuite, choisissez le nombres de lignes, de colonnes et de bombes que vous souhaitez.
Voici plusieurs difficultés possibles.

>**Facile**: 10 lignes, 10 colonnes et 20 bombes.
>
>**Moyen**: 20 lignes, 20 colonnes et 40 bombes.
>
>**Difficile**: 50 lignes, 50 colonnes et 100 bombes.

Ensuite, vous pouvez explorer chaque case suivant comment vous voulez les manipuler.

Voici les mouvements possibles:

>**M, Marcher:**
>Permet de libérer une case. Attention, si vous marcher sur une bombe, c'est Game Over !

>**F, Drapeau:**
>Permet de signaler une case comme étant minée. Pour enlever un drapeau, refaites l'action "Drapeau" sur la case déjà signalée.

>**?, Interrogation**
>Si vous n'êtes pas sûr s'il s'agit d'une bombe ou pas. Pour enlever l'interrogation, refaites l'action "?" sur la case signalée.


Le jeu se termine lorsque toutes les mines sont marquées, ou lorsque vous marchez sur une bombe. Bonne chance !

## Exigences techniques
Vous avez besoin du package Turtle, ainsi que d'un ordinateur.

