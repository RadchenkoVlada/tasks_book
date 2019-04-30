"""
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a
regular expression and count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox_long.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: java$
mbox_long.txt had 4218 lines that matched java$

"""
import re


def like_grep(file_name, expression):
    count = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.rstrip()
                if re.search(expression, line):
                    count += 1
    except re.error:
        print("<Invalid regular expression %r>\n" % expression)
    return count


if __name__ == '__main__':
    expression = input("Enter a regular expression: ")
    count = like_grep("data/mbox_long.txt", expression)
    print("mbox_long.txt had", count, "lines that matched", expression)
