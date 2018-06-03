x = 100
i = 0

square = False
done = False

while not done:
    if i**2 == x:
        square = True
    done = True
    if i**2 > x:
        done = True
    i += 1
if square:
    print('x jest kwadratem')
else:
    print('x nie jest kwadratem')

