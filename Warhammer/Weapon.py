class Weapon:
    def __init__(self, name, category, strength, reach, properties):
        self.name = name
        self.category = category
        self.strength = strength
        self.reach = reach
        self.properties = properties

    def Get_Weapon(self):
        return self.name + self.category + self.strength + self.reach + self.properties

    def __str__(self):
        return self.name + self.category + self.strength + self.reach + self.properties
