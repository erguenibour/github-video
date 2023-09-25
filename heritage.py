#classe mère
class vehicule:
    def __init__(self,nom_vehicule,quantite_essence):
        self.nom = nom_vehicule 
        self.essance = quantite_essence


    def se_deplacer(self):
        print("le vehicule {} se deplace".format(self.nom))   


#classe fille    
class voiture(vehicule):        
    def __init__(self, nom_voiture, essence, puissance):
        vehicule.__init__(self,nom_voiture, essence)
        self.puissance = puissance
    def se_deplacer(self):
        print("je roule")       


class Avion(vehicule):
    def __init__(self, nom, essence, marchandise):
        vehicule.__init__(self,nom, essence)
        self.marchandise= marchandise  
    def se_deplacer(self):
        print("je survole")       
     

#programme principal               
voiture1  = voiture("toyota",90,420)  
voiture1.se_deplacer()
print(voiture1.puissance, "ch")   
av1 = Avion("F23 raptor", 240, "missiles")
av1.se_deplacer()  
print(isinstance(av1, vehicule)) #isinstance(<objet>,<class>: verifie si l'objet est de la classe rendeigner) 
if isinstance(av1, vehicule):
    print("av1 est un vehicule")
if issubclass(Avion, vehicule):
    print("avion herite de vehicule")    
