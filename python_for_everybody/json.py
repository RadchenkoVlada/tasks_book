# http://py4e-data.dr-chuck.net/comments_42.json - this json file
"""
Sample Execution

$ python3 json.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...

"""
import urllib.request, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    total = 0
    count = 0
    """
    There are 2 ways to count the sum and count
    """
    # for comment in js['comments']:
    #     number = comment['count']
    #     count += 1
    #     total += int(number)

    for i in range(len(js["comments"])):
        number = js["comments"][i]["count"]
        count += 1
        total += int(number)

    print("Count: ", count)
    print("Sum:", total)
#
