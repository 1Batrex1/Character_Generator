class Talent:
    def __init__(self, n, desc):
        self.name = n  # nazwa talenty
        self.description = desc  # opis umiejętności

    def GetTalent(self):
        return self.name + self.description