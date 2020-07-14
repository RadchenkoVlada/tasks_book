class Node:
    def __init__(self, data, pointer_next=None):
        """
        The constructor creates an object with fields data and pointer_next which indicates the next element or its absence
        :param data: int, optional
        :param pointer_next: None
        """
        self.data = data
        self.pointer_next = pointer_next

    def __str__(self):
        """
        method returns readable text for the user
        :return: str
        """
        return str(self.data)
