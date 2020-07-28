import unittest

from LinkedListIterator import LinkedListIterator
from Linked_List import LinkedList
from Node import Node


# https://docs.python.org/3/library/unittest.html#assert-methods

class TestLinkedList(unittest.TestCase):
    def test__str__list(self):
        n1 = Node(1)
        n2 = Node(7)
        n1.pointer_next = n2
        ll = LinkedList(n1)
        self.assertEqual(str(ll), "LinkedList(1, 7)")

    def test__str__empty_list(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "LinkedList()")

    def test__bool__(self):
        """Unittest checks if __bool__ method works correctly"""
        n1 = Node(1)
        ll = LinkedList(n1)
        self.assertTrue(ll)
        self.assertFalse(LinkedList())

    def test__len__list(self):
        n1 = Node(1)
        n2 = Node(7)
        n1.pointer_next = n2
        ll = LinkedList(n1)
        self.assertEqual(len(ll), 2)

    def test__len__empty_list(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)

    def test__getitem__(self):
        """ get by index an element : l[]"""
        ll = LinkedList(Node(10))
        self.assertRaises(IndexError, ll.__getitem__, 2)
        self.assertRaises(TypeError, ll.__getitem__, False)
        self.assertRaises(TypeError, ll.__getitem__, "test data")
        self.assertEqual(ll[0].data, 10)
        self.assertEqual(ll[-1].data, 10)

    def test__delitem__(self):
        """ Removes an item by index"""
        n1 = Node(12)
        n2 = Node(2)
        n1.pointer_next = n2
        ll = LinkedList(n1)
        self.assertRaises(IndexError, ll.__delitem__, 2)
        self.assertRaises(TypeError, ll.__delitem__, "Ivan")

        ll.__delitem__(1)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll[0].data, 12)

    def test__delitem__empty_list(self):
        self.assertRaises(IndexError, LinkedList().__delitem__, 0)

    def test__iter__(self):
        ll = LinkedList()
        ll.right_append(100)
        ll.right_append(99)
        ll.left_append(0)
        iterator = iter(ll)
        self.assertEqual(next(iterator), 0)
        self.assertEqual(next(iterator), 100)
        self.assertEqual(next(iterator), 99)
        self.assertRaises(StopIteration, next, iterator)

    def test__contains__(self):
        ll = LinkedList()
        ll.right_append(3)
        ll.right_append(5)
        self.assertEqual(ll.__contains__(3), True)
        self.assertEqual(ll.__contains__(10), False)

    def test_left_append_empty_list(self):
        ll = LinkedList()
        ll.left_append(10)
        self.assertCountEqual(ll, LinkedList(Node(10)))

    def test_left_append(self):
        ll = LinkedList()
        ll.left_append(3)
        ll.left_append(1000)

        self.assertEqual(ll.head.data, 1000)
        self.assertEqual(ll.head.pointer_next.data, 3)
        self.assertIsNone(ll.head.pointer_next.pointer_next)

    def test_right_append_empty_list(self):
        ll = LinkedList()
        ll.right_append(700)

        self.assertEqual(ll.head.data, 700)
        self.assertIsNone(ll.head.pointer_next)

    def test_right_append(self):
        ll = LinkedList()
        ll.right_append(5)
        ll.right_append(7)

        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.head.pointer_next.data, 7)
        self.assertIsNone(ll.head.pointer_next.pointer_next)

    def test_delete_first_el_empty_list(self):
        ll = LinkedList()
        self.assertRaises(ValueError, ll.delete_first_el)

    def test_delete_first_el(self):
        n1 = Node(1)
        n2 = Node(7)
        n1.pointer_next = n2
        ll = LinkedList(n1)
        ll.delete_first_el()

        self.assertEqual(ll.head.data, 7)
        self.assertIsNone(ll.head.pointer_next)

    def test_delete_last_el_empty_list(self):
        ll = LinkedList()
        self.assertRaises(ValueError, ll.delete_last_el)

    def test_delete_last_el(self):
        n1 = Node(1)
        n2 = Node(7)
        n1.pointer_next = n2
        ll = LinkedList(n1)
        ll.delete_last_el()

        self.assertEqual(ll.head.data, 1)
        self.assertIsNone(ll.head.pointer_next)



if __name__ == '__main__':
    """A simple way to run the tests,
    You can run tests with more detail (higher verbosity) by passing in the -v flag 
    or verbosity=2 as an argument"""

    unittest.main(verbosity=2)
