__author__ = 'Cassio dos Santos Sousa'


# Finds all substrings that can be generated from a string. The worst case is O(n*(n-1)/2) = O(n^2).

def all_substrings(word):
    sub_set = set()
    if len(word) == 0:
        return sub_set
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            sub_set.add(word[i:j])
    return sub_set


# Test cases.

print all_substrings("") == set()
print all_substrings("a") == set(["a"])
print all_substrings("aa") == set(["a", "aa"])
print all_substrings("ab") == set(["a", "b", "ab"])
print all_substrings("banana") == set(
    ["b", "a", "n", "ba", "an", "na", "ban", "ana", "nan", "bana", "anan", "nana", "banan", "anana", "banana"])

# Print-test cases only.

print "abc -> " + str(all_substrings("abcde"))
print "abaab -> " + str(all_substrings("abaab"))
