__author__ = 'Cassio dos Santos Sousa'

from is_substring import is_substring


# Given the use of only one is_substring() command, checks if a word is a rotation of another word.


def is_rotation(ref, word):
    if len(ref) != len(word):
        return False
    if len(ref) == 0:
        return True
    return is_substring(ref + ref, word)


# Test cases. The initial print is only to differentiate from is_substring() tests.

print "\nFrom IS_ROTATION\n"

print is_rotation("", "") == True
print is_rotation("a", "") == False
print is_rotation("a", "a") == True
print is_rotation("abc", "bca") == True
print is_rotation("abcdef", "abcdfe") == False
print is_rotation("girafarig", "girafarig") == True
