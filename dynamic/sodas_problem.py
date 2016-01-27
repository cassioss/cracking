__author__ = 'Cassio dos Santos Sousa'


# Similar to the change-making problem, only now you are required to return all possible ways to generate a
# pack of N sodas for a given set of available soda packs with m sodas (in infinite amount).


def soda_problem(n, sodas):
    # It is impossible to form an N-soda pack if the m-soda packs are empty/null or invalid (negative-pack or 0-pack).

    if not all(packs > 0 for packs in sodas) or (sodas is None or len(sodas) is 0):
        return -1

    return _soda_problem(n, sodas, [], 0)


# Iterative way to make sure you will go through all possible packing scenarios

def _soda_problem(n, sodas, pack_list, current):
    if n < 0 or current is len(sodas):
        return 0
    if n == 0:
        return 1

    # New lists are required in order to lose reference from the original list

    pack_list_with_current = list(pack_list)
    pack_list_with_current.append(sodas[current])

    pack_list_without_current = list(pack_list)

    first_iteration = _soda_problem(n - sodas[current], sodas, pack_list_with_current, current)
    second_iteration = _soda_problem(n, sodas, pack_list_without_current, current + 1)

    return first_iteration + second_iteration


print soda_problem(30, [4, 6, 9])
