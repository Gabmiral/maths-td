#!/usr/bin/env python3

def definenumbers():
	global xA, yA, xB, yB, xC, yC, xD, yD
	xA = int(input("Quelle est l'abscisse de A ?\n"))
	yA = int(input("Quelle est l'ordonnée de A ?\n"))
	xB = int(input("Quelle est l'abscisse de B ?\n"))
	yB = int(input("Quelle est l'ordonnée de B ?\n"))
	xC = int(input("Quelle est l'abscisse de C ?\n"))
	yC = int(input("Quelle est l'ordonnée de C ?\n"))
	xD = int(input("Quelle est l'abscisse de D ?\n"))
	yD = int(input("Quelle est l'ordonnée de D ?\n"))

def testparall():
	if ((xB - xA) == (xC - xD)) and ((yB - yA) == (yC - yD)):
		return 0
	else:
		return 1

"""
RESULTATS
pour A(2;3); B(-2;6); C(3;4) et D(7;1) : Parallélogramme
pour A(1;1); B(4;2); C(8;-2) et D(5;-1) : Pas un parallélogramme
"""

def testquadri():
	test = testparall()
	if test == 0:
		AB = (xB - xA)**2 + (yB - yA)**2
		BC = (xC - xB)**2 + (yC - yB)**2
		if AB == BC:
			BD = (xB - xD)**2 + (yB - yD)**2
			AC = (xA - xC)**2 + (yA - yC)**2
			if BD == AC:
				print("Ce quadrilatère est un carré")
			else:
				print("Ce quadrilatère est un losange")
		else:
			BD = (xB - xD)**2 + (yB - yD)**2
			AC = (xA - xC)**2 + (yA - yC)**2
			if BD == AC:
				print("Ce quadrilatère est un rectangle")
			else:
				print("Ce quadrilatère est un parallélogramme")
	else:
		print("Ce quadrilatère est un quadrilatère quelconque")

"""
pour A(1;10); C(-1;4); B(-3;8) et D(3;6) : 1, 10, -3, 8, -1, 4, 3, 6 carré
pour A(-2;1); C(2;13); B(-3;8) et D(3;6) : -2, 1, -3, 8, 2, 13, 3, 6 losange
pour A(-1;10); C(1;4); B(-3;8) et D(3;6) : -1, 10, -3, 8, 1, 4, 3, 6 rectangle
pour A(2;3); C(-2;6); B(3;4) et D(7;1) : 2, 3, 3, 4, -2, 6, 7, 1 quelconque
pour A(1;1); C(4;2); B(8;-2) et D(5;-1) : 1, 1, 8, -2, 4, 2, 5, -1 quelconque
"""

def start():
	test = int(input("Que voulez vous tester ?\n1. Un parallélogramme\n2. Le type de quadrilatère\n3. Quitter le programme\n(rentrez le numéro de votre sélecton)\n"))
	if test == 1:
		definenumbers()
		output = testparall()
		if output == 0:
			print("ABCD est un parallélogramme")
		else:
			print("ABCD n'est pas un parallélogramme")
		input("Appuyez sur la touche \"Entrée\" pour continuer")
		start()
	elif test == 2:
		definenumbers()
		testquadri()
		input("Appuyez sur la touche \"Entrée\" pour continuer\n")
		start()
	elif test == 3:
		print("Fermeture du programme ...")
		exit()

start()
