def opening_file(name_file):
    try:
        with open(name_file, "r") as file:
            count = 0
            for line in file:
                count += 1
                line = line.rstrip()
                print(line.upper())
            # print("Lines count: ", count)
            print(file)
    except:
        print('File {0}'.format(name_file), "cannot be opened:")
        exit()


if __name__ == '__main__':
    # name_file = input("Enter a file name: ")
    opening_file("mbox.txt")