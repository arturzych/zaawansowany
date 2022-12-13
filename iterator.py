import random


class CustomIterDict():
    def __init__(self, begin, end, amount):
        self.begin = begin
        self.end = end
        self.amount = amount

    def __iter__(self):
        return self

    def __next__(self):
        if self.amount <= 0:
            raise StopIteration
        else:
            self.amount -= 1
            return random.randint(self.begin, self.end)


#if __name__ == '__main__':
a = CustomIterDict(38, 40, 2)


for _ in a:
    print(_)
