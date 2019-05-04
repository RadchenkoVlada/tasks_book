"""
Exercise 4:
Download a copy of the file from www.py4e.com/code3/romeo.txt
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is not in
the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

"""


def opening_file(name_file):
    try:
        with open(name_file, "r+") as file:
            count = 0
            new_list = []
            for line in file:
                count += 1
                words = line.split()
                for word in words:
                    if word in new_list:
                        continue
                    else:
                        new_list.append(word)
            sorted_list = sorted(new_list)
            print("Sorted list:", sorted_list)
    except IOError:
        print('File {0}'.format(name_file), "cannot be opened:")


if __name__ == '__main__':
    name_file = input("Enter file: ")
    opening_file(name_file)
