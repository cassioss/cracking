# Returns all combinations of n pairs of parentheses, properly opened and closed.

conversion_to_parentheses = [None for x in range(10000)]


def all_n_parentheses(n):
    if n <= 0:
        return []
    if n == 1:
        return ['()']


def convert_to_parentheses(some_integer):
    if conversion_to_parentheses[some_integer] is not None:
        return conversion_to_parentheses[some_integer]

