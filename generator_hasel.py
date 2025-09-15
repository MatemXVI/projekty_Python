import string
import random
while True:
    try:
        characters = int(input("Podaj liczbę znaków z których ma się składać hasło: "))
    except ValueError:
        print("Proszę podać liczbę!")
    if characters < 5:
        print("Liczba znaków musi być większa od 5")
    is_all_option = [False, False, False, False]
    all_options = False
    while not all_options:
        password = ""
        for i in range(characters):
            random_option = random.randrange(1,5)
            if random_option == 1:
                password +=  random.choice(string.ascii_lowercase)
                is_all_option[0] = True
            elif random_option == 2:
                password += random.choice(string.ascii_uppercase)
                is_all_option[1] = True
            elif random_option == 3:
                password += random.choice(string.digits)
                is_all_option[2] = True
            elif random_option == 4:
                password += random.choice(string.punctuation)
                is_all_option[3] = True
        all_options = all(is_all_option)
    print(password)