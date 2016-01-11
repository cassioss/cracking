__author__ = 'Cassio dos Santos Sousa'

ways_to_climb = [0 for x in range(500)]


# Function that returns the number of ways a child can climb a stair of n steps
# given that the child can climb 1, 2 or 3 steps at once.

def ways_to_climb_a_stair_of(n_steps):
    if n_steps <= 0:
        return 0
    if n_steps is 1:
        return 1
    if n_steps is 2:
        return 2
    if n_steps is 3:
        return 4

    if ways_to_climb[n_steps] != 0:
        return ways_to_climb[n_steps]

    ways_to_climb[n_steps] = ways_to_climb_a_stair_of(n_steps - 1) + ways_to_climb_a_stair_of(
        n_steps - 2) + ways_to_climb_a_stair_of(n_steps - 3)

    return ways_to_climb[n_steps]

print ways_to_climb_a_stair_of(0) == 0
print ways_to_climb_a_stair_of(1) == 1
print ways_to_climb_a_stair_of(2) == 2
print ways_to_climb_a_stair_of(3) == 4
print ways_to_climb_a_stair_of(4) == 7
