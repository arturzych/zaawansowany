import csv
import os


def csv_search():
    for file in os.listdir("C:\\Users\\48509\\PycharmProjects\\zaawansowany"):
        if file.endswith(".csv"):
            print(os.path.join(file))


def business_logic():
    lista = []
    for row in data:
        lista.append(row)
    # print(lista[1:3])

    # for value in lista[1:3]:
    #
    #     print(value.keys())

    for element in lista[0:3]:

        # print(element['Kategoria'], element['Kwota operacji'])
        # print(element[4], element[5])
        txt = '-'.join(element)
        # print(txt)
        txt_split = txt.split('-')
        # print(txt_split)
        for i in txt_split:
            if 'Kat' in i:

                print(i, element[i])
            elif 'Kwot' in i:

                print(i, element[i])


plik = 'lista_operacji_2.csv'

try:
    with open(plik, 'r', encoding='utf-8') as file:  # encoding='utf-8'
        data = csv.DictReader(file, delimiter=';')  # csv.DictReader po nazwie kolumny
        # data = csv.reader(file, delimiter=';')  # csv.reader po nr kolumny
        business_logic()

except UnicodeDecodeError:
    with open(plik, 'r') as file:  # encoding='utf-8'
        data = csv.DictReader(file, delimiter=';')  # csv.DictReader po nazwie kolumny
        # data = csv.reader(file, delimiter=';')  # csv.reader po nr kolumny
        business_logic()

csv_search()


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