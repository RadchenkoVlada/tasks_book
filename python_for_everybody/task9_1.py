"""
Exercise 1: [wordlist2]

Write a program that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""
def reading_words(name):
    dictionary = dict()
    with open(name, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                dictionary[word] = 'value'
            # где-то здесь использовать is_string_in_dictionary(dict)
            # а потом ретёрнуть резалт
        return len(dictionary)


"""
я предлагаю переформулировать

давай ты посчитаешь сколько раз в этом тексте встречается каждое слово.
Т.е. входной файл это текст, а на выходе должна быть таблица - каждое словао сколько раз встречается.
Ее не нужно принтить в консоль - запили аутпут в файл - каждая строка это слово и через пробел число сколько раз
встречается это слово
"""

def counter_of_words(file_name):
    dictionary = dict()
    with open(file_name, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary


def writing_to_new_file(file_name, dictionary):
    with open(file_name, "w") as file:
        # for key in dictionary:
        #     file.write("{}:{}\n".format(key, dictionary[key]))
        for key, val in dictionary.items():
            file.write('{}:{}\n'.format(key, val))


if __name__ == '__main__':
    print(counter_of_words("words.txt"))
    writing_to_new_file("new_file", counter_of_words("words.txt"))



# this implementation was created by author of the book
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#
# bigcount = None
# bigword = None
#
# for word, count in list(counts.items()):
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)