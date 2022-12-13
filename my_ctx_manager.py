# class MyCtxManager:
#     def __init__(self, nazwa_pliku, mode):
#         self.nazwa_pliku = nazwa_pliku
#         self.mode = mode
#         self.obiekt_plikowy = None
#
#     def __enter__(self):
#         self.obiekt_plikowy = open(self.nazwa_pliku, self.mode)
#         return self.obiekt_plikowy
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.obiekt_plikowy.close()
#
#
# with MyCtxManager("My_ctx_manager_file.txt", "w") as file:
#     file.write('Hurra cos sie zadzialo')

from random import randint
class MyCtxManager:
    def __init__(self, nazwa_pliku, mode):
        self.nazwa_pliku = nazwa_pliku
        self.mode = mode
        self.obiekt_plikowy = None

    def __enter__(self):
        self.obiekt_plikowy = open(self.nazwa_pliku, self.mode)
        return self.obiekt_plikowy

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obiekt_plikowy.close()


with MyCtxManager("My_ctx_manager_file.txt", "w") as file:
    for _ in range(149796):  # znak = 1,4B czyli 748 983 znaki/1MB
        a = randint(20000, 99999)
        print(a)
        file.write('\n' + str(a))



