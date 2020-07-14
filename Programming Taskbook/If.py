import math
import numpy as np

def if5(x, y, z):
    """Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.
    """
    numbers = [x, y, z]
    positive = 0
    negative = 0
    for el in numbers:
        if el > 0:
            positive += 1
        elif el == 0:
            pass
        else:
            negative += 1
    return positive, negative


def if13(x, y, z):
    """Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим)
    """
    average = 0
    if x < y and x < z:
        # minimum = x
        if y < z:
            average = y
        else:
            average = z

    elif y < x and y < z:
        # minimum = y
        if x < z:
            average = x
        else:
            average = z

    else:
        # minimum = z
        if x < y:
            average = x
        else:
            average = y

    return average


def if16(a: float, b: float, c: float):
    """
    Даны три переменные вещественного типа: A, B, C. Если их значенияупорядочены по возрастанию, то удвоить их;
    в противном случае заменить значение каждой переменной на противоположное. Вывести новые значения
    переменных A, B, C.
    """
    if a < b < c:
        a *= 2
        b *= 2
        c *= 2
    else:
        a = -a
        b = -b
        c = -c

    return a, b, c


def if20(a, b, c):
    """
    На числовой оси расположены три точки: A, B, C. Определить, какая из двух последних точек (B или C) расположена
    ближе к A, и вывести эту точку и ее расстояние от точки A.
    """
    distance_ac = math.fabs(a-c)
    distance_ab = math.fabs(a-b)
    if distance_ac > distance_ab:
        return b, distance_ab
    elif distance_ab > distance_ac:
        return c, distance_ac
    else:
        return 0, 0


def if21(x, y):
    """
    Даны целочисленные координаты точки на плоскости. Если точка совпадает с началом координат, то вывести 0.
    Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1 или 2.
    Если точка не лежит на координатных осях, то вывести 3.
    """
    if x == y == 0:
        return 0
    elif y == 0 and x != 0:
        return 1
    elif x == 0 and y != 0:
        return 2
    else:
        return 3


def if24(x):
    """
    Для данного вещественного x найти значение следующей функции f,
    принимающей вещественные значения:
    f (x) = {2·sin(x), если x > 0,
            {6-x, если x <= 0.
    """
    if x > 0:
        return 2*(math.sin(x))
    if x <= 0:
        return 6-x


def if24(x):
    """
        Для данного вещественного x найти значение следующей функции f,
        принимающей значения целого типа:
                 0, если x < 0,
        f(x) =   1, если x принадлежит [0,1), [2,3), ... ,
                -1, если x принадлежит [1, 2), [3, 4), . . . .
    """
    # we want to take the integer part of the number
    # integer is the second el in tuple and fractional is the first el
    integer_num = int(math.modf(x)[1])
    if integer_num < 0:
        return 0
    elif integer_num % 2 == 0:
        return 1
    elif integer_num % 2 != 0:
        return -1


if __name__ == '__main__':
    # positive, negative = if5(0, 1, -1)
    # print(f"positive:{positive},", f"negative:{negative}")

    # print(if13(0, 0, 1))

    # a, b, c = if16(1.4, 10, 23.5)
    # print(f"a = {a}, b = {b}, c = {c}")

    # point, distance = if20(1.4, 29, 23.5)
    # print(f"Point = {point}, distance = {distance}")

    # print(if21(2, 0))

    # print(if24(4))

    print(if24(2))




