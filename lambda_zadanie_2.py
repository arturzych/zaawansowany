dict = [{'name': 'Aragorn', 'kills': 17},
        {'name': 'Legolas', 'kills': 11},
        {'name': 'Gimli', 'kills': 5},
        {'name': 'Eowyn', 'kills': 9},
        {'name': 'Gandalf', 'kills': 11}]

a = sorted(dict, key=lambda kills: kills['kills'])
print(a)
