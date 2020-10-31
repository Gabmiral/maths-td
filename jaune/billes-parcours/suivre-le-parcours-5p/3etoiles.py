from robot import *
for i in range(24):
    if obstacleDroite():
        haut()
    else:
        droite()
