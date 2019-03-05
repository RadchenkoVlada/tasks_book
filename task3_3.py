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
