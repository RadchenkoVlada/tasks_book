def task_0(input: str):
    """Task:
    0. Replace letter 'o' to 'a'
    Input: I love you. You are the best. Our life is cool.
    Input: I lave yau. Yau are the best. Aur life is caal.
           I lave yau. Yau are the best. Our life is caal.

    """
    out = input.replace('o', 'a')
    output = out.replace("O", "A")
    return output


def task_1(input: str):
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
            if 'O' in output[ i ] or 'o' in output[ i ]:
                word = output[ i ].replace('O', 'A')
                output[ i ] = word
                if 'o' in output[ i ]:
                    word = output[ i ].replace('o', 'a')
                    output[ i ] = word
    return ' '.join(output)


def task_2 (input: str):
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

    def reverse_words(string: str):
        input_words = string.split(" ")
        '''
        first is -1 that means start from last element
        second argument is empty that means move to end of list
        third arguments is difference of steps
        '''
        to_reverse_words = input_words[ -1::-1 ]
        result = " ".join(to_reverse_words)
        return result

    return reverse_words(processed_input)


def task_3 (input: str):
    """
    3. Find and print out all names in the text (the word starting with capital letter but not start of the sentence) and the numbers of these words.
    Example:
    Input: I am Vlada. Vlada loves programming. The Radchenko is the best family. The Radchenko lives in Kharkiv.
    Output: Vlada, Radchenko, Kharkiv
    :type input: str
    """
    answer = [ ]
    sentences = input.split(".")
    if not sentences[ -1 ]:
        sentences.remove(sentences[ -1 ])

    for index in range(len(sentences)):
        sentences[ index ] = sentences[ index ].strip()
        list_of_words = sentences[ index ].split(" ")
        for index_ in range(1, len(list_of_words)):

            if list_of_words[index_].istitle():
                answer.append(list_of_words[index_])

    # Deleting duplicates in the list
    answer = list(set(answer))
    len_answer = len(answer)
    return f"There are {len_answer} proper name(s): {answer}"


def task_4(input: str):
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
    sentences = input.split(".")
    if not sentences[-1]:
        sentences.pop()
    for index in range(len(sentences)):
        if index == (len(sentences) - 1):
            sentences[-1] = "- " + sentences[-1] + "."
        else:
            sentences[index] = "- " + sentences[index].strip() + ";"
        print(sentences[index])


def task_5(phrase: str):
    """
    5. Find the position of the given word in the text and in the sentence.
    Word to search is the second input. Position of word in the text countdown from the beginning of the text.
    Input: You like to write code. I am the best programmer and you too. You are perfect.
    you

    Output:
    3 entry of word 'you' has been found:
    - sentence 1 word 1. Position in the text: word 1 character 1.
    - sentence 2 word 7. Position in the text: word 12 character 51.
    - sentence 3 word 1. Position in the text: word 14 character 60.


    Notes:
    The first sentence is easy.
    'You' is not much input 'you' but must be found by your program.
    In the fourth sentence word 'Your' contains a part of word 'You'. It shouldn't be detected.
    """
    search_word = input("Please, enter the word you want to find\n")

    sentence_word = dict()

    lower_search_word = search_word.lower()
    capital_search_word = search_word.title()

    number_of_times_in_text = phrase.count(lower_search_word) + phrase.count(capital_search_word)

    print(f"{number_of_times_in_text} entry of word '{search_word}' has been found:\t")

    # Searching the position of word in the text countdown from the beginning of the text.
    def find_position_in_text():
        l_position_in_text = []
        for search_word in [lower_search_word, capital_search_word]:
            search_pos = 0
            found_letter = phrase.find(search_word, search_pos)
            while found_letter != -1:
                search_pos = found_letter + len(search_word)
                l_position_in_text.append(found_letter + 1)
                found_letter = phrase.find(search_word, search_pos)
        l_position_in_text.sort()
        return l_position_in_text

    print(f"Position in the text of character word '{search_word}' :{find_position_in_text()}")

    sentences = phrase.split(".")
    # removing the empty line at the end
    if not sentences[-1]:
        sentences.remove(sentences[-1])

    # Searching the position of word in the input
    without_dots = phrase.replace(".", "")

    word_position_in_text = []
    words_in_the_text = without_dots.split(' ')
    for count, word in enumerate(words_in_the_text, 1):
        if word == lower_search_word or word == capital_search_word:
            word_position_in_text.append(count)
    print(f"Position in the text of word '{search_word}' :{sorted(word_position_in_text)}")

    # Searching the position in the sentence
    for i in range(len(sentences)):
        l = []
        words = sentences[i].split()
        for count, word in enumerate(words, 1):
            if word == lower_search_word or word == capital_search_word:
                l.append(count)
        sentence_word[i + 1] = l

    word_num = 0
    l_position_in_text = find_position_in_text()
    for sentence, words_in_sentence in sentence_word.items():
        for word in words_in_sentence:
            print(f"-sentence {sentence} word {word} .Position in the text: word {word_position_in_text[word_num]} "
                  f"character {l_position_in_text[word_num]}.", end="\n")
            word_num += 1

def task_6(input: str):
    """Нам дана строка символов, из которой нужно удалить все дубликаты. При этом порядок символов имеет значение.
    Каким будет результат?
    Input : geeksforgeeks
    Output : efgkos
    """
    no_repeat = set(input)
    sorted_list = sorted(list(no_repeat))
    sorted_str = ''.join(sorted_list)
    return sorted_str





if __name__ == '__main__':
    # print(task_0("I love you. You are the best. Our life is cool."))
    # print(task_1("I love you. You are the best. Ooour life is cool."))
    # print(task_2("My uncle. What a worthy man. Falling ill like that. And dying."))
    # print(task_3("I am Vlada. Vlada loves programming. The Radchenko is the best family. The Radchenko lives in Kharkiv."))
    # task_4(" I like to write code. I am the best programmer. Learning is light and ignorance is darkness.")
    # task_5("You you you like to write You the Best code. I You am the best programmer and you too. You are perfect.")
    print(task_6("geeksforgeeks"))
