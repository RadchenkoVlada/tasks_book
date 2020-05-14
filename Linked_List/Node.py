class Node:
    def __init__(self, data, pointer_next=None):
        self.data = data
        self.pointer_next = pointer_next

    def __str__(self):
        return str(self.data)

# sys.getrefcount()
