def foo():
    print('*******')


b = lambda: print('hello world')

print(b)
print(type(b))

print(foo)
print(type(foo))

b()

c = lambda x: x*x
print(c(7))
d = c(7)
print(d)

e = lambda x, y: x*y
print(e(7,8))

print(b,c,e)