"""Modes d'ouverture 
r (lecture seul)
w (ecriture avec remplacement)
a (ecriture avec ajout en fin de fichier)
x (lecture et ecriture)
r+(lectutre/ecriture dans un meme fichier)


lecture : read(), readline(), readlines()
"""
import pickle
class player:
    def __init__(self, name, level):
        self.name=name
        self.level=level
    def whoami(self):
        print("{} ({})".format(self.name, self.level))

      
with open("player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    p1=get_record.load()
p1.whoami()    
 #   nbr=1
  #  fic.write(str(nbr))
   # fic.write("\nbonjour je suisnunen phrase\n")
    #fic.write("\nbonjour je suisnunen phrase")

    #content = fic.read()
    #print(content)
#line = fic.readline()
#print(line)
#line = fic.readlines()
#print(line)
#fic.close()

#if fic.close:
    #print("fichier fermer")
#else:
    #print("fichier ouvert")    