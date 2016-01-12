# Gets all permutations of a string.

string_subsets = [[None for x in range(1000)] for y in range(1000)]


def all_permutations_of(a_string):
    if a_string is None or a_string is '':
        return []
    if len(a_string) is 1:
        return [a_string]
    for x in range(0, len(a_string) + 1):
        y = len(a_string) + 1 - x
        if string_subsets[x][y] is None:
            string_subsets[x][y] = a_string[x, y]
