"""
Write a program which repeatedly reads numbers until the user enters “done”.
Once “done” is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a elem,
detect their mistake using try and except and print an error message and skip to the next elem.
"""

if __name__ == '__main__':
    total_sum = 0
    count = 0
    while True:
        try:
            elem = input("Enter a elem:")
            if elem == "done":
                break
            number = float(elem)
            total_sum += number
            count += 1
        except ValueError:
            print("Invalid input")

    print("Total = ", total_sum, "Count = ", count, "Average = ", total_sum / count if count != 0 else 0)

