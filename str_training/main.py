import timeit

def task_0(input):
    """Task:
    0. Replace letter 'o' to 'a'
    Input: I love you. You are the best. Our life is cool.
    Input: I lave yau. Yau are the best. Aur life is caal.
           I lave yau. Yau are the best. Our life is caal.

    """
    # print(type(input))
    out = input.replace('o', 'a')
    output = out.replace("O", "A")
    return output


def task_1(input):
    """
    1. Replace letter 'o' to 'a' in each second word (words with even number)
    Input: I love you. You are the best. Our life is cool.
    Input: I lave you. Yau are the best. Aur life is cool.
    :param input: str
    :return: str
    """
    """First option"""
    output = input.split()
    for i in range(len(output)):
        if (i % 2) == 1:
            if 'O' in output[i] or 'o' in output[i]:
                word = output[i].replace('O', 'A')
                output[i] = word
                if 'o' in output[i]:
                    word = output[i].replace('o', 'a')
                    output[i] = word
    return ' '.join(output)


if __name__ == '__main__':
    print(task_0("I love you. You are the best. Our life is cool."))
    # print(task_1("I love you. You are the best. Ooour life is cool."))
    # task_1("I love you. You are the best. Our life is cool." * 10000000)
    # print(timeit.timeit("task_0(\"I love you. You are the best. Our life is cool.\")",globals=globals()))
    print(timeit.timeit("task_1(\"I love you. You are the best. Our life is cool.\")",globals=globals()))
