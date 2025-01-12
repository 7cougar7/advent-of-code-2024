from copy import deepcopy
import signal
from tqdm import tqdm

## Part 1 Solution ##
original_grid = []
start_pos = (-1, -1)
directions = [  # (y, x)
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]
barrier = '#'
path = 'X'
with open('input.txt', 'r') as f:
    for line in f.readlines():
        trimmed_line = line.strip()
        original_grid.append(list(trimmed_line))
        if '^' in trimmed_line:
            start_pos = ((len(original_grid) - 1), trimmed_line.index('^'))

def traverse(start_position, grid):
    y = 0
    x = 1
    current_position = start_position
    current_direction = (-1, 0)
    next_position = [sum(x) for x in zip(current_position, current_direction)]
    while True:
        grid[current_position[y]][current_position[x]] = path
        if next_position[y] < 0 or next_position[y] == len(grid) or next_position[x] < 0 or next_position[x] == len(grid[0]):
            break
        next_char = grid[next_position[y]][next_position[x]]
        if next_char == barrier:
            current_direction = directions[(directions.index(current_direction) + 1) % len(directions)]
            next_position = [sum(x) for x in zip(current_position, current_direction)]
            continue
        current_position = next_position
        next_position = [sum(x) for x in zip(current_position, current_direction)]
    return grid

traversed_grid = traverse(start_pos, deepcopy(original_grid))
print("Day 6, Part 1 Answer:", sum([1 if char == path else 0 for row in traversed_grid for char in row]))


## Part 2 Solution ##

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

possible_solutions = 0
for y_to_change in tqdm(range(len(original_grid)), leave=False):
    for x_to_change in tqdm(range(len(original_grid[0])), leave=False):
        grid_copy = deepcopy(original_grid)
        grid_copy[y_to_change][x_to_change] = barrier
        signal.setitimer(signal.ITIMER_REAL, 0.5)  # Should be able to find path out in under 0.5 seconds
        try:
            traverse(start_pos, grid_copy)  # Whatever your function that might hang
        except TimeoutException:
            possible_solutions += 1
            continue  # continue the for loop if function takes more than 0.5 secondx

print("Day 6, Part 2 Answer:", possible_solutions)
