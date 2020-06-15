"""
    Создайте список товаров для интернет магазина. Разрешается использовать что угодно для реализцаии самих товаров,
    главное что бы работала сортировка.

    Объекты должны содержать название, цену, рейтинг (от 1 до 5 звезд)
    и тип (один из Електроника, Мебель, Комп.Техника, Аксесуары)
    Отсортировать эти объекты используя оба варианта(только для 1) по след критериям:
    (сортировка всех строк подразумевает лексикографический порядок)

    1. По цене
    2. По названию в убывающем порядке (Z-A)
    3. По типу (название типа A-Z), вниутри каждого типа по рейтенг
"""
import random
from typing import Any, Union


class Items:
    def __init__ (self, name: str, price: float, rating: float, type_item: str):
        self.name = name
        self.price = price
        self.rating = rating
        if rating > 5 or rating < 1:
            raise ValueError
        dict_of_types = {1: "Electronics", 2: "Furniture", 3: "Comp. Equipment", 4: "Accessories"}
        self.type_item = type_item
        if type_item not in dict_of_types.values():
            raise ValueError

    def __str__(self):
        return f"Name: {self.name}, price:{self.price}, rating: {self.rating}, type of item: {self.type_item}\n"

    def __repr__(self):
        return self.__str__()


def recursion_length(l: list):
    """Напишите пример кода, который вычисляет длину списка при помощи рекурсии"""
    if l:
        return recursion_length(l[1:]) + 1
    else:
        return 0

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


def f(x):
    return 5 * x * x - 3 * x - 14


def dihotomia(f, a: float, b: float) -> float:
    """
    Написать рекурсивную функцию вычисления корня уравнения  f(x)=0. на заданном отрезке (a,b). Функция монотонная и
    решение существует.
    точное решение не получится искать с точнгостью до eps=0.0001

    Ex: 5*x*x - 3*x - 14,
    корни уравнения: x1 = -(7/5), x2 = 2
    a = 0, b =10, eps = 0.001

    base condition that stops the recursion:
    (Теорема о нуле непрерывной функции.) Если функция непрерывна на некотором отрезке и на концах этого отрезка
    принимает значения противоположных знаков, то существует точка, в которой она равна нулю.
    В частности любой многочлен нечётной степени имеет по меньшей мере один нуль
    :type a: float
    :type b: float
    """
    eps = 0.001
    c = (a + b) / 2.0
    if abs(b - a) > eps:
        fc = f(c)
        fa = f(a)
        if (fc < 0 and fa < 0) or (fc > 0 and fa > 0):
            return dihotomia(f, c, b)
        else:
            return dihotomia(f, a, c)
    return c



if __name__ == '__main__':
    # item1 = Items("hoover", 200, 2, "Electronics")
    # item2 = Items("PC", 2000, 5, "Comp. Equipment")
    # item3 = Items("Telephone", 100, 1, "Electronics")
    # items_objects = [ item1, item2, item3 ]
    # # print(list_objects)
    # # for obj in list_objects:
    # #     print(obj)
    # """ По цене"""
    # print(sorted(items_objects, key=lambda item: item.price))
    # """По названию в убывающем порядке (Z-A)"""
    # print(sorted(items_objects, key=lambda item: item.name, reverse=True))
    # """По типу (название типа A-Z), вниутри каждого типа по рейтенг"""
    # print(sorted(items_objects, key=lambda item: item.type_item))

    # print(recursion_length([1,2,3,4]))
    print(dihotomia(f, a=0.0, b=3.0))
    print(f(1.9998))
