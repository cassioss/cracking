__author__ = 'Cassio dos Santos Sousa'


# Reverses a mutable array.

def reverse_array(mutable_array):
    if len(mutable_array) <= 1:
        return mutable_array
    begin = 0
    end = len(mutable_array) - 1
    while end > begin:
        mutable_array[begin], mutable_array[end] = mutable_array[end], mutable_array[begin]
        begin += 1
        end -= 1
    return mutable_array


# Reverses a string, an immutable array.

def reverse_string(some_string):
    if len(some_string) <= 1:
        return some_string
    return some_string[-1] + reverse_string(some_string[1:-1]) + some_string[0]


print reverse_string("") == ""
print reverse_string("a") == "a"
print reverse_string("abcde") == "edcba"
print reverse_string("girafarig") == "girafarig"

print reverse_array([]) == []
print reverse_array([1]) == [1]
print reverse_array([1, 2]) == [2, 1]
print reverse_array([1, 2, 3]) == [3, 2, 1]
print reverse_array([5, 4, 9, 4, 5]) == [5, 4, 9, 4, 5]
