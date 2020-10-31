from robot import *
while not bordGrilleDroite():
    droite()
    while surBille():
        ramasserBille()
gauche()
while not surTrou():
    haut()
deposerBille()
