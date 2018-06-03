def square(x):
    return x**2

y = square(3) #lub y = square(x=3)
print(y)

def power (exponent, base):
    return base ** exponent

print(power(2,3))
print(power(base=3, exponent=2))
#argumenty mozna pomieszac, ale zawsze przez nazwe beda po wszystkich pozycyjnych


def is_palindrome(text):
        if str(text) == reversed(str(text)):
            #return palindrome = True
            print('to jest palindrom')
        else:
            #return palindrome = False
            print('to nie jest palidrom')

print(is_palindrome("oko"))

def is_palindrome1(text):
    """
    checks if text is a palindrome
    Args:
    text string to be checked
    Returns:
        True if the string is a palindrome, False otherwise
    """
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text)-2-1]:
            return False
        return True

print(is_palindrome1("oko"))

def is_pangram(text):
    """
    checks if text is a pangram (contails all the characters of the alphabet)
    Args:
    text string to be checked
    Returns:
        True if the string is a pangram, False otherwise
    """
    import string
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text)-2-1]:
            return False
        return True