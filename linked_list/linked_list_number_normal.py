from random import sample
from single_list_node import SingleLinkNode


# Implements an integer number in a list with its digits in normal order. Example: 617 is stored as 6 -> 1 -> 7.

def linked_number_normal(num):
    if num < 0:
        return None
    if num < 10:
        return SingleLinkNode(num)
    head = linked_number_normal(num / 10)
    head.append(SingleLinkNode(num % 10))
    return head


# Sum two numbers as lists in normal order.

def sum_normal(first_node, second_node):
    if first_node is None:
        return second_node
    if second_node is None:
        return first_node

    first_length = len(first_node)
    second_length = len(second_node)

    if first_length > second_length:
        return _sum_normal(first_node, complete_with_zeros(second_node, first_length - second_length))
    else:
        return _sum_normal(complete_with_zeros(first_node, second_length - first_length), second_node)


# Sums two numbers with the same number of digits in the regular order.

def _sum_normal(first_node, second_node):
    head, carry = carry_and_sum(first_node, second_node)
    if carry == 0:
        return head
    new_head = SingleLinkNode(carry)
    new_head.next = head
    return new_head


# Finds if there is a carrying unit in a sum of two numbers of equal length. Example: 90 + 10 has a carrying unit of 1
# (in order to form 100), while 90 + 09 has a carrying unit of 0 (to form 99). It then returns the sums and the carry.

def carry_and_sum(first_node, second_node):
    if first_node is None or second_node is None:
        return None, 0
    tail, carry = carry_and_sum(first_node.next, second_node.next)
    addition = carry + first_node.val + second_node.val
    head = SingleLinkNode(addition % 10)
    return head, addition / 10


# Adds a given amount of zeros to the beginning of a number, in order to allow a correct sum with a bigger number.

def complete_with_zeros(number_node, zeros):
    if zeros <= 0:
        return number_node
    head = SingleLinkNode(0)
    head.append(complete_with_zeros(number_node, zeros - 1))
    return head


# Implementation of multiple functions at once.

def sum_as_normal_list(first, second):
    return sum_normal(linked_number_normal(first), linked_number_normal(second))


# Test linked list creation for simple numbers.

def test_list_creation_normal(num_list):
    if len(num_list) > 0:
        print "\nIn normal order:\n"
        for num in num_list:
            print("{0:{width}} :: ".format(num, width=6) + str(linked_number_normal(num)))
        print


test_case = sample(range(-10000, 10001), 20)
test_list_creation_normal(test_case)
print sum_as_normal_list(120, 301)
