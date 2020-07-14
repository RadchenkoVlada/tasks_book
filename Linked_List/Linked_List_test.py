import unittest
from Linked_List import LinkedList
from Node import Node


class TestLinkedList(unittest.TestCase):
    """
    My first unittest ever, it checks if __bool__ method works correctly
    """
    def test_1__bool__(self):
        n1 = Node(1)
        ll = LinkedList(n1)
        self.assertTrue(bool(ll), True)


if __name__ == '__main__':
    """A simple way to run the tests"""
    unittest.main()
