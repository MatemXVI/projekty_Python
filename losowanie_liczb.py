import random

wylosowana_liczba = random.randrange(0, 100);
liczba_prob = 0
while(True):
    try:
        liczba_prob += 1
        liczba_uzytkownika = int(input("Podaj liczbę z zakresu od 0 do 100: "))
    except ValueError:
        print("Proszę podać liczbę!")
        continue
    if liczba_uzytkownika >= 0 and liczba_uzytkownika <= 100:
        if liczba_uzytkownika == wylosowana_liczba:
            print("Brawo, to ta liczba")
            print("Liczba prób: " + str(liczba_prob))
            break
        elif liczba_uzytkownika > wylosowana_liczba:
            print("Liczba jest za duża")
            print("Liczba prób: " + str(liczba_prob))
        elif liczba_uzytkownika < wylosowana_liczba:
            print("Liczba jest za mała")
            print("Liczba prób: " + str(liczba_prob))
    else:
        print("Liczba podana przez użytkownika jest niepoprawna")
        continue

