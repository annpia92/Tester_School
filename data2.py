month_length=[31,28,31,30,31,30,31,31,30,31,30,31]
day=int(input('Podaj dzien w formie liczby od 1 do 31'))
month=int(input('Podaj miesiac w formie liczby od 1 do 12'))
year=int(input('Podaj rok w formie liczby XXX'))

today_date = [day, month, year]


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    przestepny= True

for month == 1 or month == 3 or month == 5 or month == 7 or month ==  or month == 10 or month == 12:
    for day in range(1,30):
        next_day=day+1
        next_month=month
        next_year = year
    else:
        next_day=1
        if month==12:
            next_month = 1
            next_year = year
        else:
            next_month=month+1
            next_year=year+1
for month==4 or==4or 9 or 11:
    for day in range(1,29):
        next_day=day+1
        next_month = month
        next_year = year
    else:
        next_day=1
        next_month = month+1
        next_year = year
for month==2:
    if not przestepny:
      for day in range(1,27):
        next_day=day+1
        next_month = month
        next_year = year
      else:
        next_day=1
        next_month = month+1
        next_year = year
    else:
        for day in range(1, 28):
            next_day = day + 1
            next_month = month
            next_year = year
        else:
            next_day = 1
            next_month = month+1
            next_year = year

tommorrow_date = [next_day, next_month, next_year]
print('jutrzehsza data to ', tommorrow_date)