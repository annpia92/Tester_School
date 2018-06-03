numbers = '1,2333,222,7789,900'
def split(text, sep):
    #co ma wyjsc: separator przecinek
       # numbers = '1,2333,222,7789,900'
        # a ma byc lista = ['1', '2333', '222', '7789', '900']
    lista = []
    part = []
    text = text.lower()
    current_part = ' '
    for char in text.lower():

        if char != sep:  # sprawdza czy char jest przecinkiem
                current_part += char


        else:
            part.append(current_part)
            current_part = ''
    part.append(current_part)
    return part

numbers = '1,2333,222,7789,900'
print(split(numbers, ','))

#inna wersja

def split2(text, sep):
    parts = []
    start = 0
    for current, char in enumerate[text]:
        if char == sep:
            parts.append(text[start.current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split2(numbers, ','))