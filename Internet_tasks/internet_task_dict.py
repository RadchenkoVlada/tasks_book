"""
This is the site from there i have taken information.
https://server.179.ru/tasks/python/2014b1/17-sets.html

K: Номер появления слова
Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

L: Словарь синонимов
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре
различны. Для одного данного слова определите его синоним.

Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая строка содержит ровно два
слова-синонима. После этого следует одно слово.

Программа должна вывести синоним к данному слову.

M: Выборы в США
Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала проводятся
выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы:
на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата. На практике, все
выборщики от штата голосуют в соответствии с результами голосования внутри штата, то есть на заключительной стадии
выборов в голосовании участвуют штаты, имеющие различное число голосов.

Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом. Подведите итоги выборов: для
каждого из участника голосования определите число отданных за него голосов.

Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата, затем через
пробел идет количество выборщиков, отдавших голоса за этого кандидата.

Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них голосов.

N: Самое частое слово
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.


TEST from softserve
name: parse_number()
Please provide full program code of function which returns the dict with following structure: {odd: number of odd digits
in input value, even: number of even digits of input value} or false when wrong input value.
num-input number
NOTE: Assume that the "zero" digit also belongs to even numbers.
"""
import random

def number_of_the_word(filename):
    with open(filename, "r") as file:
        dictionary = {}
        # firstNlines = file.readlines()[0:100]
        for line in file:
            word_list = line.split()
            for word in word_list:
                if word not in dictionary:
                    dictionary[word] = 0
                else:
                    dictionary[word] = dictionary.get(word) + 1
                print(dictionary[word], end=' ')
            # return dictionary


def synonyms():
    synonyms = dict(oat="porridge", hello='hi', bye='goodbye', list='array', popcorn='corn', lady='girl', dame='queen',
                    mum='mother', sis='sister', dad='father')

    count_syn = random.randint(1, 6)
    print("Count of synonyms", count_syn)
    for i in range(count_syn):
        print(random.choice(list(synonyms.items())))
    syn = "lady"  # input("Please, enter the word for which you want to find a synonym:")
    for syn1, syn2 in synonyms.items():
        if syn1 == syn:
            print(syn2)
            print("if")
            break
        elif syn2 == syn:
            print(syn1)
            print("elif")
            break
        print(f"{syn1} {syn2} after if \n")

    print("End of the program")
    return 0  # how many returns do i need in the program or at all


def voting():
    candidates = dict(McCain=0, Obama=0, Trump=0, Weld=0)
    for i in range(7):
        candidate = random.choice(list(candidates.keys()))
        vote = random.randint(1, 11)
        candidates[candidate] += vote
        print(candidate, vote)
    print("Presidential Election Results:")
    list_keys = list(candidates.keys())  # i still haven't realized how the correct lexicographical order looks like
    list_keys.sort()
    for i in list_keys:
        print(i, candidates[i])


def most_frequent_word(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            word_list = line.split()
            for word in word_list:
                if word not in dictionary:
                    dictionary[word] = dictionary.get(word, 1)
                else:
                    dictionary[word] = dictionary.get(word) + 1
        # print(sorted(dictionary.items()))
        # list_values = list(dictionary.values())
        max_elem = max(dictionary.values())
        print(max_elem)
        answer = [key for key, value in sorted(dictionary.items()) if value == max_elem]
        return answer


def parse_number():
    dictionary = {"odd": 0, "even": 0}
    try:
        num = input("Please enter a number: ")
        numbers = int(num)  # check if input is correct
        list_ = list(str(numbers))
        list_numbers = []
        for el in list_:  # i have a problem with "0000" int() breaks everything
             list_numbers.append(int(el))
        for number in list_numbers:
            if number % 2 == 0:
                dictionary["even"] += 1
            # elif number == 0:
            #     dictionary["even"] += 1
            else:
                dictionary["odd"] += 1
    except ValueError:
            print("False input")
            exit()
    return dictionary


if __name__ == '__main__':
    # print(number_of_the_word("romeo.txt"))  # task number K
    # print(synonyms())
    # print(voting())
    print(parse_number())