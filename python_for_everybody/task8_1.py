"""
Exercise 1:
Write a function called chop that takes a list and modifies it, removing the first
and last elements, and returns None.

Then write a function called middle that takes a list and
returns a new list that contains all but the first and last elements.
"""


def chop(list_):
    del list_[0]
    del list_[-1]
    return None


def middle(list_):
    new_list = list_.copy()
    print(new_list is list_)
    new_list.pop(0)
    new_list.pop(-1)
    return new_list


if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    numbers = ['1', '2', '3', '4', '5']
    chop(letters)
    print(letters)

    middle_numbers = middle(numbers)
    print(middle_numbers)
    print(numbers)



