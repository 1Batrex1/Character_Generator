from Warhammer.money import *
from Warhammer.CharacterDescription import *
from Warhammer.specialTraits import *


class hero:
    class Skill:
        def __init__(self, n, s1, s2):
            self.name = n  # nazwa skila
            self.spec1 = s1  # czy specjalizacja +10%
            self.spec2 = s1  # czy specjalizacja +10%

        def GetSkill(self):
            return self.name + self.spec1 + self.spec2

    class Talents:
        def __init__(self, n, desc):
            self.name = n  # nazwa talenty
            self.description = desc  # opis umiejętności

        def GetTalent(self):
            return self.name + self.description

    def __init__(self, name, race, profesion, gender, Ski, Tal, Eq, *Wep):
        self.name = name
        self.race = race
        self.profession = profesion
        self.Chad = CharacterDescription(gender, self.race)
        self.st = SpecialTraits(self.race)
        self.wep = []  # Tabela Broni
        self.Ski = []  # Tabela skili
        self.Tal = []  # Tabela Talentów
        self.Eq = []  # Tabela eq
        self.Money = money()
        for x in Wep:
            self.wep.append(x)
