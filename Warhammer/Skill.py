class Skill:
    def __init__(self, n, s1, s2):
        self.name = n  # nazwa skila
        self.spec1 = s1  # podstawowa/zaawansowana
        self.spec2 = s2  # cecha

    def getSkill(self):
        return self.name + self.spec1 + self.spec2
