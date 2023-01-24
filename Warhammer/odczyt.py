import re
def wczytywanie(filename):
    bronie = []

    with open(filename, encoding="utf8") as f:
        for line in f:
            pola = line.strip('\t').split(';')
            bronie.append(pola[0] + pola[1] + pola[2] + pola[3] + pola[4])


    return bronie


def read():
    objekt = wczytywanie("Weapons.txt")
    print(objekt)

read()
