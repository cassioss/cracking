__author__ = 'Cassio dos Santos Sousa'


# Replaces blank characters in a string with %20.
# Final blank spaces are removed, and multiple blank spaces are replaced by only one %20.

def remove_end_blanks(word):
    if len(word) == 0:
        return word
    if word[-1] == ' ':
        return remove_end_blanks(word[:-1])
    else:
        return word


def replace_blanks(word):
    clean_word = remove_end_blanks(word)
    if len(clean_word) == 0:
        return clean_word

    begin_blank = 0

    while clean_word[begin_blank] != " ":
        begin_blank += 1
        if begin_blank == len(clean_word):
            return clean_word

    end_blank = begin_blank
    while clean_word[end_blank] == ' ':
        end_blank += 1

    return clean_word[:begin_blank] + '%20' + replace_blanks(clean_word[end_blank:])


# Alternative solution using char array, in order to make this solution in place.
# It is assumed that there will be enough blank spaces at the end of the array to make a precise %20 addition.

def replace_blanks_in_array(word):
    char_array = list(word)
    spaces = 0
    last_char_pointer = 0

    for i in range(len(char_array)):
        if char_array[i] == ' ':
            spaces += 1
        else:
            last_char_pointer = i

    if spaces == 0:
        return word

    new_iterator = len(char_array) - 1

    while new_iterator >= 0:
        if char_array[last_char_pointer] != ' ':
            char_array[new_iterator] = char_array[last_char_pointer]
            last_char_pointer -= 1
            new_iterator -= 1
        else:
            char_array[new_iterator] = '0'
            char_array[new_iterator - 1] = '2'
            char_array[new_iterator - 2] = '%'
            new_iterator -= 3
            last_char_pointer -= 1

    return "".join(char_array)


print remove_end_blanks("") == ""
print remove_end_blanks("    ") == ""
print remove_end_blanks("abc   ") == "abc"
print remove_end_blanks("j") == "j"

print replace_blanks("abc") == "abc"
print replace_blanks("abc   def") == "abc%20def"
print replace_blanks("abc def") == "abc%20def"
print replace_blanks("abc def gh i") == "abc%20def%20gh%20i"

print replace_blanks_in_array(" Mr John Smith      ") == "%20Mr%20John%20Smith"
print replace_blanks_in_array("Mr John Smith    ") == "Mr%20John%20Smith"
