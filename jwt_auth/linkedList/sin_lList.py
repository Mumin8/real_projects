class Node:
    def __init__(self, data):
        """the node of the singly linkedList"""
        self.data = data
        """Each node has a time stamp"""
        self.timestamp = datetime.datetime.now()
        self.next = None
class LinkedList:
    """the LinkedList"""
    def __init__(self):
        self.head = None
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
