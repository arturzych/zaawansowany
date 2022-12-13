# print('=======tyhtrrt=====')
# raise AssertionError("Incomparable")
# raise NameError("Improper name ")

# class KastomowyWyjatek(Exception):
#     pass
#
#
# print('=======tyhtrrt=====')
# try:
#     raise KastomowyWyjatek("made on my own")
# except KastomowyWyjatek:
#     print('elo kustom polecial')


class SchoolError(Exception):
    pass


a = input("Twoja ocena to: ")
print('Wystawiles ocene: ',a)


if not a.isdigit():
    raise SchoolError("ocena musi byc cyfra")

if int(a) > 6:
    raise SchoolError("ocena spoza skali")

