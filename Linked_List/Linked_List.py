from Iter import LinkedListIterator
from Node import Node
from collections.abc import Iterable, Iterator

class LinkedList:
    def __init__(self, head: Node = None) -> object:
        self.head = head

    def __str__(self):
        if self.head is None:
            return "LinkedList()"
        else:
            res = "LinkedList(" + str(self.head.data)
            curr_node = self.head
            # TODO: use usual for when it will be ready ?
            while curr_node.pointer_next is not None:
                res += ", " + str(curr_node.pointer_next.data)
                curr_node = curr_node.pointer_next
            return res + ')'

    def __len__(self):
        length = 0
        if self.head is not None:
            cur_head = self.head
            length = 1
            # TODO: use usual for when it will be ready ?
            while cur_head.pointer_next is not None:
                length += 1
                cur_head = cur_head.pointer_next
        return length

    def __bool__(self):
        return self.head is not None

    """Called to implement evaluation of self[key]."""

    def __getitem__(self, index: int):
        """
        If key is of an inappropriate type, TypeError may be raised; if of a value outside the set of indexes for the
        sequence (after any special interpretation of negative values), IndexError should be raised.
        For mapping types, if key is missing (not in the container), KeyError should be raised.
        """
        length = len(self)
        if index >= length or index < -length:
            raise IndexError
        if type(index) is not int:
            raise TypeError(f'Invalid argument type: {type(index)}')
        if index < 0:
            cur_index = -length
        else:
            cur_index = 0
        cur_head = self.head
        while cur_index != index:
            cur_head = cur_head.pointer_next
            cur_index += 1
        return cur_head

    def __delitem__(self, index):
        length = len(self)
        if index >= length or index < -length:
            raise IndexError(f"The index out of range in Linked List")
        if type(index) is not int:
            raise TypeError(f'Invalid argument type: {type(index)}')
        if not self:
            raise ValueError('The LinkedList is empty!')

        elif index == 0 or index == -length:
            self.delete_first_el()
        else:
            previous_item = self[index - 1]
            previous_item.pointer_next = previous_item.pointer_next.pointer_next

    def __iter__(self):
        return LinkedListIterator(self)

    # doesn't work
    # def __contains__(self, item):
    #     print("Calling __contains__")
    #     cur = self.head
    #     while item != cur:
    #         self.__next__()
    #         if item == cur:
    #             return True
    #         else:
    #             return False

    # no return in this function
    def left_append(self, input):
        # empty linked_list
        if not self:
            self.head = Node(input)
            self.head.pointer_next = None
        else:
            node_head = self.head
            self.head = Node(input)
            self.head.pointer_next = node_head

    # no return in this function
    def right_append(self, input):
        # empty linked_list
        if not self:
            self.head = Node(input)
        else:
            cur_head = self.head
            while cur_head.pointer_next is not None:
                cur_head = cur_head.pointer_next
            cur_head.pointer_next = Node(input)

    def delete_first_el(self):
        if not self:
            raise ValueError('The LinkedList is empty!')
        else:
            self.head = self.head.pointer_next

    def delete_last_el(self):
        if not self:
            raise ValueError('The LinkedList is empty!')
        elif len(self) == 1:
            self.head = None
        else:
            cur_head = self.head
            future_last_elem = cur_head
            while cur_head.pointer_next is not None:
                future_last_elem = cur_head
                cur_head = cur_head.pointer_next
            future_last_elem.pointer_next = None

    def search(self):  # n1 = ll.search(1) # Node(1, None)
        pass









