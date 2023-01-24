import random


class CharacterDescription:
    def __init__(self, gender, race):
        age_rand = random.randint(1, 100)
        waga_rand = random.randint(1, 100)
        # losowanie wagi
        if race == "Człowiek":
            if waga_rand == 1:
                self.waga = 50
            elif waga_rand <= 10:
                self.waga = 55
            elif waga_rand <= 20:
                self.waga = 60
            elif waga_rand <= 30:
                self.waga = 65
            elif waga_rand <= 40:
                self.waga = 70
            elif waga_rand <= 50:
                self.waga = 75
            elif waga_rand <= 60:
                self.waga = 80
            elif waga_rand <= 70:
                self.waga = 85
            elif waga_rand <= 80:
                self.waga = 90
            elif waga_rand <= 90:
                self.waga = 95
            elif waga_rand <= 99:
                self.waga = 100
            else:
                self.waga = 110

            if race == "Elf":
                if waga_rand == 1:
                    self.waga = 40
                elif waga_rand <= 10:
                    self.waga = 45
                elif waga_rand <= 20:
                    self.waga = 50
                elif waga_rand <= 30:
                    self.waga = 55
                elif waga_rand <= 40:
                    self.waga = 60
                elif waga_rand <= 50:
                    self.waga = 65
                elif waga_rand <= 60:
                    self.waga = 70
                elif waga_rand <= 70:
                    self.waga = 75
                elif waga_rand <= 80:
                    self.waga = 80
                elif waga_rand <= 90:
                    self.waga = 85
                elif waga_rand <= 99:
                    self.waga = 90
                else:
                    self.waga = 95

                if race == "Krasnolud":
                    if waga_rand == 1:
                        self.waga = 45
                    elif waga_rand <= 10:
                        self.waga = 50
                    elif waga_rand <= 20:
                        self.waga = 56
                    elif waga_rand <= 30:
                        self.waga = 60
                    elif waga_rand <= 40:
                        self.waga = 65
                    elif waga_rand <= 50:
                        self.waga = 70
                    elif waga_rand <= 60:
                        self.waga = 75
                    elif waga_rand <= 70:
                        self.waga = 80
                    elif waga_rand <= 80:
                        self.waga = 85
                    elif waga_rand <= 90:
                        self.waga = 90
                    elif waga_rand <= 99:
                        self.waga = 95
                    else:
                        self.waga = 100

                if race == "Niziołek":
                    if waga_rand == 1:
                        self.waga = 35
                    elif waga_rand <= 10:
                        self.waga = 35
                    elif waga_rand <= 20:
                        self.waga = 40
                    elif waga_rand <= 30:
                        self.waga = 40
                    elif waga_rand <= 40:
                        self.waga = 45
                    elif waga_rand <= 50:
                        self.waga = 45
                    elif waga_rand <= 60:
                        self.waga = 50
                    elif waga_rand <= 70:
                        self.waga = 50
                    elif waga_rand <= 80:
                        self.waga = 55
                    elif waga_rand <= 90:
                        self.waga = 60
                    elif waga_rand <= 99:
                        self.waga = 65
                    else:
                        self.waga = 70

        # Losowanie wieku
        if race == "Człowiek":
            if age_rand <= 5:
                self.age = 16
            elif age_rand <= 10:
                self.age = 17
            elif age_rand <= 15:
                self.age = 18
            elif age_rand <= 20:
                self.age = 19
            elif age_rand <= 25:
                self.age = 20
            elif age_rand <= 30:
                self.age = 21
            elif age_rand <= 35:
                self.age = 22
            elif age_rand <= 40:
                self.age = 23
            elif age_rand <= 45:
                self.age = 24
            elif age_rand <= 50:
                self.age = 25
            elif age_rand <= 55:
                self.age = 26
            elif age_rand <= 60:
                self.age = 27
            elif age_rand <= 65:
                self.age = 28
            elif age_rand <= 70:
                self.age = 29
            elif age_rand <= 75:
                self.age = 30
            elif age_rand <= 80:
                self.age = 31
            elif age_rand <= 85:
                self.age = 32
            elif age_rand <= 90:
                self.age = 33
            elif age_rand <= 95:
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

        # Losowanie Wzrostu
        height_rand = random.randint(1, 10) + random.randint(1, 10)
        if race == "Człowiek":
            self.height = 160 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        elif race == "Elf":
            self.height = 170 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        elif race == "Krasnolud":
            self.height = 145 + height_rand
            if gender == "Kobieta":
                self.height -= 15
        elif race == "Niziołek":
            self.height = 110 + height_rand
            if gender == "Kobieta":
                self.height -= 10
        # Losowanie Koloru Oczu
        eye_rand = random.randint(1, 10) + random.randint(1, 10)
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
        elif race == "Elf":
            if eye_rand == 1:
                self.eye_color = "Szaroniebieski"
            elif eye_rand == 2:
                self.eye_color = "Niebieski"
            elif eye_rand == 3:
                self.eye_color = "Zielony"
            elif eye_rand == 4:
                self.eye_color = "Orzechowy"
            elif eye_rand == 5:
                self.eye_color = "Kasztanowy"
            elif eye_rand == 6:
                self.eye_color = "Brązowy"
            elif eye_rand == 7:
                self.eye_color = "Ciemnobrązowy"
            elif eye_rand == 8:
                self.eye_color = "Srebrny"
            elif eye_rand == 9:
                self.eye_color = "Fioletowy"
            elif eye_rand == 10:
                self.eye_color = "Czarny"
        elif race == "Krasnolud":
            if eye_rand == 1:
                self.eye_color = "Szary"
            elif eye_rand == 2:
                self.eye_color = "Ciemnoniebieski"
            elif eye_rand == 3:
                self.eye_color = "Piwny"
            elif eye_rand <= 5:
                self.eye_color = "Jasnobrązowy"
            elif eye_rand <= 7:
                self.eye_color = "Brązowy"
            elif eye_rand <= 9:
                self.eye_color = "Ciemnobrązowy"
            elif eye_rand == 10:
                self.eye_color = "Fioletowy"
        elif race == "Niziołek":
            if eye_rand == 1:
                self.eye_color = "Niebieski"
            elif eye_rand <= 3:
                self.eye_color = "Orzechowy"
            elif eye_rand <= 5:
                self.eye_color = "Jasnobrązowy"
            elif eye_rand <= 7:
                self.eye_color = "Brązowy"
            elif eye_rand <= 10:
                self.eye_color = "Ciemnobrązowy"

        # Losowanie Znaku szczególnego
        distinctive_sign_rand = random.randint(1, 100)
        if distinctive_sign_rand <= 5:
            self.distinctive_sign = "Bielmo na oku"
        elif distinctive_sign_rand <= 10:
            self.distinctive_sign = "Blizna"
        elif distinctive_sign_rand <= 15:
            self.distinctive_sign = "Brak brwi"
        elif distinctive_sign_rand <= 20:
            self.distinctive_sign = "Brak palca"
        elif distinctive_sign_rand <= 25:
            self.distinctive_sign = "Brak zęba"
        elif distinctive_sign_rand <= 30:
            self.distinctive_sign = "Brodawki"
        elif distinctive_sign_rand <= 35:
            self.distinctive_sign = "Blada cera"
        elif distinctive_sign_rand <= 40:
            self.distinctive_sign = "Duży nos"
        elif distinctive_sign_rand <= 45:
            self.distinctive_sign = "Duży pieprzyk"
        elif distinctive_sign_rand <= 50:
            self.distinctive_sign = "Dziwny zapach ciała"
        elif distinctive_sign_rand <= 55:
            self.distinctive_sign = "Kolczyk w nosie"
        elif distinctive_sign_rand <= 60:
            self.distinctive_sign = "Kolczyk w uchu"
        elif distinctive_sign_rand <= 65:
            self.distinctive_sign = "Niewielka łysina"
        elif distinctive_sign_rand <= 70:
            self.distinctive_sign = "Oczy różnego koloru"
        elif distinctive_sign_rand <= 75:
            self.distinctive_sign = "Piegi"
        elif distinctive_sign_rand <= 80:
            self.distinctive_sign = "Poszarpane ucho"
        elif distinctive_sign_rand <= 85:
            self.distinctive_sign = "Ślady po ospie"
        elif distinctive_sign_rand <= 90:
            self.distinctive_sign = "Tatuaż"
        elif distinctive_sign_rand <= 94:
            self.distinctive_sign = "Wystające zęby"
        elif distinctive_sign_rand <= 98:
            self.distinctive_sign = "Wytrzeszczone oczy"
        else:
            self.distinctive_sign = "Złamany nos"

        # Losowanie Znaku gwiezdnego
        star_sign_rand = random.randint(1, 100)
        if star_sign_rand <= 5:
            self.star_sign = "Bębniarz"
        elif star_sign_rand <= 10:
            self.star_sign = "Dudy"
        elif star_sign_rand <= 15:
            self.star_sign = "Dwa Byki"
        elif star_sign_rand <= 25:
            self.star_sign = "Głupiec Mummit"
        elif star_sign_rand <= 30:
            self.star_sign = "Gwiazda Uroku"
        elif star_sign_rand <= 35:
            self.star_sign = "Gwiazda Wieczorna"
        elif star_sign_rand <= 40:
            self.star_sign = "Kocioł Ryhi"
        elif star_sign_rand <= 45:
            self.star_sign = "Lancet"
        elif star_sign_rand <= 50:
            self.star_sign = "Mędrzec Mammit"
        elif star_sign_rand <= 55:
            self.star_sign = "Pas Grungiego"
        elif star_sign_rand <= 60:
            self.star_sign = "Rozbity Wóz"
        elif star_sign_rand <= 65:
            self.star_sign = "Smok Dragomas"
        elif star_sign_rand <= 70:
            self.star_sign = "Sznur Limnera"
        elif star_sign_rand <= 75:
            self.star_sign = "Tancerka"
        elif star_sign_rand <= 80:
            self.star_sign = "Tłusty Kozioł"
        elif star_sign_rand <= 85:
            self.star_sign = "Vobist Ulotny"
        elif star_sign_rand <= 90:
            self.star_sign = "Wielki Krzyż"
        elif star_sign_rand <= 95:
            self.star_sign = "Wół Gnuthus"
        elif star_sign_rand <= 98:
            self.star_sign = "Wymund Pustelnik"
        else:
            self.star_sign = "Złoty Kogut"
        number_of_siblings_rand = random.randint(1, 10)

        if race == "Człowiek":
            if number_of_siblings_rand == 1:
                self.number_of_siblings = 0
            elif number_of_siblings_rand <= 3:
                self.number_of_siblings = 1
            elif number_of_siblings_rand <= 5:
                self.number_of_siblings = 2
            elif number_of_siblings_rand <= 7:
                self.number_of_siblings = 3
            elif number_of_siblings_rand <= 9:
                self.number_of_siblings = 4
            else:
                self.number_of_siblings = 5
        elif race == "Elf":
            if number_of_siblings_rand == 1:
                self.number_of_siblings = 0
            elif number_of_siblings_rand <= 5:
                self.number_of_siblings = 1
            elif number_of_siblings_rand <= 9:
                self.number_of_siblings = 2
            else:
                self.number_of_siblings = 3
        elif race == "Krasnolud":
            if number_of_siblings_rand <= 3:
                self.number_of_siblings = 0
            elif number_of_siblings_rand <= 7:
                self.number_of_siblings = 1
            elif number_of_siblings_rand <= 9:
                self.number_of_siblings = 2
            else:
                self.number_of_siblings = 3
        elif race == "Niziołek":
            if number_of_siblings_rand == 1:
                self.number_of_siblings = 1
            elif number_of_siblings_rand <= 3:
                self.number_of_siblings = 2
            elif number_of_siblings_rand <= 5:
                self.number_of_siblings = 3
            elif number_of_siblings_rand <= 7:
                self.number_of_siblings = 4
            elif number_of_siblings_rand <= 9:
                self.number_of_siblings = 5
            else:
                self.number_of_siblings = 6

        # losowanie koloru wlosow
        kolor_wlosow_rand = random.randint(1, 10)
        if race == "Człowiek":
            if kolor_wlosow_rand == 1:
                self.kolor_wlosow = "Popielaty"
            elif kolor_wlosow_rand == 2:
                self.kolor_wlosow = "Ciemny blond"
            elif kolor_wlosow_rand == 3:
                self.kolor_wlosow = "Blond"
            elif kolor_wlosow_rand == 4:
                self.kolor_wlosow = "Rudy"
            elif kolor_wlosow_rand == 5:
                self.kolor_wlosow = "Ciemno rudy"
            elif kolor_wlosow_rand == 6:
                self.kolor_wlosow = "Jasnobrązowy"
            elif kolor_wlosow_rand == 7:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 8:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 9:
                self.kolor_wlosow = "Ciemnobrązowy"
            elif kolor_wlosow_rand == 10:
                self.kolor_wlosow = "Czarny"

        if race == "Elf":
            if kolor_wlosow_rand == 1:
                self.kolor_wlosow = "Srebrny"
            elif kolor_wlosow_rand == 2:
                self.kolor_wlosow = "Biały"
            elif kolor_wlosow_rand == 3:
                self.kolor_wlosow = "Jasny blond"
            elif kolor_wlosow_rand == 4:
                self.kolor_wlosow = "Ciemny blond"
            elif kolor_wlosow_rand == 5:
                self.kolor_wlosow = "Miedziany"
            elif kolor_wlosow_rand == 6:
                self.kolor_wlosow = "Jasnobrązowy"
            elif kolor_wlosow_rand == 7:
                self.kolor_wlosow = "Kasztanowy"
            elif kolor_wlosow_rand == 8:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 9:
                self.kolor_wlosow = "Ciemnobrązowy"
            elif kolor_wlosow_rand == 10:
                self.kolor_wlosow = "Czarny"

        if race == "Krasnolud":
            if kolor_wlosow_rand == 1:
                self.kolor_wlosow = "Popielaty"
            elif kolor_wlosow_rand == 2:
                self.kolor_wlosow = "Blond"
            elif kolor_wlosow_rand == 3:
                self.kolor_wlosow = "Ciemny rudy"
            elif kolor_wlosow_rand == 4:
                self.kolor_wlosow = "Czerwony"
            elif kolor_wlosow_rand == 5:
                self.kolor_wlosow = "Rudy"
            elif kolor_wlosow_rand == 6:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 7:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 8:
                self.kolor_wlosow = "Ciemno brązowy"
            elif kolor_wlosow_rand == 9:
                self.kolor_wlosow = "Czarny"
            elif kolor_wlosow_rand == 10:
                self.kolor_wlosow = "Kruczo czarny"

        if race == "Niziołek":
            if kolor_wlosow_rand == 1:
                self.kolor_wlosow = "Popielaty"
            elif kolor_wlosow_rand == 2:
                self.kolor_wlosow = "Ciemny blond"
            elif kolor_wlosow_rand == 3:
                self.kolor_wlosow = "Blond"
            elif kolor_wlosow_rand == 4:
                self.kolor_wlosow = "Blond"
            elif kolor_wlosow_rand == 5:
                self.kolor_wlosow = "Rudy"
            elif kolor_wlosow_rand == 6:
                self.kolor_wlosow = "Ciemny rudy"
            elif kolor_wlosow_rand == 7:
                self.kolor_wlosow = "Jasno brązowy"
            elif kolor_wlosow_rand == 8:
                self.kolor_wlosow = "Brązowy"
            elif kolor_wlosow_rand == 9:
                self.kolor_wlosow = "Ciemnobrązowy"
            elif kolor_wlosow_rand == 10:
                self.kolor_wlosow = "Czarny"

        # losowanie miejsca urodzenia

        if race == "Człowiek":
            miejsce_urodzenia_rand = random.randint(1, 10)
            if miejsce_urodzenia_rand == 1:
                self.miejsce_urodzenia = "Averland"
            elif miejsce_urodzenia_rand == 2:
                self.miejsce_urodzenia = "Hochland"
            elif miejsce_urodzenia_rand == 3:
                self.miejsce_urodzenia = "Middenland"
            elif miejsce_urodzenia_rand == 4:
                self.miejsce_urodzenia = "Nordland"
            elif miejsce_urodzenia_rand == 5:
                self.miejsce_urodzenia = "Ostermark"
            elif miejsce_urodzenia_rand == 6:
                self.miejsce_urodzenia = "Ostland"
            elif miejsce_urodzenia_rand == 7:
                self.miejsce_urodzenia = "Reikland"
            elif miejsce_urodzenia_rand == 8:
                self.miejsce_urodzenia = "Stirland"
            elif miejsce_urodzenia_rand == 9:
                self.miejsce_urodzenia = "Talabecland"
            elif miejsce_urodzenia_rand == 10:
                self.miejsce_urodzenia = "Wissenland"

            miejsce_urodzenia_rand = random.randint(1, 10)
            if miejsce_urodzenia_rand == 1:
                self.miejsce_urodzenia_rodzaj = "Stolica prowincji"
            elif miejsce_urodzenia_rand == 2:
                self.miejsce_urodzenia_rodzaj = "Bogate miasto"
            elif miejsce_urodzenia_rand == 3:
                self.miejsce_urodzenia_rodzaj = "Miasto targowe"
            elif miejsce_urodzenia_rand == 4:
                self.miejsce_urodzenia_rodzaj = "Fort wojskowy"
            elif miejsce_urodzenia_rand == 5:
                self.miejsce_urodzenia_rodzaj = "Miasteczko"
            elif miejsce_urodzenia_rand == 6:
                self.miejsce_urodzenia_rodzaj = "Bogata wieś"
            elif miejsce_urodzenia_rand == 7:
                self.miejsce_urodzenia_rodzaj = "Wioska rolnicza"
            elif miejsce_urodzenia_rand == 8:
                self.miejsce_urodzenia_rodzaj = "Wioska rybacka"
            elif miejsce_urodzenia_rand == 9:
                self.miejsce_urodzenia_rodzaj = "Biedna wioska"
            elif miejsce_urodzenia_rand == 10:
                self.miejsce_urodzenia_rodzaj = "Samotna chata"

        miejsce_urodzenia_rand = random.randint(1, 100)

        if race == "Krasnolud":
            if miejsce_urodzenia_rand <= 30:
                miejsce_urodzenia_rand = random.randint(1, 10)
                if miejsce_urodzenia_rand == 1:
                    self.miejsce_urodzenia = "Averland"
                elif miejsce_urodzenia_rand == 2:
                    self.miejsce_urodzenia = "Hochland"
                elif miejsce_urodzenia_rand == 3:
                    self.miejsce_urodzenia = "Middenland"
                elif miejsce_urodzenia_rand == 4:
                    self.miejsce_urodzenia = "Nordland"
                elif miejsce_urodzenia_rand == 5:
                    self.miejsce_urodzenia = "Ostermark"
                elif miejsce_urodzenia_rand == 6:
                    self.miejsce_urodzenia = "Ostland"
                elif miejsce_urodzenia_rand == 7:
                    self.miejsce_urodzenia = "Reikland"
                elif miejsce_urodzenia_rand == 8:
                    self.miejsce_urodzenia = "Stirland"
                elif miejsce_urodzenia_rand == 9:
                    self.miejsce_urodzenia = "Talabecland"
                elif miejsce_urodzenia_rand == 10:
                    self.miejsce_urodzenia = "Wissenland"

                miejsce_urodzenia_rand = random.randint(1, 10)
                if miejsce_urodzenia_rand == 1:
                    self.miejsce_urodzenia_rodzaj = "Stolica prowincji"
                elif miejsce_urodzenia_rand == 2:
                    self.miejsce_urodzenia_rodzaj = "Bogate miasto"
                elif miejsce_urodzenia_rand == 3:
                    self.miejsce_urodzenia_rodzaj = "Miasto targowe"
                elif miejsce_urodzenia_rand == 4:
                    self.miejsce_urodzenia_rodzaj = "Fort wojskowy"
                elif miejsce_urodzenia_rand == 5:
                    self.miejsce_urodzenia_rodzaj = "Miasteczko"
                elif miejsce_urodzenia_rand == 6:
                    self.miejsce_urodzenia_rodzaj = "Bogata wieś"
                elif miejsce_urodzenia_rand == 7:
                    self.miejsce_urodzenia_rodzaj = "Wioska rolnicza"
                elif miejsce_urodzenia_rand == 8:
                    self.miejsce_urodzenia_rodzaj = "Wioska rybacka"
                elif miejsce_urodzenia_rand == 9:
                    self.miejsce_urodzenia_rodzaj = "Biedna wioska"
                elif miejsce_urodzenia_rand == 10:
                    self.miejsce_urodzenia_rodzaj = "Samotna chata"

            elif miejsce_urodzenia_rand <= 40:
                self.miejsce_urodzenia = "Karak Norn (Góry Szare)"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 50:
                self.miejsce_urodzenia = "Karak Izor (Przeskok)"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 60:
                self.miejsce_urodzenia = "Karak Hirn (Góry Czarne)"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 70:
                self.miejsce_urodzenia = "Karak Hadrin (Góry Krańca Świata)"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 80:
                self.miejsce_urodzenia = "Karaz-a-Karak (Góry Krańca Świata)"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 90:
                self.miejsce_urodzenia = "Zhufbar (Góry Krańca Świata)"
                self.miejsce_urodzenia_rodzaj = "/"
            else:
                self.miejsce_urodzenia = "Barak Varr (Czarna Zatoka)"
                self.miejsce_urodzenia_rodzaj = "/"

        if race == "Elf":
            if miejsce_urodzenia_rand <= 20:
                self.miejsce_urodzenia = "Altdorf"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 40:
                self.miejsce_urodzenia = "Marienburg"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 70:
                self.miejsce_urodzenia = "Las Laurelorn"
                self.miejsce_urodzenia_rodzaj = "/"
            elif miejsce_urodzenia_rand <= 85:
                self.miejsce_urodzenia = "Wielki Las"
                self.miejsce_urodzenia_rodzaj = "/"
            else:
                self.miejsce_urodzenia = "Las Reikwald"
                self.miejsce_urodzenia_rodzaj = "/"

        if race == "Niziołek":
            if miejsce_urodzenia_rand <= 50:
                miejsce_urodzenia_rand = random.randint(1, 10)
                if miejsce_urodzenia_rand == 1:
                    self.miejsce_urodzenia = "Averland"
                elif miejsce_urodzenia_rand == 2:
                    self.miejsce_urodzenia = "Hochland"
                elif miejsce_urodzenia_rand == 3:
                    self.miejsce_urodzenia = "Middenland"
                elif miejsce_urodzenia_rand == 4:
                    self.miejsce_urodzenia = "Nordland"
                elif miejsce_urodzenia_rand == 5:
                    self.miejsce_urodzenia = "Ostermark"
                elif miejsce_urodzenia_rand == 6:
                    self.miejsce_urodzenia = "Ostland"
                elif miejsce_urodzenia_rand == 7:
                    self.miejsce_urodzenia = "Reikland"
                elif miejsce_urodzenia_rand == 8:
                    self.miejsce_urodzenia = "Stirland"
                elif miejsce_urodzenia_rand == 9:
                    self.miejsce_urodzenia = "Talabecland"
                elif miejsce_urodzenia_rand == 10:
                    self.miejsce_urodzenia = "Wissenland"

                miejsce_urodzenia_rand = random.randint(1, 10)
                if miejsce_urodzenia_rand == 1:
                    self.miejsce_urodzenia_rodzaj = "Stolica prowincji"
                elif miejsce_urodzenia_rand == 2:
                    self.miejsce_urodzenia_rodzaj = "Bogate miasto"
                elif miejsce_urodzenia_rand == 3:
                    self.miejsce_urodzenia_rodzaj = "Miasto targowe"
                elif miejsce_urodzenia_rand == 4:
                    self.miejsce_urodzenia_rodzaj = "Fort wojskowy"
                elif miejsce_urodzenia_rand == 5:
                    self.miejsce_urodzenia_rodzaj = "Miasteczko"
                elif miejsce_urodzenia_rand == 6:
                    self.miejsce_urodzenia_rodzaj = "Bogata wieś"
                elif miejsce_urodzenia_rand == 7:
                    self.miejsce_urodzenia_rodzaj = "Wioska rolnicza"
                elif miejsce_urodzenia_rand == 8:
                    self.miejsce_urodzenia_rodzaj = "Wioska rybacka"
                elif miejsce_urodzenia_rand == 9:
                    self.miejsce_urodzenia_rodzaj = "Biedna wioska"
                elif miejsce_urodzenia_rand == 10:
                    self.miejsce_urodzenia_rodzaj = "Samotna chata"
            else:
                self.miejsce_urodzenia = ""
                self.miejsce_urodzenia_rodzaj = "/"
