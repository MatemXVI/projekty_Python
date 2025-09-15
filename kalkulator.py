import os

print("--------- KALKULATOR ------------")

def read_operations():
    filename = input("Podaj nazwę pliku(plik może być wyłącznie z rozszerzeniem .txt): ")
    operations = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("Lista wykonanych działań: ")
            for line in lines:
                print(line.strip())
                operations.append(line.strip())
            print("Plik pomyślnie wczytany. Następne działania będziesz mógł zapisać do pliku")
        return operations
    except FileNotFoundError:
        print("Brak pliku. Plik możesz utworzyć po wykonaniu działań.")
        return operations

def write_operations(lines):
    filename = input("Podaj nazwę(z rozszerzeniem .txt) : ")
    if filename[-4:] != ".txt":
        print("Plik musi mieć rozszerzenie .txt!")
        return
    if os.path.exists(filename):
        option = input("Plik już istnieje! Czy chcesz zapisać do tego pliku (T)")
        if option.lower() != 't':
            return
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    return True;

option = input("Czy chcesz wczytać dane z pliku? Naciśnij T jezeli chcesz to zrobić lub dowolny klawisz aby przejść do wykonywania działań: ")
if option.lower() == 't':
    operations = read_operations().copy()
else:
    operations = []
while True:
    operation = input("Podaj działanie matematyczne. Pamiętaj by każdy składnik działania pisać po spacji, w formie 2 + 2 a nie 2+2! Możesz podać tylko jedno działanie na raz! ")
    parts = operation.split()
    if len(parts) != 3:
        print("Niepoprawny format!")
        continue
    try:
        a = int(parts[0])
        sign = parts[1]
        b = int(parts[2])
    except ValueError:
        print("Nie podano liczby")
        continue
    if sign not in ['+', '-', '*', '/']:
        print("Podano niepoprawny znak!")
        continue
    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '*':
        result = a * b
    elif sign == '/':
        if b != 0:
            result = a / b
        else:
            print("Nie można wykonać dzielenia!")
            continue
    operation += " = " + str(result)
    operations.append(operation)
    print("Wynik działania " + operation)
    option = input("Jeżeli chcesz wyjść z programu naciśnij T bądź inny klawisz jeśli chcesz zostać. Jeżeli chcesz wyświetlić listę działan naciśnij 0 ")
    if option.lower() == 't':
        print("Trwa wychodzenie z programu...")
        quit()
    elif option == '0':
        print("Lista wykonanych działań: ")
        for operation in operations:
            print(operation)
        option = input("Czy chcesz zapisać wyniki do pliku? Naciśnij T jeżeli chcesz to zrobić. Naciśnij 0 jeżei chcesz wyjść z programu. Naciśnij dowolny klawisz jeżeli chcesz kontynuować ")
        if option.lower() == 't':
            if write_operations(operations):
                print("Dane pomyślnie zapisano do pliku.")
            option = input("Czy chcesz wyjść z programu(T)? ")
            if option.lower() == 't':
                quit()
        elif option == '0':
            quit()
        else:
            continue
