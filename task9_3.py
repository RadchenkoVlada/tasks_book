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
# PyCharm | Preferences | Editor | General | Code Completion  хз не нашла я, капецушки

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
        # this line is created to check the answer

        for key in dictionary:
            print(key, dictionary[key])
        # maximum = max(dictionary, key=dictionary.get)
        """
        Ключ должен работать с элементами dict (т.е. Парами ключ-значение). Затем, используя второй элемент элемента
        в качестве ключа max (в отличие от ключа dict), вы можете легко извлечь самое высокое значение и связанный
        с ним ключ.
        """
        maximum = max(dictionary.items(), key=lambda k: k[1])
        # maximum = max(dictionary.values())

        # def keywithmaxval(d):
        #     """ a) create a list of the dict keys and values;
        #         b) return the key with the max value
        #     """
        #     # The method index() returns the lowest index in list that obj appears.
        #     # че то через жопу как-то
        #     v = list(d.values())
        #     k = list(d.keys())
        #     return k[v.index(max(v))]
        # print("Who has the most messages: ", keywithmaxval(dictionary))

        print("Who has the most messages: ", maximum)
        return dictionary

# http://qaru.site/questions/388565/parsing-from-addresses-from-email-text
if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    # in my opinion it's hardcode, but it works
    print(find_an_email("mbox-short.txt"))
