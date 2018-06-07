def extract_personal_data(x):
        p = (x[6:9])  # 7,8,9,10 pozycja numeru PESEL - informacja o płci
        if int(p)%2 == 0:  # liczby parzyste
            plec = "F - kobieta" # liczby parzyste - płeć: kobieta
        else:
            plec = "M - mezczyzna" # liczby nieparzyste - płeć: mężczyzna
        import correct_date
        y=correct_date.extractDate(x)
        data_ur=str(y[0])+'.'+str(y[1])+'.'+ str(y[2])
        dane_osobowe = {"PESEL": x, "date_of_birth": data_ur, "sex": plec}
        return dane_osobowe