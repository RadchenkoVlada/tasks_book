"""
Write the program to store the numbers the user enters in a list
and use the max() and min() functions
to compute the maximum and minimum numbers after the loop completes
"""

def find_min(numbers):
    min = numbers[0]
    for elem in numbers:
        if elem < min:
            min = elem
    return min

def find_max(numbers):
    for element in numbers:
        max = element
        for elem in numbers:
            if elem > max:
                max = elem
    return max


if __name__ == '__main__':

    numbers = []
    element = ""
    while element != "done":
        element = input("Enter a elem:\n")
        numbers.append(element)

    print("numbers", type(numbers))
    int_numbers = [int(x) for x in numbers[:-1]]
    print("int_numbers", type(int_numbers))
    print("Maximum is ", find_max(int_numbers))
    print("built-in function max = ", max(int_numbers))
    print("Minimum is ", find_min(int_numbers))
    print("built-in function min = ", min(int_numbers))

