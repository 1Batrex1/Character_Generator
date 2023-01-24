from Warhammer.Weapon import Weapon
def wczytywanie(filename):
    bronie = []

    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip('\t').split(';')
            w = Weapon(pola[0] , pola[1] , pola[2] , pola[3] , pola[4])
            bronie.append(w)


    return bronie



