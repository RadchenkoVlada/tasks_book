from collections.abc import Iterable, Iterator
from Node import Node
from Linked_List import LinkedList


class LinkedListIterator(Iterator):

    def __init__(self, collection: Node, cursor):
        self.collection = collection
        self.cursor = cursor

    def __next__(self):
        """
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        """
        try:
            print("Calling __next__")
            # in my case __next__ must return Node, but also remember previous Node
            if self.head is not None:
                return self.head
            else:
                raise StopIteration
