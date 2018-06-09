""""
Checks if the given PESEL number is valid; if so, returns user's date of birth and gender
"""

import psl
import validation

if __name__ == "__main__":
    try:
        x = str(input('Podaj swoj numer PESEL: '))
        if validation.validate(x) == False:
            raise Exception('Wpisales nieprahwidlowy numer PESEL')
        y = psl.extract_personal_data(x)
        print("Data urodzenia: ", y["date_of_birth"], "Plec: ", y["sex"])
    except Exception as error:
        print('Wystapil nastepujacy blad: ' + repr(error))

