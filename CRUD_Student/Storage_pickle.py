import pickle
import os

from Storage import Storage




class StoragePickle(Storage):

    # why i need method because i have already the students.pickle
    def __init__(self):
        self._file_name = "students.pickle"

    def save(self, students):
        with open(self._file_name, 'wb') as students_file:
            pickle.dump(students, students_file)

    def load(self):
        if os.path.getsize(self._file_name) > 0:
            with open(self._file_name, 'rb') as students_file:
                return pickle.load(students_file)
#
