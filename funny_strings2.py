"""
Module for funny strings manipulations
"""
def bubbleize(text:str):
    #zamienia co druga litere na duza, co druga na mala
    text2 = []
    for i, char in enumerate(text):
        if i%2:
            text2.append(char.lower())
        else:
            text2.append(char.upper())
    return text2

def randomize(text):
    # zwraca lancuch znakow powstaly z text poprzez losowe ustawienie wielkosci znakow w text
    for i, char in enumerate(text):

        if randint(0,1): #sprawdzic  co jest nie tak z randomize (najpierw trzeba zimportowac random)
            text2.append(char.lower())
        else:
            text2.append(char.upper())
    return text2

def numberize(text):
     # zamienia e na 3, o na 0 itd
    text2 = []
    for i, char in enumerate(text):
        if char=='e':
            text2.append('3')
        elif char=='o':
            text2.append('0')
        else:
            text2.append(char)
    return text2

#nie nalezy wpisywac polecen wykonywalnych w modulach
#moduly importuje sie poprzez import modul
#print(bubbleize("aaaaaaaaaaaaaaaa"))
#print(randomize("aaaaaaaaaaaaaaaa"))
#print(numberize("aaeretgeouoaaeaeooooaaaa"))