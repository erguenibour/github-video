def ajoutdeux(x):
    return (x+2)**2
def retiredeux(y):
    return y-2
valeur1 = ajoutdeux(5)
valeur2 = retiredeux(3)
print(valeur1, valeur2)

def printstring(string):
    print(string)
printstring('coucou')    


import math
def hypotenus(a,b):
    hypotenus = math.sqrt(a*2+b*2)
    return hypotenus
print(hypotenus(1,2))