# def generator():
#     with open('My_ctx_manager_file.txt', 'r+') as file:
#         for wstawka in file:
#             yield wstawka
#         file.write('\nCos takiego')
#
#
# for x in generator():
#     print(x)

# def PowerTwoGen(max=3):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n = n + 1
#
#
# for x in PowerTwoGen():
#     print(x)


def power():
    max = [1, 2, 3]
    for i in max:
        yield 2 ** i


for x in power():
    print(x)
