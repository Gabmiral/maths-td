from robot import *
avancer()
if plotDevant():
    tournerGauche()
    avancer()
    tournerDroite()
    avancer()
else:
    avancer()
    deposerPlot()
    tournerGauche()
    avancer()
    tournerDroite()
for i in range(6):
    avancer()
if surCaseMarquee():
    deposerPlot()
avancer()
tournerDroite()
avancer()
if surCaseMarquee():
    deposerPlot()
