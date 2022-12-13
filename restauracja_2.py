from abc import ABC, abstractmethod




class Restauracja(ABC):


    @abstractmethod
    def przygotuj(self):
        pass


class SushiBar(Restauracja):
    def przygotuj(self):
        print('Zwijamy roleczke')


class Kebab(Restauracja):
    def przygotuj(self):
        print('Uzupełniam pite')


class Indyjska(Restauracja):
    def przygotuj(self):
        print('robie Tikka Masala')


sushi = SushiBar()
print(sushi)
sushi.przygotuj()

kebab = Kebab()
print(kebab)
kebab.przygotuj()

indyjska = Indyjska()
print(indyjska)
indyjska.przygotuj()