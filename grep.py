"""
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a
regular expression and count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$

"""
import re


def like_grep(file_name):
    expression = input("Enter a regular expression: ")
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            if re.search(expression, line):
                count += 1
    return count, expression


if __name__ == '__main__':
    count, expression = like_grep("mbox_long.txt")
    print("mbox.txt had", count, "lines that matched", expression)
