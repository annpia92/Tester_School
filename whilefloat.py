

count = 0
x = 0

total=0
while x==0:
    x = int(input('Podaj liczbe'))
    if x >= 0:
        total += x
        count += 1


if count == 0:
    print('x  nie podano liczb ujemnych')
else:
    print(count)
    print(total/count)


