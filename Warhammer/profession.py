import Warhammer.Initialize as Initialize
from os import getcwd


class Profession:

    def __init__(self, name, weapon_id_list, item_id_list, skills_id_list, talents_id_list):
        self.name = name  # Nazwa;
        self.item_id = item_id_list  # 3,6,8;
        self.weapon_id = weapon_id_list  # 3,4,6;
        self.skills_id = skills_id_list  # 3,6,8;
        self.talents_id = talents_id_list  # 3,5,6;

        itemstemp = Initialize.load_items()
        weaponstemp = Initialize.load_weapons()
        skillstemp = Initialize.load_skills()
        talentstemp = Initialize.load_talents()

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


