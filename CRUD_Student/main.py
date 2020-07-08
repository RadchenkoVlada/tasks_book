from Student import Student
from Storage_pickle import StoragePickle
from Storage_json import StorageJSON


def create_new_student():
    name = input("Enter name - ")
    last_name = input("Enter last name - ")
    passport = input("Enter student passport - ")
    stud = Student(name=name, last_name=last_name, passport=passport)
    print('A new student', stud.__str__())
    return stud


def choose_student(students):
    print("The list of students looks like this:", students)
    number = int(input("Enter please student in list starting from first"))
    if 1 <= number <= len(students):
        index = number - 1
        print("You chose this student-> ", students[index])
        return index


# how to write this function if information about all students are in main?
# def remove_student():
#     pass


def main():
    students = []
    do = ""
    s = StorageJSON()  # initializing
    while do != 10:
        try:
            do = int(input("Please choose what to do:\n"
                           "1 - create a new student,\n"
                           "2 - remove the student\n"
                           "3 - show all students\n"
                           "4 - update student attribute\n"
                           "5 - add/delete student's marks\n"
                           "6 - calculate the average student's score\n"
                           "7 - choose type of storage\n"
                           "8 - save information to the file\n"
                           "9 - load information from the file\n"
                           "10 - exit \n"))

            if do == 1:
                students.append(create_new_student())
                # save object to file
                print("Now the list of students looks like this", students, '\n')

            elif do == 2:
                index = choose_student(students)
                students.pop(index)
                # save object to file
                print("student was deleted")

            elif do == 3:
                print(*students, sep="\n")

            elif do == 4:
                index = choose_student(students)
                selected_student = students[index]
                do = 0
                while do != 4:
                    do = int(input("Please choose what do you want to do:\n"
                                   "1 - change student's name\n"
                                   "2 - change student's last name\n"
                                   "3 - change student's passport\n"
                                   "4 - exit\n"))
                    if do == 1:
                        new_name = input("Please enter new name")
                        selected_student.name = new_name
                    elif do == 2:
                        new_surname = input("Please enter new last name")
                        selected_student.last_name = new_surname
                    elif do == 3:
                        new_passport = input("Please enter new passport")
                        selected_student.passport = new_passport
                    print(selected_student)

            elif do == 5:
                index = choose_student(students)
                while do != 3:
                    do = int(input("Please choose what do you want to do:\n"
                                   "1 - add mark\n"
                                   "2 - delete mark\n"
                                   "3 - exit\n"))
                    if do == 1:
                        mark = ''
                        while mark != "end":
                            mark = input("Please enter a number\n")  # here a problem
                            print("If you have already finished entering numbers, write - \"end\" ")
                            students[index].add_mark(mark)
                            # save object to file

                    if do == 2:
                        mark = int(input("Which grade do you want to remove"))
                        students[index].remove_mark(mark)
                        # save object to file
            elif do == 6:
                index = choose_student(students)
                print("The student", students[index], "\n has such an average mark = ",
                      students[index].calc_average_mark())

            elif do == 7:
                #  choose: pickle, json, sqlite
                do = int(input("Please choose the type of storage:\n"
                               "1 - pickle\n"
                               "2 - json\n"
                               "3 - sqlite\n"))
                if do == 1:
                    s = StoragePickle()

                elif do == 2:
                    s = StorageJSON()

                elif do == 3:
                    # s = StorageSqlite
                    pass

            elif do == 8:
                # SAVE from choose: pickle, json, sqlite
                s.save(students)

            elif do == 9:
                # LOAD from choose: pickle, json, sqlite
                students = s.load()


        # except TypeError as e1:
        #     # Incorrect type for student
        #     print("A type error!")
        #     print(e1)
        #
        # except ValueError as e2:
        #     # user entered literal instead of number or other incorrect input
        #     print("A value error!")
        #     print(e2)
        #
        # except IndexError as e3:
        #     print("An index error!")
        #     print(e3)
        #
        # except EOFError as e4:
        #     print("An end of line error")
        #     print(e4)

        except Exception as e:
            # print("Exception")
            # print(e)
            raise e


if __name__ == "__main__":
    main()
#
