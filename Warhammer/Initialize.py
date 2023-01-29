from Warhammer.Weapon import Weapon
from Warhammer.Eq import Eq
from Warhammer.Skill import Skill
from Warhammer.Talent import Talent
from Warhammer.profession import Profession
from os import getcwd


def load_weapons(filename=getcwd() + "/Warhammer/Weapons.txt"):
    weapons = []
    print()
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip('\t').split(';')
            w = Weapon(pola[0], pola[1], pola[2], pola[3], pola[4])
            weapons.append(w)

    return weapons


def load_items(filename=getcwd() + "/Warhammer/Items.txt"):
    items = []

    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            it = Eq(pola[0], pola[1])
            items.append(it)
    return items


def load_skills(filename=getcwd() + "/Warhammer/Skills.txt"):
    skills = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            s = Skill(pola[0], pola[1], pola[2])
            skills.append(s)
    return skills


def load_talents(filename=getcwd() + "/Warhammer/Talents.txt"):
    talents = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            t = Talent(pola[0])
            talents.append(t)
    return talents


def load_profession(filename=getcwd() + "/Warhammer/Professions.txt"):
    profession_list = []
    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip("\t").split(";")
            bronie = pola[1].strip(" ").split(",")
            itemy = pola[2].strip(" ").split(",")
            skille = pola[3].strip(" ").split(",")
            talenty = pola[4].strip(" ").split(",")

            for x in range(0, len(bronie)):
                bronie[x] = int(bronie[x])

            for x in range(0, len(itemy)):
                itemy[x] = int(itemy[x])

            for x in range(0, len(skille)):
                skille[x] = int(skille[x])

            for x in range(0, len(talenty)):
                talenty[x] = int(talenty[x])

            s = Profession(pola[0], bronie, itemy, skille, talenty)
            profession_list.append(s)
    return profession_list
