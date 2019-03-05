import string
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
    name = "Vlada-shokolada"
    backwards(name)
    comparison("Pineapple")
    print(dir(list_))
    # https: // stackoverflow.com / questions / 3031045 / how - come - string - maketrans - does - not -work - in -python - 3 - 1 / 3031061  # 3031061
    input = b"ps"
    output = b"vl"
    print(list_.translate(bytes.maketrans(input, output)))

    print("The sum of 1 + 2 is {0} and {1}".format(1 + 2, 10))

"""
Exercise 4: There is a string method called count that is similar to
the function in the previous exercise. Read the documentation of this method at
https://docs.python.org/3.5/library/stdtypes.html#string-methods and write an invocation
that counts the number of times the letter a occurs in “banana”.
"""


    camels = 'wolf'
    print('%s' % camels)
    print(type('%s' % camels))
    print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))




