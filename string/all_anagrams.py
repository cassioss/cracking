__author__ = 'Cassio dos Santos Sousa'


# Finds all the anagrams of a given word.

def all_anagrams(word):
    if len(word) <= 1:
        return set(word)

    result_set = set()
    last_char = word[-1]
    last_char_off = word[:-1]

    for every_word in all_anagrams(last_char_off):
        for position in range(len(word)):
            result_set.add(put_in_middle(last_char, every_word, position))

    return result_set


# Puts a character in a specific position of a given word.

def put_in_middle(letter, word, position):
    first_part = word[:position]
    second_part = word[position:]
    return first_part + letter + second_part


print all_anagrams("")
print all_anagrams("a")
print all_anagrams("ab")
print all_anagrams("abc")
print all_anagrams("abba")
