# -*-coding:utf-8 -*

# Apprentissage fonctions - reprise exercice sur la table de multiplication

# calculer la table de multiplication



def table(nb): # Cr�ation fonction
	i = 0 # variable compteur incr�mentation dans le calcul
	#boucle
	while i < 10:
		print(i + 1, "x", nb, "=", (i + 1) * nb)
		i += 1 # on incremente de 1 � chaque tour de la boucle.
