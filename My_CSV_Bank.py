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


    plik = 'lista_operacji.csv'
    with open(plik, 'r') as file:
        data = csv.reader(file, delimiter=';')
        lista = []
        for row in data:
            lista.append(row)
        # print(lista[1:])

        for element in lista[1:3]:
            print(element[3], element[4])


odczyt()

