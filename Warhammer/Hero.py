
class hero:
    class SpecialTraits:
        def __init(self):
            self.fightSkills = 0
            self.shootingSkills = 0
            self.sturdiness = 0
            self.endurance = 0
            self.agility = 0

            self.intelligence = 0

            self.willpower = 0

            self.persuasion = 0
            #pozostale traity
            self.attack = 0
            self.strength = 0
            self.resilience = 0
            self.speed = 0
            self.magic = 0
            self.crazyPoints = 0
            self.destinyPoints = 0

    class Skill:
        def  __init__(self,n,s1,s2):
            self.name = n #nazwa skila
            self.spec1 = s1 #czy specjalizacja +10%
            self.spec2 = s1 #czy specjalizacja +10%
        def GetSkill(self):
            return self.name + self.spec1 + self.spec2

    class Talents:
        def  __init__(self,n,desc):
            self.name = n #nazwa talenty
            self.description = desc # opis umiejętności
        def GetTalent(self):
            return self.name + self.description



    def __init__(self,n,r,p,cd,Wep,Ski,Tal,Eq,M):
        self.name = n
        self.race = r
        self.profession = p
        self.Chad = cd
        self.st = "Tu będzie klasa"
        self.wep = [] #Tabela Broni
        self.Ski = [] #Tabela skili
        self.Tal = [] # Tabela Talentów
        self.Eq = [] #Tabela eq
        self.wep.append(Wep)


