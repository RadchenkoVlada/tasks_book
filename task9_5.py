"""
Exercise 5:
This program records the domain name (instead of the address) where the message was sent from instead of who
the mail came from (i.e.,the whole email address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py

Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


"""


def record_the_domain_name(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            if line[:5] == "From ":
                word_list = line.split()
                email = word_list[1]
                # s.find(), s.rfind(). They return the indices of the first and last occurrence of the required
                # substring.
                # If the substring is not found, the method returns the value -1.
                domain = email[email.find("@")+1:]
                if domain in dictionary:
                    dictionary[domain] += 1
                else:
                    dictionary[domain] = 1

        return dictionary


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print(record_the_domain_name("mbox-short.txt"))