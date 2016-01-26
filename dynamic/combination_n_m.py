__author__ = 'Cassio dos Santos Sousa'

# Returns (n) or C(n,m), the combination of n elements when m elements are chosen.
#         (m)

previous_combinations = [[None for x in range(1000)] for y in range(1000)]


def combination(n, m):
    if n < m or m < 0 or n < 0:
        return 0
    if n == m or m is 0:
        return 1
    if previous_combinations[n][m] is not None:
        return previous_combinations[n][m]
    combination_n_m = combination(n - 1, m) + combination(n - 1, m - 1)
    previous_combinations[n][m] = combination_n_m
    return combination_n_m


print combination(-1, -2) == 0
print combination(0, 0) == 1
print combination(1, 1) == 1
print combination(2, 2) == 1
print combination(3, 3) == 1
print combination(4, 2) == 6
print combination(3, 2) == 3
print combination(5, 4) == 5
print combination(8, 4) == 70
