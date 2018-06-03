x = float(input('Podaj a'))
y = float(input('podaj b'))
z = float(input('podaj c'))
if x <= y or y <= z:
     print('mediana wynosi', y)
elif y <= x <= z or z<= x <=y:
     print('mediana wynosi', y)

else:
     print('mediana wynosi ', z)