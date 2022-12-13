from abc import ABC, abstractmethod
from random import randint


class Basic(ABC):
    login = 'Me'

    def __init__(self, login):
        self.login = login
        self.life = 100, 100
        self.intelligence = 10, 10
        self.strength = 10, 10

    x = randint(-1, 1)

    iq_character = 0, 0
    life_character = 0, 0
    strength_character = 0, 0

    if x == -1:
        iq_character = randint(-20, -1), randint(-5, -1)
        life_character = randint(-80, -1), randint(-200, -1)
        strength_character = 0, randint(-30, -1)
    elif x == 0:
        iq_character = iq_character
        life_character = life_character
        strength_character = strength_character
    else:
        iq_character = randint(1, 20), randint(1, 5)
        life_character = randint(1, 10), randint(1, 10)
        strength_character = 0, randint(1, 30)

    @abstractmethod
    def attack(self):
        pass

    def introduce(self):
        pass

    def statistics(self):
        print(f'{self.introduce()} is under attack!!!! \nActual intelligence is: {self.attack()[0]}')
        print(f'Level of life is: {self.attack()[1]}')
        print(f'Strength: {self.attack()[2]}')


class Witcher(Basic):
    def __init__(self, login):
        super().__init__(login)
        print('\n*******', Basic.x)
        self.w_intelligence = Basic.iq_character[0]
        self.w_life = Basic.life_character[0]

    def attack(self):
        whole_intelligence = self.intelligence[0] + self.w_intelligence
        whole_life = self.life[0] + self.w_life
        return whole_intelligence, whole_life, None

    def introduce(self):
        Witchers = 'Witcher_1', 'Witcher_2', 'Witcher_3', 'Witcher_4', 'Witcher_5'
        return Witchers[randint(-5, 4)]


class Dwarf(Basic):
    def __init__(self, login):
        self.d_intelligence = Basic.iq_character[1]
        self.d_life = Basic.life_character[1]
        self.d_strength = Basic.strength_character[1]
        super().__init__(login)

    def attack(self):
        whole_intelligence = self.intelligence[1] + self.d_intelligence
        whole_life = self.life[1] + self.d_life
        whole_strength = self.strength[1] + self.d_strength
        return whole_intelligence, whole_life, whole_strength

    def introduce(self):
        Dwarfs = 'Dwarf_1', 'Dwarf_2', 'Dwarf_3', 'Dwarf_4', 'Dwarf_5'
        return Dwarfs[randint(-5, 4)]


class ExtraCharacter(Basic):
    pass


w = Witcher(login="Me")
w.statistics()

print()
d = Dwarf(login="Me")
d.statistics()
