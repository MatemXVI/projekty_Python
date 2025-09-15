zdanie_normalne = []
zdanie = input("Podaj zdanie: ").lower()
for char in zdanie:
    if char != " ":
        zdanie_normalne.append(char)

odwrocone_zdanie = zdanie_normalne.copy()
odwrocone_zdanie.reverse()
if odwrocone_zdanie == zdanie_normalne:
    print("To zdanie jest palindromem!")
else:
    print("To zdanie nie jest palindromem!")