my_file = None
try:
    my_file = open('plik.txt', 'rt')
    data = my_file.read()
    print(data)

except OSError as err:
    print("Error: ", str(err))

finally:
    if my_file is not None:
        print('zamykam')
        my_file.close()

try:
    with open('plik.txt') as my_file:
        print(my_file.read())
except OSError as err:
    print(err)

def reverse_File(input_path, output_path):

    with open(input_path, 'rt') as input_file:
        data=input_file.read()
    with open(output_path, 'wt') as output_file:
        output_file.write(data[::-1])


    reverse_File('plik.txt', 'output_file.txt')

with open('plik.txt') as my_file:
    lines = (my_file.readlines()) #wczytanie wszystkich linii, razem ze znakami konca linii /n
    print(lines)

with open('plik.txt') as my_file:
    for line in my_file:
        print(line)

text = 'some text'
print(text.rstrip('t')) #wychodzi wyprintowane 'some tex', usuwa t od prawej str

