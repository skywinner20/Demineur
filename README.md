# Demineur
Le meilleur démineur en python, dévelopé avec amour par Ardi Cerkini et Cédric Brunner. Il a été développé comme projet scolaire, afin d'apprendre le langage Python.

## Comment jouer ?
Téléchargez les fichiers turtlelib.py et demineur.py, et mettez-les dans le même dossier.

Lancez le fichier demineur.py.

>python ./demineur.py

Choisissez si vous souhaitez avoir l'interface graphique. Ensuite, choisissez le nombres de lignes, de colonnes et de bombes que vous souhaitez.
Vous pouvez choisir les nombres que vous voulez, mais, pour vous guider, voici plusieurs difficultés possibles. Le maximum est 70 lignes, 70 colonnes et 2450 bombes. Cependant, nous ne vous conseillons pas cette configuration.

>**Facile**: 5 lignes, 5 colonnes et 5 bombes.
>
>**Moyen**: 10 lignes, 10 colonnes et 20 bombes.
>
>**Difficile**: 15 lignes, 15 colonnes et 50 bombes.

Ensuite, vous pouvez explorer chaque case suivant comment vous voulez les manipuler.

Voici les mouvements possibles:

>**M, Marcher:**
>Permet de libérer une case. Attention, si vous marcher sur une bombe, c'est Game Over !

>**F, Drapeau:**
>Permet de signaler une case comme étant minée. Pour enlever un drapeau, refaites l'action "Drapeau" sur la case déjà signalée.

>**?, Interrogation:**
>Si vous n'êtes pas sûr s'il s'agit d'une bombe ou pas. Pour enlever l'interrogation, refaites l'action "?" sur la case signalée.


Le jeu se termine lorsque toutes les mines sont marquées, ou lorsque vous marchez sur une bombe. Bonne chance !

## Exigences techniques
Vous avez besoin de Python 3, du package Turtle, ainsi que d'un ordinateur.

