"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox-short.txt

Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox-short.txt and mbox-short.txt files.


Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their
program Modify the program that prompts the user for the file name so that it prints a funny message when the user
types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and
don’t exist. Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt


File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
"""

def opening_file(name_file):
    # how
    if name_file == "na na boo boo":  # a harmless Easter Egg
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
                number = float(after_pos)  # can be this situation X-DSPAM-Confidence: 0.8475jj
                total_sum += number
                count += 1
                average = total_sum / count
                print("There is a match string", number)
            print("Average spam confidence: ", average)

    except FileNotFoundError:
        print('File {0}'.format(name_file), "cannot be opened")

    except ValueError:
        print("Incorrect float value.")

    except Exception as exception:
        print('File {0}'.format(name_file))
        print(exception)


if __name__ == '__main__':
    name_file = input("Enter a file name: ")
    opening_file(name_file)

"""
Correct answer:

Enter the file name: mbox-short.txt
Average spam confidence: 0.7507185185185187    ANSWER IN MY PROGRAM
Average spam confidence: 0.750718518519    ANSWER IN BOOK


Enter the file name: mbox_long.txt
Average spam confidence: 0.894128046745    ANSWER IN BOOK
Average spam confidence: 0.8941280467445736    ANSWER IN MY PROGRAM
"""




