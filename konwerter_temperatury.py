historia_temperatur = []
przeliczona_temperatura = ()

def zapisz_temperature(skala, b_temp, temp2, temp3):
    przeliczona_temperatura = (skala, b_temp, temp2, temp3)
    historia_temperatur.append(przeliczona_temperatura)

def wyswietl_temperatury():
    for temperatury in historia_temperatur:
        for temperatura in temperatury:
            if temperatura == 'C':
                print(temperatura)

        print("--------------")

while True:
    print("Podaj skalę temperatury: C - Celsjusz, F - Fahrenheit, K - Kelvin: 0 oznacza wyjście z programu. 1 - "
          "Wyświetlenie historii temperatur.")
    skala = input()
    skala = skala.capitalize()
    if skala == '0':
        break
    if skala == '1':
        wyswietl_temperatury()
        continue
    if skala != 'C' and skala != 'F' and skala != 'K':
        print("Podaj skalę C, F lub K!")
        continue
    try:
        temp = float(input("Podaj temperaturę: "))
    except ValueError:
        print("Podaj wartość liczbową")
        continue
    if not isinstance(temp, int) and not isinstance(temp, float):
        print("Podaj wartość liczbową!")
        continue
    if skala == 'C':
        tempC = temp
        tempF = tempC * 9 / 5 + 32
        tempK = tempC + 273.15
        print("Przeliczona temperatura:")
        print("Fahrenheit: ", tempF)
        print("Kelvin: ", tempK)
        zapisz_temperature('C', tempC, tempF, tempK)
    elif skala == 'F':
        tempF = temp
        tempC = (tempF - 32) * 5 / 9
        tempK = (tempF + 459.67) * 5 / 9
        print("Przeliczona temperatura:")
        print("Celsjusz: ", tempC)
        print("Kelvin: ", tempK)
        zapisz_temperature('F', tempF, tempC, tempK)
    elif skala == 'K':
        tempK = temp
        tempF = tempK * 9 / 5 - 459.67
        tempC = tempK - 273.15
        print("Przeliczona temperatura:")
        print("Fahrenheit: ", tempF)
        print("Celsjusz: ", tempC)
        zapisz_temperature('K', tempK, tempF, tempC)
