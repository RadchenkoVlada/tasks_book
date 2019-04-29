"""
Exercise 1:
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""


def compute_pay(hours, rate):
    return 40 * rate + (hours - 40) * rate * 1.5 if hours > 40 else hours * rate


if __name__ == '__main__':
    try:
        hours = float(input('Enter Hours: '))
        rate = float(input('Enter Rate: '))
        print(compute_pay(hours, rate))
    except:
        print("Error, please enter numeric input")

