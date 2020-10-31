from robot import *
for i in range(4):
    for k in range(9):
        if surCaseMarquee():
            deposerPlot()
        if plotDevant():
            tournerDroite()
            avancer()
            tournerGauche()
            avancer()
            tournerGauche()
            if plotDevant():
                tournerDroite()
                avancer()
                tournerGauche()
            avancer()
            tournerDroite()
        else:
            avancer()
    tournerGauche()
    avancer()
    tournerGauche()
    for k in range(10):
        avancer()
    tournerDroite()
    avancer()
    tournerDroite()
