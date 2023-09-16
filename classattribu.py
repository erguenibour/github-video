#class : un plan de conception (ex: Humain)
#objet : instance de classe (ex: julien)
#Attribu : variable de classe (ex : nom, prenom, age, sexe)
#Proprieté : manière de manipuler des attribus
#Methode : fonction d'une classe (ex: manger, dormir, dancer, marcher, mourir)
#Methode de classe : foction de classe 
#Methode statique : fonction d'une classe mais independante de celle-ci
#Héritage : classe fille qui hérite d'une classe mère (fille est une sorte de mère) ex: classe chat hérite de la classe animal
class Humain:
    def __init__(self, c_prenom, c_age=1):
        print("creation d'un humain")
        self.prenom=c_prenom
        self.age=c_age
print("lancement du programme ...") 
h1=Humain("jojo") 
print("prenom de h1 : {}".format(h1.prenom))
print("l'age de h1 : {}".format(h1.age))
h2=Humain("Albert", 17)
print("prenom de h2 : {}".format(h2.prenom))
print("l'age de h2 : {}".format(h2.age)) 