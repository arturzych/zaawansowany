# Parzyste(0, 10)
# 0,2,4,6,8

"""
Parzyste(0,4) -> 0,2
Parzyste(1,4) -> 2
Parzyste(0,5) -> 0,2,4
Parzyste(1,5) -> 2,4


"""


class Parzyste:
    def __init__(self, begin, end):
        if begin % 2 == 0:
            self.begin = begin
        else:
            self.begin = begin + 1
        self.end = end
        #self.krok = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.end + 2:
            raise StopIteration
        else:
            stan = self.begin
            self.begin += 2
            return stan

"""
Parzyste(0,4) -> 0,2
Parzyste(1,4) -> 2
Parzyste(0,5) -> 0,2,4
Parzyste(1,5) -> 2,4
"""
a = Parzyste(0, 12)
print(a)

for liczba in a:
    print(liczba)