from robot import *
for i in range(25):
    if obstacleDroite():
        if obstacleHaut():
            bas()
        else:
            haut()
    else:
        droite()
