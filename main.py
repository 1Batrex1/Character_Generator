import Warhammer.Initialize
from Warhammer import *

lista = Warhammer.Initialize.load_weapons("D:\Studia\Programowanie\Python\Character_Generator\Warhammer\Weapons.txt")

hero = Warhammer.Hero.Hero("Bartek", "Elf", "Szlachcic", "Mężczyzna", "Cos", "Cos", "Cos", lista[0], lista[1])

print(hero)
