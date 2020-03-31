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


def task_2(input):
    """
    2. Reverse the words order in the text. Capital letters and dots should be correct.
    Example:
    Input: "My uncle. What a worthy man. Falling ill like that. And dying."
    Output: "Dying and. That like ill falling. Man worthy a what. Uncle my."

    Note:
    if the first word in the sentence is a name you can't know is it name or just word
    :type input: str
    """
    sentences = input.split(".")
    # last symbol is . so last el of split is empty string
    if not sentences[-1]:  # if not False -> then True
        del sentences[-1]
    # print(list_of_str)
    l = []
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        words = str(sentences[i]).split(" ")
        words[0] = words[0].lower() + "."
        words[-1] = (words[-1]).capitalize()
        processed_sentence = " ".join(words)
        l.append(processed_sentence)

    processed_input = " ".join(l)

    def reverse_words(string):
        input_words = string.split(" ")
        '''
        first is -1 that means start from last element
        second argument is empty that means move to end of list
        third arguments is difference of steps
        '''
        to_reverse_words = input_words[-1::-1]
        result = " ".join(to_reverse_words)
        return result

    return reverse_words(processed_input)


def task_3(input):
    """
    3. Find and print out all names in the text (the word starting with capital letter but not start of the sentence) and the numbers of these words.
    Example:
    Input: I am Vlada. Vlada loves programming. The Radchenko is the best family. The Radchenko lives in Kharkiv.
    Output: Vlada, Radchenko, Kharkiv
    :type input: str
    """
    answer = []
    sentenses = input.split(".")
    if not sentenses[-1]:
        sentenses.remove(sentenses[-1])

    for index in range(len(sentenses)):
        sentenses[index] = sentenses[index].strip()
        list_of_words = sentenses[index].split(" ")
        for index_ in range(1, len(list_of_words)):

            if list_of_words[index_].istitle():
                answer.append(list_of_words[index_])

    # Deleting duplicates in the list
    answer = list(set(answer))
    len_answer = len(answer)
    return f"There are {len_answer} proper name(s): {answer}"


def task_4(input):
    """4.
     Convert a text into "todo list" sentence by sentence. Use '-' symbol for start and ';' for end of all lines except
        the last one and use '.' for the last one.
        Input: I like to write code. I am the best programmer. Learning is light and ignorance is darkness.
        Output:
        - I like to write code;
        - I am the best programmer;
        - Learning is light and ignorance is darkness.
    """
    answer = []
    sentenses = input.split(".")
    if not sentenses[-1]:
        sentenses.pop()
    for index in range(len(sentenses)):
        if index == (len(sentenses) - 1):
            sentenses[-1] = "- " + sentenses[-1] + "."
            print(sentenses[index])
        else:
            sentenses[index] = "- " + sentenses[index].strip() + ";"
            print(sentenses[index])


def task_5(input):
    """
    5. Find the position of the given word in the text and in the sentence. Word to search is the second input.
    Input: You like to write code. I am the best programmer ana you too. You are perfect.
    you

    Output:
    3 entry of word 'you' has been found:
    - sentence 1 word 3. Position in the text: word 3 character 8.
    - sentence 2 word 1. Position in the text: word 4 character 12.
    - sentence 3 word 1. Position in the text: word 8 character 31.


    Notes:
    The first sentence is easy.
    'You' is not much input 'you' in the second and the third sentences but must be found by your program.
    In the fourth sentence word 'Your' contains a part of word 'You'. It shouldn't be detected.
    :return:
    """
    pass


if __name__ == '__main__':
    # print(task_0("I love you. You are the best. Our life is cool."))
    # print(task_1("I love you. You are the best. Ooour life is cool."))
    # print(task_2("My uncle. What a worthy man. Falling ill like that. And dying."))
    # print(task_3("I am Vlada. Vlada loves programming. The Radchenko is the best family. The Radchenko lives in Kharkiv."))
    task_4(" I like to write code. I am the best programmer. Learning is light and ignorance is darkness.")
    # task_1("I love you. You are the best. Our life is cool." * 10000000)
    # print(timeit.timeit("task_0(\"I love you. You are the best. Our life is cool.\")",globals=globals()))
    # print(timeit.timeit("task_1(\"I love you. You are the best. Our life is cool.\")", globals=globals()))
    # print(timeit.timeit("task_2(\"My uncle. What a worthy man. Falling ill like that. And dying.\")", globals=globals()))
