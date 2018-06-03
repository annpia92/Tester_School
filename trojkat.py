x = float(input('Podaj a'))
y = float(input('podaj b'))
z = float(input('podaj c'))
if x <= 0 or y<= 0 or z <= 0:
    print('co najmniej jedna z warotsci jest ujemna, nie moze byc dlugoscia boku trojkata')
elif x+z>y and z+y>x and y+x>z:
    print(x, y, z, "moga byc bokami torjkata")
else:
    print('nie moga byc bokami trojkata')