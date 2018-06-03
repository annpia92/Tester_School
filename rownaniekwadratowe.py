print("podaj wspolczynniki rownania")
x=float(input('Podaj a'))
y=float(input('podaj b'))
z=float(input('podaj c'))
delta = y*y - (4*x*z)
x1 = ((-y)+(delta**0.5))/(2*x)
x2 = ((-y)+(delta**0.5))/(2*x)
x3= (-y)/(2*x)

print('delta wynosi:', (y*y - (4*x*z)))
if delta<0:
    print('delta ujemna, brak rozwiazan')
elif delta==0:
    print(x3)
else:
    print('miejsca zerowe to', x1, x2)