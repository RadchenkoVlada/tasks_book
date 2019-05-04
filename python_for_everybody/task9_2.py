"""
Exercise 2:
Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of
the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""


def find_a_day(filename):
    with open(filename, "r") as file:
        dictionary = {}
        # firstNlines = file.readlines()[0:100]
        for line in file:
            if line[:5] == "From ":
                word_list = line.split()
                day = word_list[2]
                if day not in dictionary:
                    dictionary[day] = dictionary.get(day, 1)
                else:
                    dictionary[day] = dictionary.get(day) + 1
        return dictionary


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print(find_a_day("mbox.txt"))
