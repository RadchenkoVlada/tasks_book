def compute_pay(hours, rate):
    return 40 * rate + (hours - 40) * rate * 1.5 if hours > 40 else hours * rate

if __name__ == '__main__':
    try:
        hours = float(input('Enter Hours: '))
        rate = float(input('Enter Rate: '))
        print(compute_pay(hours, rate))
    except:
        print("Error, please enter numeric input")

