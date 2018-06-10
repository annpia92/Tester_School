import json

data = {"spam": [1, 2, 3], 'eggs': {'a': 2, "b": 3}}
serialized = json.dumps(data) #dumps zrzuca lancuch znakow (s na koncu od string)
print(data)
print(serialized)
data2 = json.loads(serialized)  #loads# laduje lancuch znakow (s na koncu od string)
print(data2)

with open('data.json', 'wt') as json_file:
    json.dump(json_file)

with open('data.json', 'rt') as json_file:
    json.load(json_file)