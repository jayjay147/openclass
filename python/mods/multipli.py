# -*-coding:Latin-1 -*

"""module multipli contenant la fonction table"""

nb = input("Saisir la table de multiplication choisie : ")
nb = int(nb)

max = input("Saisir le max : ")
max = int(max)

def table(nb, max):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1