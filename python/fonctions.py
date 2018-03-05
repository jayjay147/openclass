# Apprentissage fonctions - reprise exercice sur la table de multiplication

# calculer la table de multiplication



def table(nb): # Création fonction
	i = 0 # variable compteur incrémentation dans le calcul
	#boucle
	while i < 10:
		print(i + 1, "x", nb, "=", (i + 1) * nb)
		i += 1 # on incremente de 1 à chaque tour de la boucle.
