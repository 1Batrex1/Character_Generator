import Initialize
from os import getcwd

class Profession:

    def __init__(self, name, weapon_id_list, item_id_list,skills_id_list,talents_id_list):
        self.name = name #Nazwa;
        self.item_id = item_id_list # 3,6,8;
        self.weapon_id = weapon_id_list #3,4,6;
        self.skills_id = skills_id_list # 3,6,8;
        self.talents_id = talents_id_list#3,5,6;

        itemstemp = Initialize.load_items("Items.txt")
        weaponstemp = Initialize.load_weapons("Weapons.txt")
        skillstemp = Initialize.load_skills("Skills.txt")
        talentstemp = Initialize.load_talents("Talents.txt")

        self.items = []
        self.weapons = []
        self.skills = []
        self.talents = []

        for x in self.item_id:
            self.items.append(itemstemp[x])

        for x in self.weapon_id:
            self.weapons.append(weaponstemp[x])

        for x in self.skills_id:
            self.skills.append(skillstemp[x])

        for x in self.talents_id:
            self.talents.append(talentstemp[x])



def lista_profesji(filename = getcwd()+"/Warhammer/Professions.txt"):
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



