import random
class money:
    goldCrowns = 0
    silverShillings = 0
    brassPennies = 0

    def __init__(self):
        goldCrowns = random.randint(1, 10) + random.randint(1,10) - 1 #generowanie liczby koron poprzez rzut 2d10, następnie 'rozbijamy' jedną na mniejsze nominały
        silverShillings = 19 #20-1 żeby rozbić na mniejszy nominał
        brassPennies = 12

    def return_crowns(self):
        return self.goldCrowns

    def return_shillings(self):
        return self.silverShillings

    def return_pennies(self):
        return self.brassPennies
