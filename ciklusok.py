def feladat1(szam):
    i = 3
    while i <= szam:
        print(i, end=', ' if i < szam - 2 else ' ')
        i += 3



def feladat2(szam):
    while szam >= 1:
        print(szam, end=';' if szam > 1 else ' ')
        szam -= 1






def feladat3():
    szam = 1

    while szam % 5 != 0:
        szam = int(input("Kérem, adjon meg egy 5-tel osztható számot: "))

    print(f"A megadott szám ({szam}) osztható 5-tel.")




def feladat4(szam):
    i = 1
    while i <= szam:
        if i % 6 == 0:
            print("BUMMBAM", end='' if i == szam else ', ')
        elif i % 2 == 0:
            print("BAM", end='' if i == szam else ', ')
        elif i % 3 == 0:
            print("BUMM", end='' if i == szam else ', ')
        else:
            print(i, end='' if i == szam else ', ')
        i += 1






