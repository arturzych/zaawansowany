def test():
    a = 5
    return a ** 2


print(test())


def decrement(number):
    return number - 1


a = 3

while a > 0:
    print(decrement(a))
    a = a - 1
print('==========')


def decrement2(number):
    for i in range(number):
        yield number - i


for x in decrement2(8):
    print(x-1)

print('==========')
