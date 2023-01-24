import random
class CharacterDescription:
    def __init__(self, gender,race):
        age_rand = random.randint(1,100)
        #Losowanie wieku
        if race == "Człowiek":
            if age_rand <= 5:
                self.age = 16
            elif age_rand <=10:
                self.age = 17
            elif age_rand <=15:
                self.age = 18
            elif age_rand <=20:
                self.age = 19
            elif age_rand <=25:
                self.age = 20
            elif age_rand <=30:
                self.age = 21
            elif age_rand <=35:
                self.age = 22
            elif age_rand <=40:
                self.age = 23
            elif age_rand <=45:
                self.age = 24
            elif age_rand <=50:
                self.age = 25
            elif age_rand <=55:
                self.age = 26
            elif age_rand <=60:
                self.age = 27
            elif age_rand <=65:
                self.age = 28
            elif age_rand <=70:
                self.age = 29
            elif age_rand <=75:
                self.age = 30
            elif age_rand <=80:
                self.age = 31
            elif age_rand <=85:
                self.age = 32
            elif age_rand <=90:
                self.age = 33
            elif age_rand <=95:
                self.age = 34
            else:
                self.age = 35
        elif race == "Elf":
            if age_rand <= 5:
                self.age = 30
            elif age_rand <= 10:
                self.age = 35
            elif age_rand <= 15:
                self.age = 40
            elif age_rand <= 20:
                self.age = 45
            elif age_rand <= 25:
                self.age = 50
            elif age_rand <= 30:
                self.age = 55
            elif age_rand <= 35:
                self.age = 60
            elif age_rand <= 40:
                self.age = 65
            elif age_rand <= 45:
                self.age = 70
            elif age_rand <= 50:
                self.age = 75
            elif age_rand <= 55:
                self.age = 80
            elif age_rand <= 60:
                self.age = 85
            elif age_rand <= 65:
                self.age = 90
            elif age_rand <= 70:
                self.age = 95
            elif age_rand <= 75:
                self.age = 100
            elif age_rand <= 80:
                self.age = 105
            elif age_rand <= 85:
                self.age = 110
            elif age_rand <= 90:
                self.age = 115
            elif age_rand <= 95:
                self.age = 120
            else:
                self.age = 125
        elif race == "Krasnolud":
            if age_rand <= 5:
                self.age = 20
            elif age_rand <= 10:
                self.age = 25
            elif age_rand <= 15:
                self.age = 30
            elif age_rand <= 20:
                self.age = 35
            elif age_rand <= 25:
                self.age = 40
            elif age_rand <= 30:
                self.age = 45
            elif age_rand <= 35:
                self.age = 50
            elif age_rand <= 40:
                self.age = 55
            elif age_rand <= 45:
                self.age = 60
            elif age_rand <= 50:
                self.age = 65
            elif age_rand <= 55:
                self.age = 70
            elif age_rand <= 60:
                self.age = 75
            elif age_rand <= 65:
                self.age = 80
            elif age_rand <= 70:
                self.age = 85
            elif age_rand <= 75:
                self.age = 90
            elif age_rand <= 80:
                self.age = 95
            elif age_rand <= 85:
                self.age = 100
            elif age_rand <= 90:
                self.age = 105
            elif age_rand <= 95:
                self.age = 110
            else:
                self.age = 115
        elif race == "Niziołek":
            if age_rand <= 5:
                self.age = 20
            elif age_rand <= 10:
                self.age = 22
            elif age_rand <= 15:
                self.age = 24
            elif age_rand <= 20:
                self.age = 26
            elif age_rand <= 25:
                self.age = 28
            elif age_rand <= 30:
                self.age = 30
            elif age_rand <= 35:
                self.age = 32
            elif age_rand <= 40:
                self.age = 34
            elif age_rand <= 45:
                self.age = 36
            elif age_rand <= 50:
                self.age = 38
            elif age_rand <= 55:
                self.age = 40
            elif age_rand <= 60:
                self.age = 42
            elif age_rand <= 65:
                self.age = 44
            elif age_rand <= 70:
                self.age = 46
            elif age_rand <= 75:
                self.age = 50
            elif age_rand <= 80:
                self.age = 52
            elif age_rand <= 85:
                self.age = 54
            elif age_rand <= 90:
                self.age = 56
            elif age_rand <= 95:
                self.age = 58
            else:
                self.age = 60

        #Losowanie Wzrostu
        height_rand = random.randint(1,10) + random.randint(1,10)
        if race == "Człowiek":
            self.height= 160 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        elif race == "Elf":
            self.height= 170 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        elif race == "Krasnolud":
            self.height= 145 + height_rand
            if gender == "Kobieta":
                self.height -= 15
        elif race == "Niziołek":
            self.height= 110 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        #Losowanie Koloru Oczu
        eye_rand = random.randint(1,10) + random.randint(1,10)
        if race == "Człowiek":
            if eye_rand == 1:
                self.eye_color = "Szary"
            elif eye_rand == 2:
                self.eye_color = "Ciemnoniebieski"
            elif eye_rand == 3:
                self.eye_color = "Niebieski"
            elif eye_rand == 4:
                self.eye_color = "Zielony"
            elif eye_rand == 5:
                self.eye_color = "Piwny"
            elif eye_rand == 6:
                self.eye_color = "Jasnobrązowy"
            elif eye_rand == 7:
                self.eye_color = "Brązowy"
            elif eye_rand == 8:
                self.eye_color = "Ciemnobrązowy"
            elif eye_rand == 9:
                self.eye_color = "Fioletowy"
            elif eye_rand == 10:
                self.eye_color = "Czarny"