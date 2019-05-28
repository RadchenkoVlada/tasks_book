"""
Exercise 3:
 Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000
 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this
 exercise, simply show the first 3000 characters of the document contents.

"""
import urllib.request
import urllib.error


# user_url = input("Enter url: ")
# test address
user_url = "http://data.pr4e.org/romeo.txt"
fhand = urllib.request.urlopen(user_url)
count = 0
characters = 0
for line in fhand:
    words = line.decode()
    if characters < 3000:
        print(words.strip())

    characters += len(words)
print("\nThe number of characters is ", characters)

#






