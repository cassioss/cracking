__author__ = 'Cassio dos Santos Sousa'

# Function that returns the number of ways a robot can go from (0,0) to (x,y)
# if it only knows how to move up or right by one unit (x, y integers).

moving_in_grid = [[0 for x in range(500)] for y in range(500)]


def ways_to_move_to(x, y):
    if x <= 0 and y <= 0:
        return 0
    if y == 0:
        return 1
    if x == 0:
        return 1
    if moving_in_grid[x][y] is not 0:
        return moving_in_grid[x][y]

    moving_in_grid[x][y] = ways_to_move_to(x - 1, y) + ways_to_move_to(x, y - 1)
    return moving_in_grid[x][y]


print ways_to_move_to(0,0) == 0
print ways_to_move_to(0,5) == 1
print ways_to_move_to(5,0) == 1
print ways_to_move_to(2,2) == 6
print ways_to_move_to(4,4) == 70
