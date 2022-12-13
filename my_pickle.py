# import pickle
#
# a = [[4], 6]
#
# with open('pickle', 'wb') as file:
#     ogor = pickle.dumps(a)
#     file.write(ogor)
#
# print('zapisalem')

# serializacja

import pickle

lista = [x for x in range(0, 11)]
print(lista)
with open('pickle', 'wb') as file:
    lista1 = pickle.dumps(lista)
    file.write(lista1)

# deserializacja

with open('pickle', 'rb') as file:
    # dane = pickle.load(file)
    ogor = file.read()
    print(ogor)
    dane = pickle.loads(ogor)
    print(dane)