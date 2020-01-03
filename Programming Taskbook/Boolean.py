import math


def boolean10(a, b):
    """Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»."""
    if ((a+b) % 2) != 0:
        return True
    else:
        return False


def boolean11(a, b):
    """Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B имеют одинаковую четность»"""
    if (a % 2) == 0 and (b % 2) == 0:
        return True
    if (a % 2) != 0 and (b % 2) != 0:
        return True
    else:
        return False


def boolean14(a, b, c):
    """Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».»
    """
    if (a > 0) and (b <= 0) and (c <= 0):
        return True
    if (b > 0) and (a <= 0) and (c <= 0):
        return True
    if (c > 0) and (b <= 0) and (a <= 0):
        return True
    else:
        return False


def boolean17(a):
    """Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным»»
    """
    if (a > 0) and (a % 2 != 0) and (100 <= a < 1000):
        return True
    else:
        return False


def boolean21(a):
    """Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую
    последовательность»
    """
    if 100 <= a < 1000:
        hundreds = a // 100
        dozens = (a // 10) % 10
        units = a % 10
        if hundreds < dozens < units:
            return True
        return False
    else:
        return False


def boolean31(a, b, c):
    """Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника. Проверить истинность высказывания:
     «Треугольник со сторонами a, b, c является равнобедренным»
    """
    # try:
    if a > 0 and b > 0 and c > 0:
        first_way = (a + b) > c and a == b
        second_way = (b + c) > a and b == c
        third_way = (c + a) > b and c == a
        if first_way is not None:
            return True
        elif second_way is not None:
            return True
        elif third_way is not None:
            return True
    else:
        return False
    # except ValueError:
    #     print("It is impossible to create a triangle with these three numbers.")


def boolean39(x1, y1, x2, y2):
    """Даны координаты двух различных полей шахматной доски x1,y1, x2, y2 (целые числа, лежащие в диапазоне 1–8).
    Проверить истинность высказывания: «Ферзь за один ход может перейти с одного поля на другое».
    """
    x = x1 - x2
    y = y1 - y2
    if math.fabs(x) == math.fabs(y) or (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
        return True
    else:
        return False


if __name__ == '__main__':
    # print(boolean10(2, 3))
    # print(boolean11(1, 8))
    # print(boolean14(0, 0, -2))
    # print(boolean17(904))
    # print(boolean21(121))
    # print(boolean31(0, 2, 4))
    # print(boolean34(2, 8))
    print(boolean39(2, 2, 3, 2))


#
