"""
Functions which returns dict or false when wrong input
"""
def count_symbols(word):
    dictionary = {}
    if not isinstance(word, str):
        return False
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = dictionary.get(letter, 1)
        else:
            dictionary[letter] = dictionary.get(letter) + 1
    return dictionary



if __name__ == '__main__':
    word = input("Please enter a word: ")
    print(count_symbols(word))

# def count_symbols(data):
#     if not isinstance(data, str):
#         return False
#     d = {}
#     print(data)
#     for symbol in data:
#         if symbol in d:
#             d[symbol] += 1
#         else:
#             d[symbol] = 1
#     return d
#
# print(count_symbols(123445))
#
