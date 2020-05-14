from Node import Node
from Linked_List import LinkedList
from Iter import LinkedListIterator, LinkedCollection

if __name__ == '__main__':
    """create LinkedList"""
    n1 = Node(1)
    # n2 = Node(7)
    # n1.pointer_next = n2
    # ll = LinkedList(n1)
    ll = LinkedList()
    # ll.delete_first_el()
    # print(ll)
    """length of LinkedList"""
    # print(len(ll))

    """append to left"""
    # print(ll)
    ll.left_append(42)
    ll.left_append(2)
    # print(ll)
    """check list for emptiness"""
    # if ll.is_empty():
    #     print("Empty")
    # else:
    #     print("Not empty")
    """test append_right"""
    # ll1 = LinkedList(None)
    # print(f"none - {len(ll1)}")
    # ll1 = LinkedList(Node(0))
    #
    ll.right_append(10)
    ll.right_append(16)
    #
    # print(len(ll1))
    """get_by_index"""
    # print(ll1.get_by_index(3))
    """delete_first_el"""
    # print(ll1)
    # ll1.delete_first_el()
    # print(ll1)
    # print(ll1)
    """delete_last_el"""
    # ll1.delete_last_el()
    # print(ll1)
    """delete_by_index"""
    # ll1.delete_by_index(1)
    # print(ll1)

    """magic 1"""
    # print(len(ll))
    """magic 2"""
    # print(ll)
    # if ll:
    #     print("Not empty")
    # else:
    #     print("Empty")
    """magic 3"""
    # print(len(ll))
    # print(ll)
    # print(ll[-20])
    """magic 4"""
    # print(ll)
    # del ll[-1]
    # print(ll)
    # del ll[0]
    # print(ll)
    """magic 5"""
    # print(ll)
    # print(10 in ll)
    #
    print(ll)
    for i in ll:
        print("fuck ", i)
    # print(ll)
    """magic 6"""
    # for el in ll:
    #     print(f"contains {el}")
    l = [1, 2, 3]
    iterator = iter(l)
    next(iterator)

    # General Purpose: client code
    # ll = LinkedList()  # так не работает, если в аргумент подать None - работает
    # ll.append(42)
    # ll.append(2)
    # ll.append(3)
    # ll.append(7)
    # ll.append(1)
    #
    # print(ll.is_empty())
    #
    # if ll.is_empty():
    #     print("Empty")
    # else:
    #     print("Not empty")
    #
    # print(len(ll))  # 5
    # print(len(LinkedList()))  # 0
    #
    # print(ll.get_by_index(3)) # 7
    # print(ll.get_by_index(10)) # exception
    #
    # ll.remove_by_index(3)
    # print(ll) # LinkedList(3, 2, 3, 1)
    #
    # n1 = ll.search(1) # Node(1, None)
    # n2 = ll.search(42) # Node(42, ...) # next is 2
    # print(n2 is ll.head) # True

    # for i in ll:
    #     print(i)
    #
    # print(ll)
    # print(ll[3])
