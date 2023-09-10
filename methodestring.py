#.strip() :c'est une methode qui permet d'effacer les espaces dans les cas des login et mot de passe ,
# .len() : c'est une fonction qui permet de savoir la longueur d'une liste ou chaine de caractere ....,
# .lower() , .upper() : sont des methodes qui permet de mettre en majuscule et minuscule les lettre dans un string  ,
# .split() : c'est une methode qui est utilise ciomme un separateur qui stock dans une liste les chaines de caracteres
# Une fonction peut etre appeler a n'importe momentet pas a la suite d'un string par contre une methode c'est quelque chose qu'on va pouvoir appeler a la suite d'string
text = ' chIEn chat loud lion '
print(text)
print(text.strip())

print(len(text))
print(text.lower())
print(text.upper())


if 'chien'== 'CHien'.lower(): # python est sensible a la casse
    print('oui')
print(text.split()) 