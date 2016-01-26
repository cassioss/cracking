__author__ = 'Cassio dos Santos Sousa'

# A step is defined as one of three choices:
#
# (1) Subtract 1 from the number;
# (2) Divide the number by 2, if possible;
# (3) Divide the number by 3, if possible.
#
# The algorithm must be able to return the smallest amount of steps until 1.

minimal_steps_from_top = [None for x in range(1000)]
minimal_steps_from_bottom = [-1 for y in range(1000)]


# Top-down: the top most call calculates all the others.

def minimal_steps_to_1_top_down(n):
    if n < 1:
        return -1
    if n == 1:
        return 0

    if minimal_steps_from_top[n] is not None:
        return minimal_steps_from_top[n]

    steps = 1 + minimal_steps_to_1_top_down(n - 1)

    if n % 2 is 0:
        steps = min(steps, 1 + minimal_steps_to_1_top_down(n / 2))

    if n % 3 is 0:
        steps = min(steps, 1 + minimal_steps_to_1_top_down(n / 3))

    minimal_steps_from_top[n] = steps
    return steps


# Bottom-up approach - every value is calculated from the beginning.

def minimal_steps_to_1_bottom_up(n):
    if n < 1:
        return -1

    if minimal_steps_from_bottom[n] is not -1:
        return minimal_steps_from_bottom[n]

    minimal_steps_from_bottom[1] = 0

    for i in range(2, n + 1):
        minimal_steps_from_bottom[i] = 1 + minimal_steps_from_bottom[i - 1]

        if i % 2 == 0:
            minimal_steps_from_bottom[i] = min(minimal_steps_from_bottom[i], 1 + minimal_steps_from_bottom[i / 2])

        if i % 3 == 0:
            minimal_steps_from_bottom[i] = min(minimal_steps_from_bottom[i], 1 + minimal_steps_from_bottom[i / 3])

    return minimal_steps_from_bottom[n]


print minimal_steps_to_1_top_down(0) == -1
print minimal_steps_to_1_top_down(1) == 0
print minimal_steps_to_1_top_down(2) == 1
print minimal_steps_to_1_top_down(3) == 1
print minimal_steps_to_1_top_down(4) == 2
print minimal_steps_to_1_top_down(5) == 3
print minimal_steps_to_1_top_down(6) == 2
print minimal_steps_to_1_top_down(7) == 3
print minimal_steps_to_1_top_down(8) == 3
print minimal_steps_to_1_top_down(9) == 2
print minimal_steps_to_1_top_down(10) == 3

print minimal_steps_to_1_bottom_up(0) == -1
print minimal_steps_to_1_bottom_up(1) == 0
print minimal_steps_to_1_bottom_up(2) == 1
print minimal_steps_to_1_bottom_up(3) == 1
print minimal_steps_to_1_bottom_up(4) == 2
print minimal_steps_to_1_bottom_up(5) == 3
print minimal_steps_to_1_bottom_up(6) == 2
print minimal_steps_to_1_bottom_up(7) == 3
print minimal_steps_to_1_bottom_up(8) == 3
print minimal_steps_to_1_bottom_up(9) == 2
print minimal_steps_to_1_bottom_up(10) == 3
