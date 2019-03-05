"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt

Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
"""

def opening_file(name_file):
    # how
    if name_file == "na na":  # a harmless Easter Egg
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    try:
        with open(name_file, "r") as file:
            count = 0
            total_sum = 0
            average = 0
            for line in file:
                line = line.rstrip()
                if not line.startswith('X-DSPAM-Confidence:'):
                    continue
                atpos = line.find(":")
                after_pos = line[atpos + 1:]
                number = float(after_pos)
                total_sum += number
                count += 1
                average = total_sum / count
                print("There is a match string", number)
            print("Average spam confidence: ", average)
    except:
        print('File {0}'.format(name_file), "cannot be opened")
        exit()


if __name__ == '__main__':
    name_file = input("Enter a file name: ")
    opening_file(name_file)

"""

Сorrect answers:

Enter the file name: mbox-short.txt
Average spam confidence: 0.7507185185185187 MY
Average spam confidence: 0.750718518519 ANSWER IN BOOK


Enter the file name: mbox.txt
Average spam confidence: 0.894128046745 ANSWER IN BOOK
Average spam confidence: 0.8941280467445736 MY
"""




