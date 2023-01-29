from Warhammer.Weapon import Weapon
from Warhammer.Eq import Eq
from Warhammer.Skill import Skill
from Warhammer.Talent import Talent
from os import getcwd
def load_weapons(filename):
    weapons = []
    print()
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip('\t').split(';')
            w = Weapon(pola[0], pola[1], pola[2], pola[3], pola[4])
            weapons.append(w)

    return weapons


def load_items(filename):
    items = []

    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            it = Eq(pola[0], pola[1])
            items.append(it)
    return items


def load_skills(filename):
    skills = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            s = Skill(pola[0], pola[1], pola[2])
            skills.append(s)
    return skills


def load_talents(filename):
    talents = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            t = Talent(pola[0])
            talents.append(t)
    return talents
