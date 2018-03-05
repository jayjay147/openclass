# -*-coding:utf-8 -*

import os # importation module

annee = input("Saisir une année supérieur à 0 : ")

try: 
	annee = int(annee) # conversion de l'année
	# assert annee > 0
#except ValueError:
	#print("Vous n'avez pas saisi un nombre.")
#except AssertionError:
	#print("L'année saisie est inférieur ou égale à 0.")
	
	if annee <= 0:
		raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
		print("la valeur saisie est incorrecte. ")
	
os.system("pause") # La fenetre ne se ferme pas automatiquement. Permet de voir l'erreur.