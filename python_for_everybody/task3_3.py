"""
Exercise 3.
Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:

Score	Grade
>= 0.9	  A
>= 0.8	  B
>= 0.7	  C
>= 0.6	  D
< 0.6	  F


Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F

Run the program repeatedly as shown above to test the various, different
values for input.
"""


def score(number):
    result = ""
    if number >= 0.9:
        result = "A"
    elif number >= 0.8:
        result = "B"
    elif number >= 0.7:
        result = "C"
    elif number >= 0.6:
        result = "D"
    elif number < 0.6:
        result = "F"

    return result


if __name__ == '__main__':
    try:
        number = float(input('Enter score between 0.0 and 1.0: '))
        if number > 1.0 or number <= 0.0:
            print("You didn't follow instructions")
            exit()
        print(score(number))

    except:
        print("Error, Bad score")
