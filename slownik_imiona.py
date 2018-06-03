data = [{"first_name": "John", "last_name": "Doe", "height": 173},
        {"first_name": "Mike", "last_name": "Don", "height": 176},
        {"first_name": "Henry", "last_name": "Kovalsky", "height": 143},
        {"first_name": "John", "last_name": "Novak", "height": 193}]

total = 0
for record in data:
   total += (record['height'])
   mean=total/(len(data))
print(mean)

heights_by_name = {}
for record in data:
    if record["first_name"] in heights_by_name:
        heights_by_name[record['first_name']].append(record["height"])
    else:
        heights_by_name[record['first_name']] = [record["height"]]

print(heights_by_name)

for name, height in heights_by_name.items():
    print(name, sum(height)/len(height))

total_by_name= {}
count_by_name ={}

for record in data:
    if record["first_name"] in total_by_name:
        total_by_name[record["first_name"]] += record["height"]
        count_by_name[record["first_name"]] += 1
    else:
        total_by_name[record["first_name"]] = record["height"]
        count_by_name[record["first_name"]] = 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])

for record in data:

        total_by_name[record["first_name"]] = total_by_name.get(record["first_name"],0) + record["height"]
        count_by_name[record["first_name"]] = count_by_name.get(record["first_name"], 0) + 1

for name, total in total_by_name.items():
    print('to jest z ostniej petli', name, total / count_by_name[name])