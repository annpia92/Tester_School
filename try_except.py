number = None

while number is None:
    try:
        number = int(input('Podaj liczbe ',))
    except ValueError:
        print("To nie byla liczba...")
print("podales: ", number)