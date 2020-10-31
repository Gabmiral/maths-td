from robot import *
for i in range(5):
    for i in range(7):
        pousserCaisse()
    tournerDroite()
    avancer()
    tournerDroite()
    for i in range(7):
        avancer()
    tournerGauche()
    avancer()
    tournerGauche()
for i in range(7):
    pousserCaisse()
