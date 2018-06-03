def factorial(n):
    if n < 0:
        raise ValueError('Factorial is defined only for non-negative numbers')
    result = 1

    for i in range(1,n+1):
        result *= i
    print('silnia wynosi', result)
factorial(9)