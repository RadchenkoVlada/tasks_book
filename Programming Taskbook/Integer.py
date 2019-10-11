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


def integer21(seconds):
    """С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последней минуты.
    :return: int
    """
    return seconds % 60


def integer24(k):
    """Дни недели пронумерованы следующим образом: 0 — воскресенье, 1 — понедельник, 2 — вторник, ..., 6 — суббота.
    Дано целое число K, лежащее в диапазоне 1–365. Определить номер дня недели для K-го дня года, если известно, что в
    этом году 1 января было понедельником.
    :
    :return: str - day of the week depending on the number k
    :except: ValueError if number k not in range of 1 to 365

    You can find a calendar in folder - "data" to check the given number "k"
    """
    days_of_the_week = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}
    if 1 <= k <= 365:
        answer = k % 7
        return type(days_of_the_week[answer])
    else:
        raise ValueError("Number k should be in range of 1 to 365")


if __name__ == '__main__':
    print(integer7(12))

    print(integer8(95))

    print(integer17(1200))

    print(integer21(121))

    print(integer24(23))

#