from collections.abc import Iterator
# from Linked_List import LinkedList


class LinkedListIterator(Iterator):

    def __init__(self, collection):
        """
        The constructor creates an object of type LinkedListIterator
        :param collection:
        """
        # LinkedList object reference
        # self._collection = collection
        # member variable to keep track of current index
        self._cur_head = collection.head

    def __iter__(self):
        """
        iterator.__iter__()
        Return the iterator object itself. This is required to allow both containers and iterators to be used with the
        for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in
        the Python/C API.
        """
        return self

    def __next__(self):

        """
        This method is called by the iterator in this case by __iter__ in LinkedList class.

        The __next __ () method should return the next element in the sequence.
        Upon reaching the end of the collection and in subsequent calls should be called
        StopIteration exception.

        Returns an element of LinkedList until it ends.
        """
        if self._cur_head is None:
            raise StopIteration
        else:
            res = self._cur_head.data
            self._cur_head = self._cur_head.pointer_next
            return res

        # if self._cursor >= int(len(self._collection)):
        #     # End of Iteration
        #     raise StopIteration
        # else:
        #     self._cursor += 1
        #     return self._collection.head
