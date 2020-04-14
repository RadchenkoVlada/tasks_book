"""
Exercise 5:
Write a program to read through the mail box data and when you find line that starts with “From”,
you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a count at the end.

This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
"""


def find_a_sender(filename):
    senders_set = set()
    with open(filename, "r") as file:
        count = 0
        for line in file:
            if line[:4] == "From":
                word_list = line.split()
                sender = word_list[1]
                if sender not in senders_set:
                    senders_set.add(sender)
                    print("Sender is a ", sender)
                    count += 1

    with open("clean.txt", "w") as cleandata:
        for el in senders_set:
            cleandata.write(el+'\n')

    print("There were", count, "lines in the file with From as the first word")


if __name__ == '__main__':
    filename = input("Enter a file name: ")
    # find_a_sender("mbox.txt")
