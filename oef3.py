import random

#loop over alle nummers dat je ingeeft als user
def kipOfEi():
	userGuess = str(input("Raad het juiste getal"))
	kip = 0
	kipei = 0

# 4 getallen opgeven e raden wat juist is
	for i in range(4):
		if num[i] == userGuess[i]:
			kip += 1

# check of het opgegeven cijfer op de juiste plaats staat er het juiste cijfer
	for i in num:
		if i in userGuess:
			kipei += 1

# kijken of het cijfer overeenkomt 
	ei = kipei - kip

	print("{} kippen, {} eieren".format(kip,ei))

	return kip

# play the game 
if __name__== '__main__': 
	num = str(random.randrange(1000,10000))
	# als test gelogd om de werking te checken
	print(num)
	print("LINGO-BINGO: Welkom bij het kip en eieren spel")
	print("Geef een viercijferig getal in")
	kip = 0
	count = 0
	while kip != 4:
		count += 1
		kip = kipOfEi()

	print("Je had {} pogingen nodig".format(count))