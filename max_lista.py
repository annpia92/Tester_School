lista = [1,2,3,4,5,6,67,7,8,90]
i=0
for idx, value in enumerate(lista):
    if idx == 0:
        current_min = value
        current_max = value
    elif current_max < value:
         current_max = value
    elif current_min > value:
         current_min = value

print("max", current_max)
print("min", current_min)

