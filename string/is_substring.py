__author__ = 'cassio'


# Checks if a word is substring of another one. Given that m = len(ref) and n = len(word), the algorithm has an O(n)
# loop that makes O(m) checks whenever the initial character of the word is found in the reference string. The worst
# case scenario is O(nm).

def is_substring(ref, word):
    if len(ref) < len(word):
        return False
    if len(ref) == 0 or len(word) == 0:
        return True
    for i in range(len(ref) - len(word) + 1):
        if ref[i] == word[0] and _check_substring(ref, word, i):
            return True
    return False


# Iterates over the word to see if the next characters of the reference string match the word. It is O(m).

def _check_substring(ref, word, i):
    j = 1
    while j < len(word):
        if ref[j + i] != word[j]:
            return False
        j += 1
    return True


# Exhaustive test cases.

print is_substring("", "") == True
print is_substring("a", "") == True
print is_substring("", "a") == False
print is_substring("a", "a") == True
print is_substring("ab", "ba") == False
print is_substring("abcd", "abc") == True
print is_substring("abcde", "ad") == False
print is_substring("abc", "abce") == False
print is_substring("abc def", "ade bcf") == False
print is_substring("bbbbbbabbbb", "bba") == True
print is_substring("babbbb", "bba") == False
print is_substring("this is a really bia bib big string", " big ") == True
