def opening_file(name_file):
    try:
        with open(name_file, "r") as file:
            count = 0
            for line in file:
                count += 1
                line = line.rstrip()
                if not line.startswith('From:'):
                    continue
                print("There is line", line)
            print("Lines count: ", count)
    except:
        print('File {0}'.format(name_file), "cannot be opened:")
        exit()


def writing_in_file(name_file):
    with open(name_file, "w") as file:
        print(file)
        line1 = "This here's the wattle,\n"
        print(file.write(line1))


if __name__ == '__main__':
    name_file = input("Enter a file name: ")
    opening_file(name_file)
    s = '1 2\t 3\n 4'
    print(repr(s))


