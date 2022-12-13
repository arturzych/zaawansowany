import csv

with open('cities.csv') as file:
    data = csv.reader(file)
    print(data)
    data_list = list(data)
    print(data_list)

    # for row in data:
    #     print(row)