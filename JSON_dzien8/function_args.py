def foo(x, y, *args, **kwargs): #z podanych argumentow zostanie ulozony slwonik
    print(kwargs)
    print(args)
    print(x, y)

foo(x=1, y = 2, first_name="Adam", age=100)

