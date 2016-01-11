__author__ = 'Cassio dos Santos Sousa'


# Swaps the minimum and maximum values of an integer array on their first occurrences.

def swap_min_max(int_array):
    if len(int_array) <= 1:
        return int_array

    min_pos = max_pos = 0
    min_val = max_val = int_array[0]

    for i in range(1, len(int_array)):
        if int_array[i] < min_val:
            min_val = int_array[i]
            min_pos = i
            continue
        if int_array[i] > max_val:
            max_val = int_array[i]
            max_pos = i
            continue

    int_array[min_pos], int_array[max_pos] = max_val, min_val

    return int_array


print swap_min_max([])
print swap_min_max([1])
print swap_min_max([1, 2])
print swap_min_max([1, 2, 4])
print swap_min_max([1, 2, 4, 3])
