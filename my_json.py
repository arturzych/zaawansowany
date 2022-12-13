import json

a = {
    'a': True,
    'b': None,
    'c': False,
    'd': [1, 2, 3],
    'e': {1: 1}
}

with open('example.json', 'w') as plik:
    json_tekst = json.dumps(a)
    print(json_tekst)
    print(type(json_tekst))
    plik.write(json_tekst)
    # json.dump(a, plik)


with open('example.json') as plik:
    dane_plik = plik.read()
    print(dane_plik)
    slownik = json.loads(dane_plik)
    print(slownik)
    print(type(slownik))