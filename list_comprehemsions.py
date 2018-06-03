#dev_ids = []

#for i in range (1,5):
#    dev_ids.append('device_' + str*(i))

#print(dev_ids)
#print(['device_' + str(i) for i in range (1,5)])

print(['square_' + str(i*i) for i in range (1,100)])
print(*['square_' + str(i*i) for i in range (1,100)])

slownik = [{'id': 1, 'model': "abc"}, {'id': 2, 'model': "def"}, {'id': 3, 'model': "ghi"}]

#zamiast petli uzyc wyrazenia listowego

for record in slownik:
    print(record['id'])


print(record['id'] for record in slownik)

lista = ['asdghk', 'asdetg', 'vvvvvvvvvvvvvvvvvvvvv', 'bbbbbbbbbbbbbb', 'v']


print([len(name) for name in lista])