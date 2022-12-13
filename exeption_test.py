'''a = {}
try:
    print(a['asdfg'])
    print('============================')
except IndexError:
    print('blanddddddddddddddddddd')
except ArithmeticError:
    print('blad arymetyczny')
except ZeroDivisionError:
    print('to jest key error')

print('+++++++++++++++')'''

a = input('Podaj liczbe 1: ')
b = input('Podaj liczbe 2: ')

try:
    c = (int(a) / int(b))

    print(float(c))
except ZeroDivisionError:
    print('nie dzielimy przez zero')
