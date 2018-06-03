# print(",", join(['a', 'b', 'c']))
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
            part.append(''.join(current_part))
            current_part = ''
    part.append(''.join(current_part))
    return part

numbers = '1,2333,222,7789,900'
print(split(numbers, ','))