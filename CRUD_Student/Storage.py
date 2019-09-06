from abc import ABCMeta, abstractmethod


class Storage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self, students):
        pass

    @abstractmethod
    def load(self):
        pass

#
