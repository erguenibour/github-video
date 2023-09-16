def dire(nom="ali", message="hello"):
    print("{} : {}".format(nom , message))
dire("jean")    
dire("Tom","Salut" )

def show_inventory(*items):
    for item in items:
        print(item)
show_inventory("épée") 
show_inventory("épée","dragon rouge","cape","lasse")       

def comparer (nbr1,nbr2):
    if nbr1<nbr2:
        return nbr2
    elif nbr1>nbr2:
        return nbr1
    else:
        return "Egalité"
print(comparer(16,16))    