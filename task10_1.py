"""
Exercise 1:
 Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
def record_the_adresses(filename):
    with open(filename, "r") as file:
        dictionary = {}
        count = 0
        for line in file:
            if line[:5] == "From ":
                word_list = line.split()
                email = word_list[1]
                # s.find(), s.rfind(). Они возвращают индексы первого и последнего вхождения искомой подстроки.
                #  Если же подстрока не найдена, то метод возвращает значение -1.
                if email not in dictionary:
                    dictionary[email] = dictionary.get(email, 1)
                else:
                    dictionary[email] = dictionary.get(email) + 1
        t = list()
        for key, val in dictionary.items():
            # t.append((val, key))
            t.append((key, val))

        t.sort(reverse=True)
        # если я что-либо print после сортировки, то it become this way
        """
        zqian@umich.edu 195
        zach.thomas@txstate.edu 17
        wagnermr@iupui.edu 44
        tnguyen@iupui.edu 6
        thoppaymallika@fhda.edu 1
        stuart.freeman@et.gatech.edu 17
        stephen.marquard@uct.ac.za 29
        ssmail@indiana.edu 5
        sgithens@caret.cam.ac.uk 43
        rjlowe@iupui.edu 90
        
        """
        # print("The list of tuples sorted by value: ", t)
        for key, val in t[:10]:
            print("The list of tuples sorted by value: ", key, val)

        # for key, val in t:
        #     print(val, key)

        # странно попросили одно, хотят другое в output
        return t[0]



if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print("The person who has the most commits", record_the_adresses("mbox_long.txt"))
