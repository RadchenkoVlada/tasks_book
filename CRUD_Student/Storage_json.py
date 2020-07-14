import json
from Storage import Storage
from Student import Student


class StorageJSON(Storage):
    def __init__(self):
        self._file_name = "students.json"

    def save(self, students):
        with open(self._file_name, "w") as write_file:
            # method dump() is used to write data to files
            json.dump([student.__dict__ for student in students], write_file)

    def load(self):
        with open(self._file_name, "r") as read_file:
            list_of_dicts = json.load(read_file)
        return [StorageJSON.trans(el) for el in list_of_dicts]

    #dict to Student
    #TODO add all_marks
    @staticmethod
    def trans(d):
        s = Student(d["_name"], d["_last_name"], d["_passport"])
        print(s.__dict__)
        return s
