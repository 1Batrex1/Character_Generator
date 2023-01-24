import random


class SpecialTraits:
    def __init__(self, race):

        self.fightSkills = (20 + random.randint(1, 10) + random.randint(1, 10))
        self.shootingSkills = (20 + random.randint(1, 10) + random.randint(1, 10))
        self.sturdiness = (20 + random.randint(1, 10) + random.randint(1, 10))
        self.endurance = (20 + random.randint(1, 10) + random.randint(1, 10))
        self.agility = (20 + random.randint(1, 10) + random.randint(1, 10))

        self.intelligence = (20 + random.randint(1, 10) + random.randint(1, 10))

        self.willpower = (20 + random.randint(1, 10) + random.randint(1, 10))

        self.persuasion = (20 + random.randint(1, 10) + random.randint(1, 10))
        # pozostale traity
        self.attack = 1
        self.speed = 4
        self.hp = random.randint(1, 10)
        if (race == "Elf"):
            self.shootingSkills += 10
            self.agility += 10
            self.speed = 5

        if (race == "Krasnolud"):
            self.fightSkills += 10
            self.endurance += 10
            self.agility -= 10
            self.persuasion -= 10
            self.speed = 3

        if (race == "Niziołek"):
            self.fightSkills -= 10
            self.shootingSkills += 10
            self.endurance -= 10
            self.sturdiness -= 10
            self.agility += 10
            self.persuasion += 10

        if (race == "Człowiek"):
            if (self.hp <= 3):
                self.hp = 10
            elif (self.hp <= 6):
                self.hp = 11
            elif (self.hp <= 9):
                self.hp = 12
            else:
                self.hp = 13

        if (race == "Elf"):
            if (self.hp <= 3):
                self.hp = 9
            elif (self.hp <= 6):
                self.hp = 10
            elif (self.hp <= 9):
                self.hp = 11
            else:
                self.hp = 12

        if (race == "Krasnolud"):
            if (self.hp <= 3):
                self.hp = 11
            elif (self.hp <= 6):
                self.hp = 12
            elif (self.hp <= 9):
                self.hp = 13
            else:
                self.hp = 14

        if (race == "Niziołek"):
            if (self.hp <= 3):
                self.hp = 8
            elif (self.hp <= 6):
                self.hp = 9
            elif (self.hp <= 9):
                self.hp = 10
            else:
                self.hp = 11

        self.health = self.hp

        self.strength = self.sturdiness / 10
        self.resilience = self.endurance / 10
        self.magic = 0
        self.crazyPoints = 0
        self.pp = random.randint(1, 10)

        if (race == "Człowiek"):
            if (self.pp <= 4):
                self.pp = 2
            else:
                self.pp = 3

        if (race == "Elf"):
            if (self.pp <= 4):
                self.pp = 1
            else:
                self.pp = 2

        if (race == "Krasnolud"):
            if (self.pp <= 4):
                self.pp = 1
            elif (self.pp <= 7):
                self.pp = 2
            else:
                self.pp = 3

        if (race == "Niziołek"):
            if (self.pp <= 7):
                self.pp = 2
            else:
                self.pp = 3

        self.destinyPoints = self.pp

    def __str__(self):
        return "WW:" + str(self.fightSkills) + "\nUS:" + str(self.shootingSkills) \
            + "\nK:" + str(self.sturdiness) + "\nOdp:" + str(self.endurance) + "\nZr:" + str(self.agility) + \
            "\nInt:" + str(self.intelligence) + "\nSW:" + str(self.willpower) + "\nOdg" + str(self.persuasion) \
            + "\nA:" + str(self.attack) + "\nŻyw:" + str(self.hp) + "\nS:" + str(self.strength) + "\nWt:" + str(
                self.resilience) + \
            "\nSz:" + str(self.speed) + "\nMag:" + str(self.magic) + "\nPO:" + str(self.crazyPoints) + "\nPP:" + str(
                self.destinyPoints)
