# -*-coding:utf-8 -*

# Programme roulette simplifié

import os
from random import randrange # fonction tirer nb aléatoire
from math import ceil # fonction Arrondir au supérieur

# Définir les variables

bankroll = 500 # Bankroll de départ
next_game = True 

print("Bienvenue, votre bankroll est de", bankroll, "$.")

while next_game:

# choix du chiffre où l'on mise

	num_mise = -1
	while num_mise < 0 or num_mise > 49:
		num_mise = input("Saisir le numéro choisi entre 0 et 49 : ")
		num_mise = int(num_mise) # on veut que choix mise soit une valeur entière
		
		if num_mise < 0 or num_mise > 49:
			print("Le nombre saisi n'est pas valide")

# Choix montant de la mise

	mise = 0
	while mise <= 0 or mise > bankroll:
		mise = input("Faites vos jeux, combien de $ voulez-vous miser : ")
		mise = int(mise) # on veut que la mise soit un nombre entier
	
		if mise <= 0:
			print("la saisie est incorrecte.")
		if mise > bankroll:
			print("Vous n'avez pas assez de $$$.")

# tirage

	num_win = randrange(50)
	print("Rien ne va plus..., la bille s'arrête sur le numéro : ", num_win)

# Vérification bon numéro :

	if num_mise == num_win: # cas où le numéro gagnant est trouvé
		print("Bravo, vous avez gagné : ", mise * 3, "$")
		bankroll += mise * 3

	else:
		print("Désolé, vous avez perdu.")
		bankroll -= mise # incrémentation bankroll - la mise

# Mise à jour bankroll

	if bankroll <=0:
		print("Vous avez perdu. Vous n'avez plus de $$$. La partie est terminée.")
		next_game = False #si la BR est à 0, alors game over
	else:
		print("Votre bankroll est maintenant de : ", bankroll, "$")
		print("Le jeu reprend dans quelques instants...")
	
os.system("pause")
	
	
