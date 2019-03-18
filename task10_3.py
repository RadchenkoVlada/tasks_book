"""
Exercise 3:
 Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z. Your program should not count
spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different
languages and see how letter frequency varies between languages. Compare your results with the tables
at "wikipedia.org/wiki/Letter_frequencies".
"""
import collections

def letter_counter(filename):
    with open(filename, "r") as file:
        dictionary = {}
        c = collections.Counter()
        for line in file:
            line = line.lower()
            symbols = ''.join(c for c in line if c.isalpha())
            for letter in symbols:
                if letter not in dictionary:
                    dictionary[letter] = dictionary.get(letter, 1)
                else:
                    dictionary[letter] = dictionary.get(letter) + 1
        t = list()
        for key, val in dictionary.items():
            t.append((key, val))

        t.sort()

        for key, val in t[:]:
            print(key, val)


if __name__ == '__main__':
    # filename = input("Enter a file name: ")
    print(letter_counter("english.txt"))

"""
import string
fname = raw_input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
letters = dict()
for line in fhandle:
	line = line.translate(None, string.punctuation)
	line = line.translate(None, string.digits)
	line = line.lower()
	line = line.split()
	for t in line:
		word = list(t)
		for letter in word:
			letters[letter] = letters.get(letter,0) + 1
letterlist = []
for letter, count in letters.items():
	letterlist.append( (count, letter) )
letterlist.sort(reverse=True)
for count, letter in letterlist:
	print letter, count
"""