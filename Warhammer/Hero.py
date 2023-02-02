from Warhammer.Money import *
from Warhammer.CharacterDescription import *
from Warhammer.specialTraits import *


class Hero:

    def __init__(self, name, race, profession, gender, Ski, Tal, Eq, Wep):
        self.name = name
        self.race = race
        self.profession = profession
        self.Chad = CharacterDescription(gender, self.race)
        self.st = SpecialTraits(self.race)

        self.wep = Wep
        self.Ski = Ski  # Tabela skili
        self.Tal = Tal  # Tabela Talentów
        self.Eq = Eq  # Tabela eq
        self.Money = Money()

    def __str__(self):
        wep = ""
        for x in self.wep:
            wep += str(x)
        ski = ""
        for x in self.Ski:
            ski += str(x)
        tal = ""
        for x in self.Tal:
            tal = str(x)
        eq = ""
        for x in self.Eq:
            eq += str(x)+"\n"

        return "=====================\nBohater\n=====================\nImię:" + self.name + "\nRasa:" + \
            self.race + "\nProfesja:" + self.profession + \
            "\n=====================\nOpis Bohatera\n=====================\n" + self.Chad.__str__() + \
            "\n=====================\nCechy Specjalne\n=====================\n" + \
            self.st.__str__() + "\n=====================\nBronie\n=====================\n" + wep + \
            "=====================\nZdolności\n=====================\n"+ ski+ \
            "=====================\nTalenty\n=====================\n" + tal+ \
            "=====================\nEq\n=====================\n"+ eq +\
            "=====================\nPieniądze\n=====================\n" + self.Money.__str__()
