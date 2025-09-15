print("--------- KALKULATOR ------------")

def read_operations():
    filename = input("Podaj nazwę pliku: ")
    operations = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("Lista wykonanych działań: ")
            for line in lines:
                print(line.strip())
                operations.append(line.strip())
            print("Następne działania będziesz mógł zapisać do pliku")
        return operations
    except FileNotFoundError:
        print("Brak pliku. Plik możesz utworzyć po wykonaniu działań.")
        return operations

def write_operations(lines):
    filename = input("Podaj nazwę : ")
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

option = input("Czy chcesz wczytać dane z pliku? Naciśnij T jezeli chcesz to zrobić lub dowolny klawisz aby przejść do wykonywania działań: ")
if option.lower() == 't':
    operations = read_operations().copy()
else:
    operations = []
while True:
    try:
        a = int(input("Podaj pierwszą liczbę: "))
    except ValueError:
        print("Wartośc którą podałeś musi być liczbą!")
        continue
    operation = str(a) + " "
    print("Podaj znak operacji (+, -, *, /): ")
    sign = input(operation)
    if sign not in ['+', '-', '*', '/']:
        print("Podano niepoprawny znak!")
        continue
    operation += sign + " "
    print("Podaj drugą liczbę: ", end="")
    b = int(input(operation))
    operation += str(b) + " "
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
    operation += "= " + str(result)
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
        option = input("Czy chcesz zapisać wyniki do pliku? Naciśnij T jeżeli chcesz to zrobić. Naciśnij 0 jeżei chcesz wyjść z programu ")
        if option.lower() == 't':
            write_operations(operations)
            option = input("Dane pomyślnie zapisane do pliku. Czy chcesz wyjść z programu(T)? ")
            if option.lower() == 't':
                quit()
        elif option == '0':
            quit()
