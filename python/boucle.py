# calculer la table de multiplication par 7

nb = input("Merci de saisir par un chiffre, la table de multiplication que vous voulez calculer : ")
# formulaire 
nb = int(nb) # variable en nombre entier

i = 0 # variable compteur qui incrémentera dans le calcul

while i < 10: # tant que i est strictement inférieur à 10
	print(i+1, "x", nb, "=", (i+1) * nb)
	i += 1 # on incrémente i de + 1 à chaque tour