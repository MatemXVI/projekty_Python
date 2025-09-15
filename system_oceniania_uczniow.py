liczba_uczniow = int(input("Podaj liczbę uczniów: "))
if liczba_uczniow < 1:
    print("Liczba uczniów musi wynosić więcej niż zero!")
uczniowie = {}
for i in range(1, liczba_uczniow+1):
    print("Uczeń " + str(i))
    imie = input("Imię: ")
    mat_ocena = float(input("Ocena z matematyki: "))
    pol_ocena = float(input("Ocena z polskiego: "))
    ang_ocena = float(input("Ocena z angielskiego: "))
    srednia = (mat_ocena + pol_ocena + ang_ocena)/3
    uczniowie[imie] = round(srednia, 2)
print("Wyniki: ")
for imie, srednia in uczniowie.items():
    if srednia > 1.75:
        print(imie + " - Średnia: " + str(srednia) + " - ZDAŁ(A)")
    else:
        print(imie + " - Średnia: " + str(srednia) + " - NIE ZDAŁ(A)")
naj_uczen, naj_srednia = max(uczniowie.items(), key=lambda x: x[1])
print("Najlepszy uczeń: " + naj_uczen +"(" + str(naj_srednia) + ")")

