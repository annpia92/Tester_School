device_names = {1: 'cpu0', 2: 'mem_bank1'}
device_models = {1: "Xeon",2: "Corsair"}

[{'id': 1, "name": "cpu0", "model": 'Xeon'},
 {'id': 2, "name": "mem_bank1", "model": 'Corsair'}]

slownik = []
for id, name in device_names.items():
    model = device_models[id]
    slownik.append({"id_dev": id, "name": name, "model": model})
print(slownik)

slownik2 = []
for id, name in device_models.items():
    model_name = device_models[id]
    slownik.append({"id_dev": name, "name": name, "model": model})
print("slownik2", slownik)

model_map= {}
slownik3 = {} #ma zawierac nazwy przypiasne do modeli, slownik
for id, model in device_models.items():
    if model in model_map:
        model_map[model].append(device_names[id])
    else:
        model_map[model] = [device_names[id]]

print("modelmap", model_map)