"""
Exercise 3:
Write a program to read through a mail log, build a histogram using a dictionary
to count how many messages have come from each email address, and print the dictionary.

Enter file name: mbox-short.txt

{'gopal.ramasammycook@gmail.com': 1,
'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5,
'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2,
'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4,
'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4,
'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

Exercise 4:
Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created,look through the dictionary
using a maximum loop (see Section [maximumloop]) to find who has the most messages and print
how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195


"""


def find_an_email(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            if line[:8] == "Author: ":
                word_list = line.split()
                email = word_list[1]
                if email not in dictionary:
                    dictionary[email] = dictionary.get(email, 1)
                else:
                    dictionary[email] = dictionary.get(email) + 1

        for key in dictionary:
            print(key, dictionary[key])
        # maximum = max(dictionary, key=dictionary.get)
        """
        The key should work with dict elements (i.e. Key-value pairs). Then, using the second element of the element
        as the max key (unlike the dict key), you can easily extract the highest value and the associated
        with him the key.
        """
        maximum = max(dictionary.items(), key=lambda k: k[1])
        # maximum = max(dictionary.values())

        print("Who has the most messages: ", maximum)
        return dictionary


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print(find_an_email("mbox-short.txt"))
