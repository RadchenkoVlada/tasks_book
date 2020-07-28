from Node import Node
from Linked_List import LinkedList


if __name__ == '__main__':
    """
    help()
    The Python help function can be super helpful for easily pulling up documentation for classes and methods. 
    We can call the help function on one of our classes, which will return some basic info about the methods defined 
    in our class

    """

    """create LinkedList"""
    n1 = Node(1)
    n2 = Node(7)
    n1.pointer_next = n2
    ll = LinkedList(n1)
    ll.left_append(100)
    print(ll)
    # # ll = LinkedList()
    # print(ll)
    # if ll:
    #     print("Not empty!")
    """length of LinkedList"""

    # print(len(ll))

    """append to left"""
    # print(ll)
    # ll.left_append(42)
    # ll.left_append(2)
    # print(ll)
    """check list for emptiness"""
    # if ll.is_empty():
    #     print("Empty")
    # else:
    #     print("Not empty")
    """test append_right"""
    # ll1 = LinkedList(None)
    # # print(f"none - {len(ll1)}")
    # ll1 = LinkedList(Node(0))
    # #
    # ll.right_append(10)
    # ll.right_append(16)
    # type(print(ll))
    # print(len(ll1))
    """delete_first_el"""
    # print(ll1)
    # ll1.delete_first_el()
    # print(ll1)
    # print(ll1)
    """delete_last_el"""
    # ll1.delete_last_el()
    # print(ll1)
    """delete_by_index"""
    # ll1.__delitem__(0)
    # # ll1 must be empty now: LinkedList()
    # print(ll1)

    """magic __len__()"""
    # print(len(ll))
    """magic __bool__"""
    # print(ll)
    # if ll:
    #     print("Not empty")
    # else:
    #     print("Empty")
    """magic __getitem__()"""
    # print(len(ll))
    # print(ll)
    # print(ll[-20])
    """magic __delitem__()"""
    # del ll[-1]
    # print(ll)
    # del ll[0]
    # print(ll)
    """magic __contains__"""
    # print(ll)
    # if 7 in ll:
    #     print("Vlada SUPER PRO")
    #
    # sum = 0
    # for i in ll:
    #     sum += i
    # print(sum)

    """magic __iter__"""
    # for el in ll:
    #     print(f"contains {el}")

    # General Purpose: client code
    #TODO: implement search
    # n1 = ll.search(1) # Node(1, None)
    # n2 = ll.search(42) # Node(42, ...) # next is 2
    # print(n2 is ll.head) # True

