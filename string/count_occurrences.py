__author__ = 'Cassio dos Santos Sousa'


# Counts all occurrences of a substring inside a string. There are two ways to evaluate it:
#
# "bbb" - if i decide to check disjoint "bb" appearances, the algorithm returns 1;
#       - if i decide to check "bb" appearances not necessarily disjoint, the algorithm returns 2.
#
# Both algorithms will be constructed here.


# This algorithm counts appearances of a substring that might be joint (i.e. one character can be part of multiple
# substrings being counted).

def count_joint(word, sub):
    if len(word) < len(sub):
        return 0
    if len(sub) == 0:
        return len(word) + 1  # Empty strings
    count = 0
    i = 0
    while i < len(word) - len(sub) + 1:
        if word[i] == sub[0] and _check_substring(word, sub, i):
            count += 1
        i += 1
    return count


# This algorithm counts appearances of a substring that are disjoint (i.e. each character can be part of only one
# substring being counted).

def count_disjoint(word, sub):
    if len(word) < len(sub):
        return 0
    if len(sub) == 0:
        return len(word) + 1  # Empty strings
    count = 0
    i = 0
    while i < len(word) - len(sub) + 1:
        if word[i] == sub[0] and _check_substring(word, sub, i):
            count += 1
            i += len(sub)
        else:
            i += 1
    return count


# Starting from a matching initial, sees if the following characters of the reference strings match a substring.

def _check_substring(word, sub, i):
    j = 1
    while j < len(sub):
        if word[j + i] != sub[j]:
            return False
        j += 1
    return True


# Test cases for both functions.

print count_disjoint("", "") == count_joint("", "") == 1
print count_disjoint("abcde", "") == count_joint("abcde", "") == 6
print count_disjoint("", "a") == count_joint("", "a") == 0
print count_disjoint("abcde", "ad") == count_joint("abcde", "ad") == 0
print count_disjoint("abcde", "bcd") == count_joint("abcde", "bcd") == 1

print count_disjoint("abbba", "bb") == 1
print count_joint("abbba", "bb") == 2

print count_disjoint("bbbbbbb", "bbb") == 2
print count_joint("bbbbbbb", "bbb") == 5
