"""
This is the site from there i have taken information.
https://server.179.ru/tasks/python/2014b1/17-sets.html

A: Количество различных чисел
Дан список чисел, который могут содержать до 100000 чисел каждый. Определите, сколько в нем встречается различных чисел.

B: Количество совпадающих
Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел содержится одновременно
как в первом списке, так и во втором.

С: Пересечение списков
Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа, которые входят как в первый,
так и во второй список в порядке возрастания.

D: Встречалось ли число раньше
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

E: Кубики
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны
по цвету. Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих
наборах. Для этого они занумеровали все цвета случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается
помочь им в оставшейся части.

Номер любого цвета — это целое число в пределах от 0 до 109. В первой строке входного файла записаны числа N и M —
количество кубиков у Ани и Бори соответственно. В следующих N строках заданы номера цветов кубиков Ани. В последних M 
строках номера цветов кубиков Бори.

Выведите сначала количество, а затем отсортированные по возрастанию номера цветов таких, что кубики каждого цвета есть в
обоих наборах, затем количество и отсортированные по возрастанию номера остальных цветов у Ани, потом количество и 
отсортированные по возрастанию номера остальных цветов у Бори.

F: Количество слов в тексте
Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.

G: Угадай число
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для
этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел
есть задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы
она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август. Далее идут строки,
содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами. После каждой строки с
вопросом идет ответ Августа: YES или NO.

Наконец, последняя строка входных данных содержит одно слово HELP. Вы должны вывести (через пробел, в порядке
возрастания) все числа, которые мог задумать Август.

I: Полиглоты
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые
знает хотя бы один из школьников.

Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет
Mi строк, содержищих названия языков, которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
количество различных языков не более 1000. 1≤N≤1000, 1≤Mi≤500.

"""
import random
from itertools import chain


def number_of_different_numbers():
    list_input = [random.randint(-5, 100) for _ in range(20)]
    print(list_input)
    unique_word_count = len(set(list_input))
    return unique_word_count


def number_of_matches():
    input1 = set([random.randint(-5, 100) for _ in range(10)])
    print(input1)
    input2 = set([random.randint(-5, 100) for _ in range(10)])
    print(input2)
    count = len(input1.intersection(input2))
    return count


def crossing_lists():
    input1 = set([random.randint(-5, 100) for _ in range(10)])
    print(input1)
    input2 = set([random.randint(-5, 100) for _ in range(10)])
    print(input2)
    crossing = list(input1.intersection(input2))
    crossing.sort()
    return crossing


def did_the_number_occur_before():
    input = [random.randint(-5, 100) for _ in range(10)]
    print(input)
    numbers_set = set()
    for elem in input:
        if elem in numbers_set:
            print('YES')
        else:
            print('NO')
            numbers_set.add(elem)


def blocks():
    A_input = set([random.randint(0, 11) for _ in range(10)])
    print(A_input)
    B_input = set([random.randint(0, 11) for _ in range(10)])
    raw_crossing = A_input.intersection(B_input)
    crossing = sorted(list(raw_crossing))
    count = len(crossing)
    print(B_input)
    print("Input")
    print("Anna", len(A_input), "Boris", len(B_input))
    print("The colors of Anna's blocks:")
    for elem in A_input:
        print(elem)
    print("The colors of Boris' blocks:")
    for elem in B_input:
        print(elem)
    print("Output:")
    print('intersections of blocks', count)
    print(crossing)
    print("count of only Anna's blocks:", len(A_input.difference(B_input)))
    print(sorted(list(A_input-B_input)))
    print("count of only Boris' blocks:", len(B_input.difference(A_input)))
    print(sorted(list(B_input-A_input)))


def different_words_text(name_file):
    try:
        with open(name_file, "r") as file:
            unique_words = set(chain(*(line.split() for line in file if line)))
    except IOError:
        print('File {0}'.format(name_file), "cannot be opened")
        return 0
    else:
        return len(unique_words)


def guess_the_number():
    input_number = random.randint(0, 10)
    print("It is a secret! Hush! A hidden number:", input_number)
    print("The max number in which the hidden number is:", 10)
    output_set = set()
    for i in range(10):
        input_set = set([random.randint(0, 10) for _ in range(10)])
        print(" ".join(map(str, input_set)))
        output_set.update(input_set)
        if input_number in input_set:
            print("Yes\n")
            output_set = input_set & output_set
            print("Output set", output_set)
        else:
            print("No\n")
            output_set -= input_set  # The result of the difference is a set containing elements that are in
            # the "decreasing", but they are not in the "deductible"
            print("Output set", output_set)
    print("Help!")
    truthful_output = list(output_set)
    sorted_truthful_output = sorted(truthful_output)
    return " ".join(map(str, sorted_truthful_output))


def polyglots():
    languages = {"Russian", "English", "Japanese", "German", "French", "Finnish"}
    count_schoolkid = random.randint(1, 10)
    print("Count of schoolkid", count_schoolkid)
    list_of_set = []
    for schoolkid in range(count_schoolkid):
        count_languages = random.randint(1, 6)
        schoolkid_lang = set(random.sample(languages, count_languages))
        print("Languages ​​that the child knows", count_languages, ":", " ".join(map(str, schoolkid_lang)))
        list_of_set.append(schoolkid_lang)
    lang_know_all = set.intersection(*list_of_set)
    print("Languages ​​spoken by all students:", lang_know_all)
    lang_know_one = set.union(*list_of_set)
    print("Languages ​​that at least one of the students knows:", lang_know_one)



if __name__ == '__main__':
    # print("A: Numbers of different values in the list",number_of_different_numbers())
    # print("B: There are count of numbers at the same time in the first list and in the second:", number_of_matches())
    # print("C: Displays all numbers included in both the first and second list in ascending order: ", crossing_lists())
    # print("D:", did_the_number_occur_before())
    # print("E:", blocks())
    # words = different_words_text("romeo.txt")
    # if words is not None:
    #     print("F: Different words in the text -", words)
    print("G: Output", guess_the_number())
    # print("I:", polyglots())