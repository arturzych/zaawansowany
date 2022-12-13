import csv


with open('ford_escort.csv', 'r') as file:
    data = csv.reader(file)
    print(data)

    data_list = list(data)
    print(data_list)

    suma = 0
    for row in data_list[1:]:   # dla każdego wiersza począwszy od nr 2 w kolejności
        a, b = row[2], row[1]   # dodałem wartość b czyli drugiej kolumny każdego wiersza
        print(a, b)
        suma = round((suma + float(a)), 2)

    print(len(data_list[1:]))
    print('Srednia cena Forda ESCORT to: ', round((suma / len(data_list[1:])), 2))
