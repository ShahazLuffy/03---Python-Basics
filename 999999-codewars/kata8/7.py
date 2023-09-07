"""
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
def abbrev_name(name):
    reza =  list(name)
    karim=[]
    karim.append((reza[0]).upper())
    for index, item in enumerate(reza):
        if item ==' ':
            karim.append(reza[index+1].upper())
    return ".".join(karim)
print(abbrev_name("patrick feenan"))


def abbrevName2(name):
    return '.'.join(w[0] for w in name.split()).upper()


def abbrevName3(name):
    return '.'.join(x[0].upper() for x in name.split())


def akbar(name):
    return name.split()

print(akbar("reza karim sari"))