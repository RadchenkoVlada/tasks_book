from collections import Counter

def if5(x, y, z):
    """Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.
    """
    numbers = [x, y, z]
    positive = 0
    negative = 0
    for el in numbers:
        if el > 0:
            positive += 1
            continue
        elif el == 0:
            pass
        else:
            negative += 1
            continue
        return positive, negative


def if13(x, y, z):
    """Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим)
    """
    numbers = [x, y, z]
    counter = Counter(numbers)
    result = [i for i, j in counter.items() if j > 1]
    average = 0
    if result:
        value, count = counter.most_common(1)[0]
        return f"You have number repetition: there are  number - {value}, have repeated {count} times"
    if x < y and x < z:
        # minimum = x
        if y < z:
            average = y
        elif z < y:
            average = z

    elif y < x and y < z:
        # minimum = y
        if x < z:
            average = x
        elif z < x:
            average = z

    elif z < x and z < y:
        # minimum = z
        if x < y:
            average = x
        elif y < x:
            average = y

    elif y == z or x == z or y == x:
        return f"You entered two identical numbers"

    return average


if __name__ == '__main__':
    # positive, negative = if5(0, 0, 0)
    # print(f"positive: {positive}, negative: {negative}")
    print(if13(1, 5, 123))
