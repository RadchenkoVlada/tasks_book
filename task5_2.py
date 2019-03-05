"""
Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers
instead of the average.

"""
if __name__ == '__main__':
    total_sum = 0
    count = 0
    numbers = []
    while True:
        try:
            elem = input("Enter a elem:")
            if elem == "done":
                break
            number = float(elem)
            total_sum += number
            count += 1
            numbers.append(number)
        except:
            print("Invalid input")
    print("Total = ", total_sum, "Count = ", count, "Min = ", min(numbers), "Max = ", max(numbers))
