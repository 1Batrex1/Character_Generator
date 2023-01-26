from Warhammer.Money import *
from Warhammer.CharacterDescription import *
from Warhammer.specialTraits import *


class Hero:

    def __init__(self, name, race, profesion, gender, Ski, Tal, Eq, *Wep):
        self.name = name
        self.race = race
        self.profession = profesion
        self.Chad = CharacterDescription(gender, self.race)
        self.st = SpecialTraits(self.race)
        self.wep  = [] # Tabela Broni
        self.Ski = []  # Tabela skili
        self.Tal = []  # Tabela Talentów
        self.Eq = []  # Tabela eq
        self.Money = Money()

    def __str__(self):
        wep = ""
        for x in self.wep:
            wep += str(x)
        return "=====================\nBohater\n=====================\nImię:" + self.name + "\nRasa:" + \
            self.race + "\nProfesja:" + self.profession + \
            "\n=====================\nOpis Bohatera\n=====================\n" + self.Chad.__str__() + \
            "\n=====================\nCechy Specjalne\n=====================\n" + \
            self.st.__str__() + "\n=====================\nBronie\n=====================\n" + wep + \
            "=====================\nPieniądze\n=====================\n" + self.Money.__str__()
