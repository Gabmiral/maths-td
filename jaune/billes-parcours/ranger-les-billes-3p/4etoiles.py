from robot import *
droite()
for i in range(5):
    haut()
    ramasserBille()
    for k in range(10):
        droite()
    deposerBille()
    for k in range(10):
        gauche()
