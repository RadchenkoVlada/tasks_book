"""
Exercise 2:
 This program counts the distribution of the hour of the day for each of the messages. You can pull the hour
from the “From” line by finding the time string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""


def time_of_day(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            if line[:5] == "From ":
                word_list = line.split()
                exact_time = word_list[5]
                # s.find(), s.rfind(). Они возвращают индексы первого и последнего вхождения искомой подстроки.
                #  Если же подстрока не найдена, то метод возвращает значение -1.
                hour = exact_time[:exact_time.find(":")]
                if hour not in dictionary:
                    dictionary[hour] = dictionary.get(hour, 1)
                else:
                    dictionary[hour] = dictionary.get(hour) + 1
        t = list()
        for key, val in dictionary.items():
            t.append((key, val))

        t.sort()

        for key, val in t[:]:
            print(key, val)
        #  как бы это красиво вывести?
        #  без принта и без None at the end of the programm


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print(time_of_day("mbox-short.txt"))