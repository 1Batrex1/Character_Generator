import random
class money:
    goldCrowns = 0
    silverShillings = 0
    brassPennies = 0

    def __init__(self):
        goldCrowns = random.randint(1, 10) + random.randint(1,10) - 1
        silverShillings = 19
        brassPennies = 12

    def return_crowns(self):
        return self.goldCrowns

    def return_shillings(self):
        return self.silverShillings

    def return_pennies(self):
        return self.brassPennies
