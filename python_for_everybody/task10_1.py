"""
Exercise 1:
 Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
def record_the_adresses(filename):
    with open(filename, "r") as file:
        dictionary = {}
        for line in file:
            if line[:5] == "From ":
                word_list = line.split()
                email = word_list[1]
                if email not in dictionary:
                    dictionary[email] = dictionary.get(email, 1)
                else:
                    dictionary[email] = dictionary.get(email) + 1
        t = list()
        for key, val in dictionary.items():
            t.append((key, val))

        t.sort(reverse=True)

        for key, val in t[:10]:
            print("The list of tuples sorted by value: ", key, val)

        return t[0]


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print("The person who has the most commits", record_the_adresses("mbox_long.txt"))
