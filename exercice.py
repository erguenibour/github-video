import random 

prix= random.randint(1,10)
prixdevin = input(" deviner le prix: ")
while int(prixdevin)!=prix:
    if int(prixdevin)<prix:
        prixdevin = input(" c'est plus entre une nouvelle valeur: ")
    elif int(prixdevin)>prix:
        prixdevin = input(" c'est moins entre une nouvelle valeur: ")    
        break
print("bravo tu as trouve le prix ", prixdevin)