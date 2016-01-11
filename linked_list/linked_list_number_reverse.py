from random import sample
from single_list_node import SingleLinkNode


# Implements an integer number in a list with its digits in reverse order. Example: 617 is stored as 7 -> 1 -> 6.

def linked_number_reverse(num):
    if num < 0:
        return None
    if num < 10:
        return SingleLinkNode(num)
    head = SingleLinkNode(num % 10)
    head.next = linked_number_reverse(num / 10)
    return head


# Sums two numbers turned into reverse linked lists.

def sum_reverse(first_num_node, second_num_node):
    if first_num_node is None:
        return second_num_node
    if second_num_node is None:
        return first_num_node

    return _sum_reverse(first_num_node, second_num_node, 0)


# Iterative call of the function above.

def _sum_reverse(first_node, second_node, carry):
    if first_node is None and second_node is None:
        if carry == 1:
            return SingleLinkNode(carry)
        else:
            return None

    addition = carry

    if first_node is not None:
        addition += first_node.val

    if second_node is not None:
        addition += second_node.val

    current = SingleLinkNode(addition % 10)
    current.next = _sum_reverse(first_node.next, second_node.next, addition / 10)
    return current


# Natural implementation of the sum above for two positive integers.

def sum_as_reverse_list(first, second):
    if first >= 0 and second >= 0:
        return sum_reverse(linked_number_reverse(first), linked_number_reverse(second))
    return None


# Test linked list creation for simple numbers.

def test_list_creation_reverse(num_list):
    if len(num_list) > 0:
        print "\nIn reverse order:\n"
        for num in num_list:
            print("{0:{width}} :: ".format(num, width=6) + str(linked_number_reverse(num)))
        print


test_case = sample(range(-10000, 10001), 20)
test_list_creation_reverse(test_case)
print sum_as_reverse_list(587, 694)
