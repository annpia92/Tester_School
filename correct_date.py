
def val_checksum(x):  # Funkcja służąca do walidacji wg sumy kontrolnej
    x1 = x[10]
    sum = ((1 * int(x[0])) + (3 * int(x[1])) + (7 * int(x[2])) + (9 * int(x[3])) + ((1 * int(x[4]))) + (
                3 * int(x[5])) + (7 * int(x[6])) + (9 * int(x[7])) + (1 * int(x[8])) + (3 * int(x[9])))
    check1 = 10 - (sum % 10)
    check2 = check1 % 10
    if check2 == int(x1):
        return True
    else:
        return False

def extractDate(x):

    p = (x[6:9])  # 7,8,9,10 pozycja numeru PESEL - informacja o płci
    r = (x[0:2])  # 1 i 2 pozycja numeru PESEL - informacja o dwóch ostatnich cyfrach roku urodzenia
    m = (x[2:4])  # 3 i 4 pozycja numeru PESEL - informacja o miesiącu urodzenia
    d = (x[4:6])  # 5 i 6 pozycja numeru PESEL - informacja o dniu urodzenia

    ym = '';
    ypr = '';
    if int(p) % 2 == 0:  # liczby parzyste
        plec = "F - kobieta"  # liczby parzyste - płeć: kobieta
    else:
        plec = "M - mezczyzna"  # liczby nieparzyste - płeć: mężczyzna

    if 0 < int(m) <= 12 and int(d) <= 31:  # warunek dla lat 1900 - 1999
        ypr = 1900  # początek stulecia
        ym = int(x[2:4])
    elif 22 < int(m) <= 32 and int(d) <= 31:  # warunek dla lat  2000 - 2099 (liczba dot. miesiąca pow. o 20)
        ypr = 2000  # początek stulecia
        ym = ((int(x[2:4])) - 20)
    elif 81 < int(m) <= 92 and int(d) <= 31:  # warunek dla lat  1800 - 1899 (liczba dot. miesiąca pow. o 80)
        ypr = 1800  # początek stulecia
        ym = ((int(x[2:4])) - 80)
    result = [d, ym, ypr + int(r), plec]
    return result

def correctDate(x):
    result = extractDate(x);
    if (result[2] % 4 == 0 and result[2] % 100 != 0) or result[2] % 400 == 0:
        przestepny = True
    else:
        przestepny = False

    if  result[1] == 1 or result[1] == 3 or result[1] == 5 or result[1] == 7 or result[1] == 8 or result[1] == 10 or result[1] == 12 and result[0] >= 31:
        return True
    elif result[1] == 4 or result[1] == 6 or result[1] == 9 or result[1] == 11 and result[0] >= 30:
        return True
    elif result[1] == 2  and przestepny == True and result[0] == 29:
        return True
    elif result[1] == 2  and przestepny == False and result[0] == 28:
        return True
    else:
        return False

def not_empty(x):
    if len(x) != 0:
        return True
    else:
        return False

def length_pesel(x):
    if len(x) == 11:
        return True
    else:
        return False


def is_positiveNumber(x):
    try:
        if int(x)>0:
            return True
        else:
            return False;
    except Exception:
        return False

