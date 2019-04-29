"""
Exersise:
Enter 5 words and count the length of each word.
"""

def task4():
    words = []
    length_words = []
    for word in range(5):
        word = input('Please enter word word:\n')
        words.append(word)
        length_word = len(word)
        length_words.append(length_word)

    return words, length_words


if __name__ == '__main__':
    words, length_words = task4()

    print("Words list:", words)
    print("Lengths of words:", length_words)