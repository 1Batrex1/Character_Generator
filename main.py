import Warhammer.odczyt
from Warhammer import *

lista = Warhammer.odczyt.wczytywanie("D:\Studia\Programowanie\Python\Character_Generator\Warhammer\Weapons.txt")

hero = Warhammer.Hero.hero("Bartek","Człowiek","Szlachcic","Mężczyzna","Cos","Cos","Cos",lista[0],lista[1])

for x in hero.wep:
        print(x)

print(hero.st)