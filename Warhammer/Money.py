import random


class Money:

    def __init__(self):
        self.goldCrowns = random.randint(1, 10) + random.randint(1, 10) - 1
        # generowanie liczby koron poprzez rzut
        # 2d10, następnie 'rozbijamy' jedną na mniejsze nominały
        self.silverShillings = 19  # 20-1, żeby rozbić na mniejszy nominał
        self.brassPennies = 12

    def return_crowns(self):
        return self.goldCrowns

    def return_shillings(self):
        return self.silverShillings

    def return_pennies(self):
        return self.brassPennies

    def __str__(self):
        return "Złote Korony:" + str(self.goldCrowns) + "\nSrebrne Szylingi:" + \
            str(self.silverShillings) + "\nMiedziane Pensy:" + str(self.brassPennies)
