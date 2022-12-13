import json

with open('hotel.json') as plik:
    data = plik.read()
    # print(data)

slownik = json.loads(data)

cena = 0
for room in slownik["hotel"]["rooms"]:
    print(room['price'])
    cena += room['price']
    if room['breakfast']:
        cena += 50

cena += slownik['hotel']['parking']['price']
print(cena)

d = {'zaplata': cena}

with open('rachunek.json', "w") as plik:
    rachunek_json = json.dumps(d)
    plik.write(rachunek_json)


