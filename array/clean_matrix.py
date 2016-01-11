__author__ = 'cassio'


#   If an mxn matrix has a zero as element, its row and column are set to zero.
#
#   0 1 0 3         ->      0 0 0 0
#   4 5 6 7                 0 9 0 1
#   8 9 A B                 0 A 0 2
#   C D E F                 0 B 0 3

def clean_matrix(mn_array):
    if len(mn_array) == 0:
        return mn_array

    m = len(mn_array)
    n = len(mn_array[0])

    rows_to_clean = set()
    columns_to_clean = set()

    for i in range(m):
        for j in range(n):
            if mn_array[i][j] == 0:
                rows_to_clean.add(i)
                columns_to_clean.add(j)

    for i in rows_to_clean:
        clean_row(mn_array, i, n)

    for j in columns_to_clean:
        clean_column(mn_array, j, m)

    return mn_array


def clean_row(mn_array, i, n):
    for j in range(n):
        mn_array[i][j] = 0


def clean_column(mn_array, j, m):
    for i in range(m):
        mn_array[i][j] = 0


# Prints a matrix from a double array in a more organized way (not the typical one-line).

def print_matrix(double_array):
    for some_array in double_array:
        print some_array
    print


matrix0 = [[]]

matrix1 = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
    [23, 24, 25, 26]
]

matrix2 = [
    [0, 12, 0, 14],
    [5, 16, 7, 18],
    [9, 20, 1, 22],
    [3, 24, 5, 26]
]

print_matrix(clean_matrix(matrix0))
print_matrix(clean_matrix(matrix1))
print_matrix(clean_matrix(matrix2))
