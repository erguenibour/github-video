try:
    age=input(enter voter age : )
    age=int(age)
    assert age > 25 # je veux que l'age soit superieur a 25
except AssertionError:
    print("j'ai attrappé l'assertion")