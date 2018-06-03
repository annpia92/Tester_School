month_length=[31,28,31,30,31,30,31,31,30,31,30,31]
day=int(input('Podaj dzien w formie liczby od 1 do 31'))
month=int(input('Podaj miesiac w formie liczby od 1 do 12'))
year=int(input('Podaj rok w formie liczby XXX'))

today_date = [day, month, year]

next_year= year + 1
for month==1 or ==3 or==5 or ==7 or == or ==10 or ==12:
    for day in range(1,30):
        next_day=day+1
    else:
        next_day=1
for month==4 or==4or 9 or 11:
    for day in range(1,29):
        next_day=day+1
    else:
        next_day=1
for month=2:
    for day in range(1,27):
        next_day=day+1
    else:
        next_day=1

tommorrow_date = [next_day, next_month, next_year]
print(tommorrow_date)