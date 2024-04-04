import math


def getDiscriminant(a, b, c):
    return (b ** 2) - 4 * a * c


a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

discriminant = getDiscriminant(a, b, c)

match discriminant:
    case d if (d > 0):
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f'Result: x1 = {x1}, x2 = {x2}')
    case d if (d < 0):
        x = -b / (2 * a)
        print(f'Result: x = {x}')
    case _:
        print('No solutions')
