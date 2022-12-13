from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, legs, fins, voice, age, jaws):
        self.legs = legs
        self.fins = fins
        self.voice = voice
        self.age = age
        self.jaws = jaws

    @abstractmethod
    def species_of_animal(self):
        pass

    def move_of_animal(self):
        pass

    def voice_of_animal(self):
        pass

    def age_of_animal(self):
        pass

    # należy pamiętać aby nazwy metod abstrakcyjnych nie były takie same jak nazwy pól w klasie

    def introduce(self):
        print(f'Cześć jestem {self.species_of_animal()}, {self.move_of_animal()}')
        print(self.voice_of_animal())
        print(self.age_of_animal())
        print('**************************************')


class Lion(Animals):
    def __init__(self, legs, voice, age):
        super().__init__(legs=4, voice='ryk', fins=0, age=5, jaws=None)
        # nie muszą być ustalone zmienne w powyższych argumentach, można zdefiniować wszędzie None
        self.legs = legs
        self.voice = voice
        self.age = age

    def species_of_animal(self):
        return 'Lew Simba'

    def move_of_animal(self):
        return f'biegnę za antylopą bo mam {self.legs} silne lapy i zachowuję koordynację ruchową.'

    def voice_of_animal(self):
        return f'Dopadam swoją ofiarę, wydając głośny {self.voice}.'

    def age_of_animal(self):
        return f'Moj wiek to {self.age} lat, więc jestem doskonałym przywódcą stada'


class Wolf(Animals):
    def __init__(self, legs, voice, jaws, age):
        super().__init__(legs=4, voice='przerażająco wyjąc', jaws='silne szczęki', fins=0, age=2)
        # nie muszą być ustalone zmienne w argumentach
        self.legs = legs
        self.voice = voice
        self.jaws = jaws
        self.fins = None
        self.age = age

    def species_of_animal(self):
        return 'Wilk'

    def move_of_animal(self):
        return f'biegnę gdy poluje na zające, korzystam z szybkich {self.legs} łap, na większe ofiary jak jelenie ' \
               f'poluję z rodziną. \nBiada kiedy moje {self.jaws} dopadną zdobycz.'

    def voice_of_animal(self):
        return f'Porozumiewam się i ostrzegam, wydając głośne {self.voice}.'

    def age_of_animal(self):
        return f'Mój wiek to {self.age} lata, więc jestem sprytny, szybki i czujny'


class Elephant(Animals):
    def __init__(self, legs, voice, age, jaws):
        super().__init__(legs=None, voice=None, age=None, fins=None, jaws=None)
        self.legs = legs
        self.voice = voice
        self.age = age
        self.jaws = jaws

    def species_of_animal(self):
        return 'Jestem Słoń Dumbo'

    def move_of_animal(self):
        return f' przemieszczam się wolno przez pustynię na {self.legs} silnych nogach, opiekując się innymi. ' \
               f' Odganiam wszystkich, którzy próbują przeszkadzać. \nMoje {self.jaws} ' \
               f'potrafią skutecznie powstrzymać atak narwańców.'

    def voice_of_animal(self):
        return f'Porozumiewam się za pomocą dźwięków przypominających {self.voice}.'

    def age_of_animal(self):
        return f'Mój wiek to {self.age} lat więc jestem dostojnym przewodnikiem stada'


class Seal(Animals):
    def __init__(self, legs, fins, voice, age, jaws):
        super().__init__(legs, fins, voice, age, jaws)

    def move(self):
        print("Wskakuję do wody")


lew = Lion(legs=4, voice='ryk', age=5)
# powinny być zmienne w argumentach jeśli chcemy ich użyć dalej w opisach
lew.introduce()

wilk = Wolf(legs=4, voice='przerażające wycie', age=2, jaws='silne szczęki')
wilk.introduce()

slon = Elephant(legs=4, voice='trąbienie', age=20, jaws='2 duże kły')
slon.introduce()
# slon = Elephant()
# slon.move()
#
# foka = Seal()
# foka.move()
#
# zwierz = Animals()
# zwierz.move()
