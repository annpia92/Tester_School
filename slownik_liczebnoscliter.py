def histogram_letters(text):
    #slownik = {'a': 4, 'b': 4, 'others': 68}
    slownik = {}
    text = text.lower()

    for char in text.lower():

        if char.isalpha(): #sprawdza czy char jest litera

            slownik[char]= slownik.get(char, 0) +1  #wpisuje do slownika rekord

        else:
            slownik['others'] = slownik.get(char, 0) +1

    return print("to jest histogram wystepowania liter", slownik)

print(histogram_letters("alalalalvdfsigjerotgi"))

#prawidlowe rozwiazanie

def histogram(text):
    hist = {}
    for chat in text.lower():
        if char.isalpha():
            hist[char] = hist.get(char, 0) + 1
        else:
            hist['others'] = hist.get('others', 0) + 1

    return hist
