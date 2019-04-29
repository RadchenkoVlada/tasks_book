"""
Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
"""

def backwards(list_):
    index = len(list_) - 1
    while index >= 0:
        print(list_[index])
        index = index - 1

"""
Exercise 3: 
Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.
"""


def count(word, desired_letter):
    count = 0
    for letter in word:
        if letter == desired_letter:
            count = count + 1
    print("The number of times =", count, "when the letter appears in a word", word)


def comparison(word):
    if word < 'banana':
        print('Your word, ' + word + ', comes before banana.')
    elif word > 'banana':
        print('Your word, ' + word + ', comes after banana.')
    else:
        print('All right, bananas.')


if __name__ == '__main__':
    list_ = "persimmon"
    name = "apple"
    backwards(name)
    comparison("Pineapple")
    print(dir(list_))
    print("The sum of 1 + 2 is {0} and {1}".format(1 + 2, 10))
