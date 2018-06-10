def csv_to_list(input_file):

    lista = []

    for line in input_file:
        rec = line.rstrip("\r\n'").split(',')

        lista.append(rec)
    return lista

if __name__ =="__main__":
    path = input('Podaj sciezke: ')
    try:
        with open(path) as input_file:
            print(csv_to_list(input_file))
    except OSError as err:
         print(err)

#2. wersja
def csv_to_list2(csv_file):
    expected_len = None
    result = []
    for line in csv_file:
        record = line.rstrip('\r\n').split(,)
        if expected_len is None:
            expected_len = len(record)
        elif len(record) != expected_len:
            raise ValueError("malformed CSV file")
        result.append(record)
    return result

#3. wersja
def csv_to_list(csv_file):
    result =[csv_file.readLine()]
    for line in csv_file:
        record = line.rstrip('\r\n').split(',')
        if len(record) != len(result[0]):
            raise ValueError('Malformed CSV file')
        result.append(record)
    return result