from Warhammer import *

lista = Warhammer.Initialize.load_weapons()

#for x in lista: tak można znaleźć coś w liście obiektów
#    if "Rapier" in x.name:
#        print(lista.index(x))

hero = Warhammer.Hero.Hero("Bartek", "Niziołek", "Szlachcic", "Mężczyzna", "Cos", "Cos", "Cos", lista[0] , lista[1])

print(hero)
