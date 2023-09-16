class Humain:
    lieu_habitation= "Terre"  #attribu de classe
    def __init__(self, nom, age):
        self.nom=nom
        self.age=age
    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))

    def changer_planete(cls, nouvelle_planete): # cls= methode de classe
        Humain.lieu_habitation= nouvelle_planete
    changer_planete= classmethod(changer_planete)
    def definition():
        print("L'Humain est le plus haut etre vivant dans la chaine alimentaire")
    definition=staticmethod(definition) 
Humain.definition()               

#programme principal
h1=Humain("jakson", 27) 
print("planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("planète actuelle : {}".format(Humain.lieu_habitation))


          
        