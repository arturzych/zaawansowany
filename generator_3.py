def generator():
    with open('My_ctx_manager_file.txt', 'a') as file:
        for wstawka in file:
            yield wstawka


for x in generator():
    print(x)
