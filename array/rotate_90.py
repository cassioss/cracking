__author__ = 'Cassio dos Santos Sousa'


# Rotates an NxN array 90 degrees counterclockwise. It is assumed that only square arrays are received.
#
#   0 1 2 3         ->      C 8 4 0                 01 13 32 20
#   4 5 6 7                 D 9 5 1                 00 03 33 30
#   8 9 A B                 E A 6 2                 11 12 22 21
#   C D E F                 F B 7 3                 ij j(I) (I)(J) (J)i

def rotate_90(n_array):
    if len(n_array) <= 1:
        return n_array
    opposite = len(n_array) - 1
    x_range = len(n_array) / 2
    y_range = len(n_array) / 2
    if opposite % 2 == 0:
        y_range += 1
    for i in range(x_range):
        for j in range(y_range):
            temp = n_array[i][j]
            n_array[i][j] = n_array[j][opposite - i]
            n_array[j][opposite - i] = n_array[opposite - i][opposite - j]
            n_array[opposite - i][opposite - j] = n_array[opposite - j][i]
            n_array[opposite - j][i] = temp
    return n_array


# Prints a matrix from a double array in a more organized way (not the typical one-line).

def print_matrix(double_array):
    for some_array in double_array:
        print some_array
    print


matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
    [23, 24, 25, 26]
]

matrix2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix3 = [
    [0, 1],
    [2, 3]
]

matrix4 = [
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
]

print_matrix(matrix)
print_matrix(rotate_90(matrix))
print_matrix(rotate_90(matrix2))
print_matrix(rotate_90(matrix3))
print_matrix(rotate_90(matrix4))
