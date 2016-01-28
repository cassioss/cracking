__author__ = 'Cassio dos Santos Sousa'


# Similar to the change-making problem, only now you are required to return the number of ways to generate a
# pack of N sodas for a given set of available soda packs with m sodas (in infinite amount).

ways_to_soda_packs = [[None for x in range(1000)] for y in range(1000)]
sodas = [1, 4, 6, 9]


def soda_problem(n):
    # It is impossible to form an N-soda pack if the m-soda packs are empty/null or invalid (negative-pack or 0-pack).

    if not all(packs > 0 for packs in sodas) or (sodas is None or len(sodas) is 0):
        return -1

    return _soda_problem(n, [], 0)


# Iterative way to make sure you will go through all possible packing scenarios

def _soda_problem(n, pack_list, current):
    if n < 0 or current is len(sodas):
        return 0
    if n == 0:
        return 1

    if ways_to_soda_packs[n][current] is not None:
        return ways_to_soda_packs[n][current]

    # New lists are required in order to lose reference from the original list

    pack_list_with_current = list(pack_list)
    pack_list_with_current.append(sodas[current])

    pack_list_without_current = list(pack_list)

    first_iteration = _soda_problem(n - sodas[current], pack_list_with_current, current)
    second_iteration = _soda_problem(n, pack_list_without_current, current + 1)

    ways_to_soda_packs[n][current] = first_iteration + second_iteration

    return first_iteration + second_iteration


print soda_problem(10)
print soda_problem(20)
print soda_problem(30)
print soda_problem(40)
print soda_problem(50)
print soda_problem(100)
