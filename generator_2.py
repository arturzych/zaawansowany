def generator():
    slowo = 'generator'

    for litera in slowo:
        yield litera


for x in generator():
    print(x)


print('-------------')
print(next(generator()))
print(next(generator()))
print(next(generator()))
print(next(generator()))
print(next(generator()))
print(next(generator()))
