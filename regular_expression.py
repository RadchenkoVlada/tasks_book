"""
Exercise 2: Write a program to look for lines of the form
`New Revision: 39772`
and extract the number from each of the lines using a regular expression and the findall() method. Compute the average
of the numbers and print out the average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
"""
import re


def average_of_numbers(filename):
    count = 0
    sum_all = 0
    # new_list = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            one_elem = re.findall('^New.*: ([0-9.]+)', line)
            if len(one_elem) > 0:
                number = int(one_elem[0])
                sum_all += number
                count += 1
        average = sum_all / count
        average = int(average * 10000000) / 10000000
    return average


if __name__ == '__main__':
    file_name = input("Enter file: ")
    print(average_of_numbers(file_name))
