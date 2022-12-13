import csv, os


# plik = 'lista_operacji.csv'
# with open(plik, 'r') as file:
#     data = csv.reader(file, delimiter=';')
#     print(data)
#
#     lista = []
#     for row in data:
#         lista.append(row)
#     # print(lista[1:])
#
#     for element in lista[1:3]:
#         print(element[3], element[4])

def odczyt():
    for file in os.listdir("c:\\Users\\Artur\\PycharmProjects\\zaawansowany"):
        if file.endswith(".csv"):
            print(os.path.join(file))


    plik = 'lista_operacji_2.csv'
    with open(plik, 'r', encoding='utf-8') as file:  # encoding='utf-8'
        data = csv.DictReader(file, delimiter=';')  # csv.DictReader po nazwie kolumny
        # data = csv.reader(file, delimiter=';')  # csv.reader po nr kolumny
        lista = []
        for row in data:
            lista.append(row)
        # print(lista[1:])

        for element in lista[1:3]:

            print(element['Kategoria'], element['Kwota operacji'])
            # print(element[4], element[5])


odczyt()

