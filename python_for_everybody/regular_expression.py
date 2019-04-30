"""
Exercise 2: Write a program to look for lines of the form
`New Revision: 39772`
and extract the number from each of the lines using a regular expression and the findall() method. Compute the average
of the numbers and print out the average.

Enter file:mbox_long.txt
38549.7949721

Enter file:mbox.txt
39756.9259259
"""
import re


def average_of_numbers(filename):
    sum_all = 0
    try:
        with open(filename, "r") as file:
            temp_var = re.findall('^New.*: ([0-9]+)', file.read(), re.MULTILINE)
            for elem in temp_var:
                number = float(elem)
                sum_all += number
            count = len(temp_var)
            if count == 0:
                return 0
            average = sum_all / count
            round_average = round(average, 7)
            return round_average
    except IOError:
        print('File {0}'.format(filename), "cannot be opened:")


if __name__ == '__main__':
    file_name = input("Enter file: ")
    print(average_of_numbers(file_name))
    #
