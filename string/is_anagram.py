__author__ = 'Cassio dos Santos Sousa'


# Checks if two strings are anagrams.

def is_anagram(ref, word):
    if len(ref) != len(word):
        return False
    if len(ref) == 0:
        return True

    char_map = [0] * 256
    for i in range(len(ref)):
        char_map[ord(ref[i])] += 1
        char_map[ord(word[i])] -= 1

    for ascii in char_map:
        if char_map[ascii] != 0:
            return False

    return True


print is_anagram("", "") == True
print is_anagram("a", "a") == True
print is_anagram("ab", "ba") == True
print is_anagram("abcd", "abc") == False
print is_anagram("abc", "abce") == False
print is_anagram("abc def", "ade bcf") == True
