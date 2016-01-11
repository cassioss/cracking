__author__ = 'Cassio dos Santos Sousa'


# Checks if all characters of a string are unique.

def all_unique(a_string):
    if len(a_string) == 0:
        return False
    for i in range(len(a_string)):
        one_char = a_string[i]
        for j in range(i + 1, len(a_string)):
            another_char = a_string[j]
            if one_char == another_char:
                return False
    return True


# Now using an array to keep track of unicode characters.

def all_unique_hash(a_string):
    if len(a_string) == 0 or len(a_string) > 256:
        return False
    has_char = [False] * 256
    for i in range(len(a_string)):
        unicode_i = ord(a_string[i])
        if has_char[unicode_i]:
            return False
        else:
            has_char[unicode_i] = True
    return True


print all_unique("") == False
print all_unique("a") == True
print all_unique("abcde") == True
print all_unique("a b c") == False

print all_unique_hash("") == False
print all_unique_hash("a") == True
print all_unique_hash("abcde") == True
print all_unique_hash("a b c") == False
