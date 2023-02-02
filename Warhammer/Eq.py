class Eq:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def GetEq(self):
        return self.name + self.description

    def __str__(self):
        return self.name + self.description
