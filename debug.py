from datetime import datetime


def disable_at_night(func):
    # dekorator, który wywołuje udekorowaną funkcję tylko w ciągu dnia
    print('jestem w disable_at_night')
    def wrapper():
        print('jestem w jestem we wrapper w disable_at_night')
        if 7 <= datetime.now().hour < 20:
            func()
            print('skonczylem funkcje we wrapper')
    print('zwracam wrapper')
    return wrapper


@disable_at_night
def say_something():
    print('jestem w funkcji say_something')
    print("Hello world")

print('dzien dobry zaczynamy debug dekoratora')
say_something()