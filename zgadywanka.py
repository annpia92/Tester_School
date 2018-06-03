import random
# print(random.random()) liczba od [0,1)
# print(random,randint(0,10)) liczba calkowita od 0 do 10 wlacznie
# print(random.choice(['a', 'b', 'c']))

def foo():
    print('foo')

def bar():
    print('bar')

func = random.choice([bar, foo])
func()
def int_input(prompt):
    number=None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print("To nie byla liczba...")
    return number

x = int_input('Podaj dolna granice')
y = int_input('Podaj gorna granice')
while x > y :
    print("dolna granica nie moze byc wieksza od gornej")
    x = int_input('Podaj dolna granice')
    y = int_input('Podaj gorna granice')
a = random.randint(x,y)
b = 0
count = 0
while b == 0:
    count += 1
    b=int_input("podaj liczbe")
    if b > a:
        print("za duzo")

    elif b < a:
        print("za malo")

else:
    print("zgadles")
    print('liczba ruchow', count)

