


class Hero:


    class Sklis:
        def  __init__(self,n,s1,s2):
            self.name = n #nazwa skila
            self.spec1 = s1 #czy specjalizacja +10%
            self.spec2 = s1 #czy specjalizacja +10%
    class Talents:
        def  __init__(self,n,desc):
            self.name = n #nazwa talenty
            self.description = desc # opis umiejętności



    def __init__(self,n,r,p,cd,Wep,Ski,Tal,Eq,M):
        self.name = n
        self.race = r
        self.profession = p
        self.Chad = cd
        self.wep.append(Wep)
        self.st = "Tu będzie klasa"
        self.wep = [] #Tabela Broni
        self.Ski = [] #Tabela skili
        self.Tal = [] # Tabela Talentów
        self.Eq = [] #Tabela eq





