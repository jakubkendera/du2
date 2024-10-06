cislo = float(input("zadaj lubovolne cislo"))
pocet_cifier = 0
while cislo != 0:
    cislo //= 10
    pocet_cifier += 1


def stredne_cislo_neparne():
    if pocet_cifier % 2 == 1:
        cislo // 10 ** (pocet_cifier / 2)
        print(stredne_cislo_neparne)


def stredne_cislo_parne():
    if pocet_cifier % 2 == 0:
        (cislo // 10 ** (abs(-(pocet_cifier / 2))) + cislo // 10 ** ((abs(-(pocet_cifier / 2))) + 1)) /2
        print(stredne_cislo_neparne)





def symetricke():
    if cislo%10 == cislo//10:
        print("číslo je symetrické")

