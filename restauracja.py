from abc import ABC, abstractmethod


class Restauracja(ABC):
    def __init__(self, kawa, zupa, filet, kebab, twister, lody, burger):
        self.coffee = kawa
        self.soup = zupa
        self.chicken = filet
        self.kebab = kebab
        self.twister = twister
        self.ice_cream = lody
        self.burger = burger





    def daj_jesc(self, Burger_King, Mc_Donalds, Bazyliszek, Besova):
        self.food = Mc_Donalds, Burger_King, Bazyliszek, Besova
        self.drink = Mc_Donalds, Bazyliszek, Besova
        self.dessert = Besova
class

class Club(Restauracja):
    def eat(self):
        print(f'Obiad mozesz zjesc w {self.food}')
        print('\n ')

club = Club()
print(club.coffee)
