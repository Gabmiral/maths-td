#!/usr/bin/env python3
import random

def partie():
    N = 0
    output = 0
    while N < 6:
        diceroll = random.randint(1,6) # jai nommé la var "dé" en "diceroll" pour ne pas avoir d'accents ou de variable en 2 lettres
        print(diceroll, N)
        if diceroll == 6:
            output = 1
            break
        N+=1
    if output == 1:
        print("Le lièvre a gagné")
    else:
        print("La tortue a gagnée")

def test(nombre): # la fonction de test que j'ai créé pour l'ex 1. Bien qu'elle fasse la meme chose que la fonction exercice3(), elle n'a pas tous les élements demandés par le professeur
    score = 0
    for i in range(nombre):
        N = 0
        output = 0
        while N < 6:
            diceroll = random.randint(1,6)
            if diceroll == 6:
                output = 1
                break
            N+=1
        score += output
    print(score)

"""
1. Le lièvre semble avoir l'avantage : sur 10 millions d'essais, il a gagné 6650535 parties, soit 66.5%.

2. https://github.com/gabmiral/maths-td/livretortue/arbredespossibles.png
"""

def exercice3(nombre):
    L = 0
    T = 0
    for i in range(nombre):
        N = 0
        output = 0
        while N < 6:
            diceroll = random.randint(1,6)
            if diceroll == 6:
                output = 1
                break
            N+=1
        if output == 1:
            L += 1
        else :
            T += 1
    print("Sur " + str(nombre) + " parties, le lièvre a gagné " + str(L) + " fois et la tortue a gagnée " + str(T) + " fois.") # La loi des grands nombres est validée