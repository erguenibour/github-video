#liste[x] = affiche element d'indice x
#liste[-x] = affiche  xème element en partant de la fin
#liste[:] = affiche tous les elements 
#liste[x:] = affiche les x elements derniers
#liste[:x] = affiche les x elements premiers
#liste[A:B] = affiche de l'element d'indice Aa l'element indice B exclus
 
#creation d'une liste

inventaire= range(20)
i=0
while i < len(inventaire):
    print(inventaire[i])
    i+=1
for valeur in inventaire:
    print(valeur)    

inven=["moi", "yoi", "toi", "mpo"]
print(inven[:])
inven.append("erc")    
print(inven[:])
inven.insert(1, "posi")
print(inven[:])
del inven[1]
print(inven[:])
objet_sup=inven.remove("toi")
print(inven[:])  
inven.sort()
print(inven[:])
inv=[2,1,3,5,4,2,1,4,9,8,5]
inv.sort()
print(inv)
#help(list)
chaine="bonjour a tous"
chaine=chaine.split(" ")
print(chaine)

import copy


liste1=["un", "dre", "oid","oihhj"]
liste2=["uio", "hgfh", "lloo"]
liste2=copy.deepcopy(liste1)

print(liste1[:])
print(liste2[:])

liste1.extend(liste2)
liste1+=liste2

print(liste1[:])
print(liste2[:])


