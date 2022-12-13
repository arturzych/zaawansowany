def testowy_generator():
    yield 'a'
    yield 'b'
    yield 'v'

a = testowy_generator()
print(type(a))
print(next(a))
print(next(a))
print(next(a))

print(dir(testowy_generator()))

# for x in testowy_generator():
#     print(x)

a = range(10)
print(a)
print(type(a))