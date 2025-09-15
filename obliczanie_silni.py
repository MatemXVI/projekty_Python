def silnia(liczba):
    for i in range(1, liczba):
        liczba *= i
    return liczba


def potega(podstawa, wykladnik):
    wynik = podstawa
    if wykladnik == 0:
        wynik = 1
    if wykladnik < 0:
        wynik = 1/wynik
        for i in range(1, wykladnik):
            wynik *= podstawa
    if wykladnik >= 1:
        for i in range(1, wykladnik):
           wynik *= podstawa
    return wynik

print("OBLICZANIE POTĘGI I SILNI")
lista_wynikow = {}
while True:
    podstawa = int(input("Podaj podstawę: "))
    if podstawa == 0:
        print(lista_wynikow)
        continue
    wykladnik = int(input("Podaj wykładnik: "))
    wynik_potega = potega(podstawa, wykladnik)
    wynik_silnia = silnia(podstawa)
    print(str(podstawa) + " do potęgi " + str(wykladnik) + " to", wynik_potega)
    print("Silnia z " + str(podstawa) + "! wynosi", wynik_silnia)
    lista_wynikow[podstawa] = {"potega": wynik_potega, "silnia": wynik_silnia}
    print("Wpisz 0 jako podstawę żeby wyświetlić wszystkie wyniki")
