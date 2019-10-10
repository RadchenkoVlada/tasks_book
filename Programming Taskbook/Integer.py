def integer7(number):
    """Дано двузначное число. Найти сумму и произведение его цифр."""
    if 10 <= number <= 99:
        digit = str(number)
        for num in range(len(digit) - 1):
            amount = int(digit[num]) + int(digit[num + 1])
            product = int(digit[num]) * int(digit[num + 1])
        return 'Sum: {0}, Product: {1}'.format(amount, product)


def integer8(number):
    """Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
        :raises: ValueError in case number isn't a two-digits

    """
    if 10 <= number <= 99:
        digit = str(number)
        str_list = []
        for el in range(len(digit)):
            str_list.append(digit[el])
        str_list[0], str_list[1] = str_list[1], str_list[0]
        answer = int(''.join(str_list))
        return answer
    else:
        raise ValueError("number isn't a two-digits")


def integer17(number):
    """ Дано целое число, большее 999.
        Используя одну операцию деления нацело и одну операцию взятия остатка от деления,
        найти цифру, соответствующую разряду сотен в записи этого числа.

        :return: int number
        :raises: ValueError in case number <= 999
        """
    if int(number) > 999:
        answer = number // 100 % 10
        return answer
    else:
        raise ValueError("number should be > 999")





if __name__ == '__main__':
    print(integer7(12))

    print(integer8(95))

    print(integer17(1200))
