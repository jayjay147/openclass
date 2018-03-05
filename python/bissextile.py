# programme déterminant si une année est bissextile ou non

annee = input("Merci de saisir une année : ") # Saisie d'une année
annee = int(annee) # variable année en type entier et non chaines de caractères

bissextile = False

if annee % 400 == 0:
	bissextile = True
elif annee % 100 == 0:
	bissextile = False
elif annee % 4 == 0:
	bissextile = True

if bissextile:
	print("l\'année est bissextile")
else:
	print("l\'année n'est pas bissextile")

exit()
