
LENGTH_OF_PASSPORT = 9


class Student:
    def __init__(self, name: str, last_name : str, passport: str):
        self.name = name
        self.last_name = last_name
        self.passport = passport
        self.all_marks = []

    def add_mark(self, mark):
            if mark.isnumeric():
                number = int(mark)
                self.all_marks.append(number)
                self.calc_average_mark()

    def remove_mark(self, mark):
        self.all_marks.remove(mark)

    def calc_average_mark(self):
        # where should i put this "division by zero"
        if len(self.all_marks) == 0:
            print("Division by zero - ")
            return 0
        else:
            avg_mark = sum(self.all_marks) / len(self.all_marks)
        return avg_mark

    def __str__(self):
        return "name - {0}, last name - {1}, passport = {2}, all marks = {3}".format(self.name, self.last_name,
                                                                                     self.passport, self.all_marks)

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Last name must be str type")
        self._name = new_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        if not isinstance(new_last_name, str):
            raise TypeError("Last name must be str type")
        self._last_name = new_last_name

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, new_passport):
        if not isinstance(new_passport, str):
            raise TypeError("Passport must be str type")
        if not new_passport.isnumeric() or len(new_passport) != LENGTH_OF_PASSPORT:
            raise Exception("Incorrect passport value")
        self._passport = new_passport


#
