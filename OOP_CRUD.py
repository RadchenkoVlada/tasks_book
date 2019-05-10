import re

class Student:
    def __init__(self, name, passport, last_name):
        self.name = name
        self.last_name = last_name
        # if re.search( , passport):
        self.passport = passport
            # raise exception

        self.avg_mark = 0
        self.all_marks = []

    def pass_exam(self, mark):
        if mark > 1:
            self.all_marks.append(mark)

    def add_mark(self):
        mark = input("Please enter a number\n")
        print("If you have already finished entering numbers, write - \"end \\")
        while mark != "done":
            self.all_marks.append(mark)

    def remove_mark(self, mark):
        self.all_marks.remove(mark)

    def get_average_mark(self):
        self.avg_mark = sum(self.all_marks) / len(self.all_marks)

    # def valid_passport(self):


def main():
    students = []
    do = " "
    stud = Student("Vlada", "Radchenko", "0000000001")
    while do != "exit":
        do = input("Do you want to work? (Y/N/exit):")
        if do == "Y":
            do = int(input("Please choose what do you want to do:\n"
                           "1- add a new student,\n"
                           "2- remove the student\n"
                           "3- show all students\n"
                           "4- change student attribute\n"
                           "5- exit\n"))

            if do == 1:
                name = input("Enter name")
                last_name = input("Enter last name")
                passport = input("Enter student surname")
                stud = Student(name, last_name, passport)
                print('A new student', stud)
                students.append(stud)
                print("Now the list of students looks like this", students)

            elif do == 2:
                print("The list of students looks like this:", students)
                number = int(input("Enter please student number in list starting with 1"))
                if 1 < number <= len(students):
                    number -= 1
                    del students[number]

            elif do == 3:
                for student in students:
                    print("name - ", student.name, "surname - ")
            elif do == 4:
                    do = int(input("Please choose what do you want to do:\n"
                                   "1- add a new student,\n"
                                   "2- remove the student\n"
                                   "3- show all students\n"
                                   "4- change student attribute\n"
                                   "5- exit\n"))

                    if do == 1:
                        pass
        elif do == "N":
            print("Goodbye")
        else:
            print("unknown answer")


if __name__ == "__main__":
    main()
#
