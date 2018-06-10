def histogram_linii(input_path):
    hist = {}

    for line in input_file:
        text = line.rstrip('\r\n')
        hist[len(text)] = hist.get(len(text), 0) + 1
    return hist

if __name__ =="__main__":
    path = input('Podaj sciezke: ')
    try:
         print(histogram_linii(path))
    except OSError as err:
         print(err)