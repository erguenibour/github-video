jeu_lancer= True
print("")
while jeu_lancer: # faire les instructions en rapport avec le jeu
    choixmenu = input("> ")
    if choixmenu == "again":
        continue
    elif choixmenu == "quit":
        break
    elif choixmenu =="hello":
        print("Bonjour :) !")
    else:
        print("commande introuvable ")
print("A Bientot ....")            