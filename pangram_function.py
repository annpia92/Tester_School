import string


def is_pangram(text):
    """
    checks if text is a pangram (contains all the characters of the alphabet)
    Args:
        Text string to be checked
    Returns:
        True if the string is a pangram, False otherwise
    """

    text = text.lower()
    for i in string.ascii_lowercase:
        if i not in text:
            return False
            print("nie")
        else:
            return True
            print('tak')


print(is_pangram("jgjgjgjhjjhhjhj"))
print(is_pangram("the quick brown fox jumps over a lazy dog"))


#wydajniejsze rozwiazanie
def is_pangram2(text):
    found_letters = {} #slwonik, slowniki nie przyjmuja duplikatow kluczy
    for char in text.lower():
        if char.isalpha(): #sprawdza czy char jest litera
            found_letters[char]= 0 #wpisuje do slwonika rekord
    if len(found_letters) == len(string.ascii_lowercase)    #jesli liczba rekordow jest rowna dlguosci alfabetu
        return True
    return False