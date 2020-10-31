from robot import *
for i in range(10):
    avancer()
    tournerGauche()
    for k in range(7):
        if caisseDevant():
            pousserCaisse()
        else:
            avancer()
    tournerDroite()
    tournerDroite()
    for k in range(7):
        avancer()
    tournerGauche()
