__author__ = 'Cassio dos Santos Sousa'


# Compresses a string into each character and its number of repetitions.

def compressed(word):
    if len(word) == 0:
        return word
    current_char = word[0]
    char_count = 1
    compressed = ""
    for i in range(1, len(word)):
        if word[i] == current_char:
            char_count += 1
        else:
            compressed += current_char + str(char_count)
            current_char = word[i]
            char_count = 1
    return compressed + current_char + str(char_count)  # Gets the last character


# If the compressed string is smaller than the original string, returns the string.
# Otherwise, returns the compressed version.

def compress(word):
    reduced_word = compressed(word)
    if len(word) < len(reduced_word):
        return word
    else:
        return compressed(word)


print compress("") == ""
print compress("abc") == "abc"
print compress("aabcccccaaa") == "a2b1c5a3"
