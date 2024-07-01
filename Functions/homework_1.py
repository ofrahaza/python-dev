from math import sqrt


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve(a, b, c):
    d = discriminant(a, b, c)

    match d:
        case dis if (dis > 0):
            x1 = (-b - sqrt(dis)) / (2 * a)
            x2 = (-b + sqrt(dis)) / (2 * a)
            print(f'Два корня, x1 = {x1}, x2 = {x2}')
        case dis if (dis < 0):
            x = -b / (2 * a)
            print(f'Один корень, x = {x}')
        case _:
            print('Корней нет')