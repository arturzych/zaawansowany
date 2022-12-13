from abc import ABC, abstractmethod


class A(ABC):
    def func(self):
        print('A')

    @abstractmethod
    def ugotuj_jedzenie(self):
        print('chcę jeść')


class B(A):
    def func(self):
        print('B')

    def ugotuj_jedzenie(self):
        print('gotuje ryz')

    def func_from_b(self):
        print('hello I am in B')


# a = A()
b = B()
print(b.ugotuj_jedzenie())
print(b.func())
print(b.func_from_b())

