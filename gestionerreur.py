"""
ageutilisateur= input("entrer votre age : ")
try:
    ageutilisateur=int(ageutilisateur)
except:
       print("L'age indiquer est incorret")
else:     
      print("Tu as ", ageutilisateur, "ans")
finally:
      print("Fin du programme !")      
"""

# try/except (else/finally)
# types d'exceptions on a : ValueError, zeroDivisionError, NameError, AssertionError, OsError, typeErro
"""
nbr1=150
nbr2=input("entrer un nbr : ")
try:
    nbr2=int(nbr2)
    print("le resultat, {}".format(nbr1/nbr2))
except ZeroDivisionError:
    print("on ne peut pas diviser un nbr par 0")
except ValueError:
    print("valeur incorrect")
except:
    print(" ce que vous avez enter est incorrect")
else: 
    print("tu as indiqué un nbr valide")    
finally:
    print('Fin du programme !')            

"""


try:
    age=input('enter voter age : ')
    age=int(age)
    assert age > 25 # je veux que l'age soit superieur a 25 sinon tu leve une assertion error
except AssertionError:
    print("j'ai attrappé l'assertion")
        