from Warhammer import *

lista = Warhammer.Initialize.load_weapons()

hero = Warhammer.Hero.Hero("Bartek", "Niziołek", "Szlachcic", "Mężczyzna", "Cos", "Cos", "Cos", lista[0] , lista[1])

print(hero)
