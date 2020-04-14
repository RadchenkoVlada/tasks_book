"""
Exercise 2:
Change your socket program so that it counts the number of characters it has received and stops
displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the
total number of characters and display the count of the number of characters at the end of the document.
"""

import socket

from urllib.error import HTTPError

try:
    user_url = input("Enter url: ").strip()
    host = user_url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + user_url + ' HTTP/1.0\n\n').encode()
    mysock.send(cmd)
except ConnectionError:
    print("Please enter a valid URL")
except HTTPError:
    print("Invalid HTTP query")

count = 0

while True:
    data = mysock.recv(512)
    if (len(data) < 1) or count >= 3000:
        break
    count = count + len(data)
    print(data.decode("utf-8"))

mysock.close()
print("The number of characters is ", count)

#