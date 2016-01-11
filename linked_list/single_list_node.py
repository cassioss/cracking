__author__ = 'Cassio dos Santos Sousa'


# Defines the node of a singly linked list.

class SingleLinkNode:
    # Initializes the node.

    def __init__(self, val):
        self.val = val
        self.next = None

    # Returns the length of this list, by returning the total number of nodes linked to this one.
    # If no node is linked, returns 1.

    def __len__(self):
        counter = 1
        reference = self
        while reference.next is not None:
            reference = reference.next
            counter += 1
        return counter

    # Prints the entire list connected to this node.

    def __str__(self):
        if self is None:
            return "None"
        word = str(self.val)
        current = self
        while current.next is not None:
            current = current.next
            word += " --> " + str(current.val)
        return word

    # Appends a new node to the end of the list. Since it is necessary to reach the final value, this algorithm is O(n).

    def append(self, val):
        current = self
        while current.next is not None:
            current = current.next
        current.next = SingleLinkNode(val)

    # It is assumed that a node cannot delete itself without having a next one. Otherwise,
    # its existence would not make any sense. This algorithm is O(n), being n the number of nodes linked to this one.

    def delete_node(self, val):
        current = self
        if current.val == val and current.next is not None:
            current.val = current.next.val
            current.next = current.next.next
        else:
            while current.next is not None:
                if current.next.val == val:
                    current.next = current.next.next
                    return
                current = current.next


# Simple tests for the data structure.

def basic_tests():
    print "\nBasic tests are coming:\n"

    head = SingleLinkNode(0)
    print head
    print len(head)
    head.append(1)
    print head
    head.append(2)
    print head
    head.append(3)
    print head
    head.append(2)
    print head
    print len(head)
    head.append(3)
    print head
    print len(head)
    head.delete_node(0)
    print head
    head.delete_node(3)
    print head
    print len(head)
    head.delete_node(2)
    print head
    head.delete_node(2)
    print head
    head.delete_node(1)
    print head
