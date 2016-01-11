__author__ = 'Cassio dos Santos Sousa'


# Defines the node of a singly linked list.

class DoubleLinkNode:
    val = 0
    next = None
    prev = None

    def __init__(self, val):
        self.val = val

    def __str__(self):
        if self is None:
            return "None"
        word = str(self.val)
        current = self
        while current.next is not None:
            current = current.next
            word += " <-> " + str(current.val)
        return word

    def append(self, val):
        current = self
        while current.next is not None:
            current = current.next
        current.next = DoubleLinkNode(val)
        current.next.prev = current

    def delete_node(self, val):
        current = self
        if current.val == val and current.next is not None:
            current.val = current.next.val
            current.next = current.next.next
        else:
            while current.next is not None:
                if current.next.val == val:
                    current.next = current.next.next
                    current.next.prev = current
                    return
                current = current.next


# Simple tests for the data structure.

def basic_tests():
    print "\nBasic tests are coming:\n"
    head = DoubleLinkNode(0)
    print head
    head.append(1)
    print head
    head.append(2)
    print head
    head.append(3)
    print head
    head.append(2)
    print head
    head.append(3)
    print head
    print head.next.next.prev.prev.val
    head.delete_node(0)
    print head
    head.delete_node(3)
    print head
    head.delete_node(2)
    print head
    head.delete_node(2)
    print head
    head.delete_node(1)
    print head
