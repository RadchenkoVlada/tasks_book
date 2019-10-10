import math


def begin9(a, b):
    """
    Даны два неотрицательных числа a и b. Найти их среднее геометри-
    ческое, то есть квадратный корень из их произведения чисел a и b.
    :return: a float number

    :raises: ValueError when numbers a, b are negative

    """
    if a < 0 or b < 0:
        raise ValueError("Number should be non-negative")
    geometric_mean = math.sqrt(a * b)
    return type(geometric_mean)


def begin23(a: int, b: int, c: int):
    """
    Даны переменные A, B, C. Изменить их значения, переместив содер- жимое A в B, B — в C, C — в A, и вывести новые
    значения переменных A, B, C.
    """
    a, b, c = b, c, a
    return a, b, c



def begin29(angle_in_degrees):
    """Дано значение угла Æ в градусах (0 < Æ < 360). Определить значение этого же угла в радианах, учитывая, что
    180 градусов = pi радианов. В качестве значения o использовать 3.14."""
    angle_in_radian = (angle_in_degrees * math.pi) / 180
    # angle_in_radians = math.radians(angle_in_degrees)
    return angle_in_radian


def begin39(a, b, c):
    """
    Найти корни квадратного уравнения A·x^2 + B·x + C = 0, задан- ного своими коэффициентами A, B, C
(коэффициент A не равен0), если известно, что дискриминант уравнения положителен. Вывести вначале меньший, а затем
больший из найденных корней.

    :return: A sorted list of float
    """
    if a != 0:
        D = (b ** 2) - 4 * a * c
        if D >= 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            if x1 < x2:
                return [x1, x2]
            if x2 < x1:
                return [x2, x1]
            if x1 == x2:
                return [x1]
        else:
            return []
    else:
        if b != 0:
            x = -c / b
            return [x]






if __name__ == '__main__':
    print(begin9(2, 1))

    print(begin23(1, 2, 3))

    print(begin29(180))

    print(begin39(3, 0, -27))  # -3, 3
    print(begin39(1, 4, 9))  # no roots
    print(begin39(4, -20, 25))  # 2,5

    # Input
    roots = begin39(5, 0, 30)
    # Output
    if not roots:
        print("not roots")
    else:
        print("root(s) is ", roots)



#