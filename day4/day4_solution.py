def in_range(x, y):
    return x >= 0 and x < width and y >= 0 and y < height

## Part 1 Solution ##

xmas_combos = [
    [(0,0), (1,0), (2,0), (3,0)], #straight right
    [(0,0), (-1,0), (-2,0), (-3,0)], #straight left
    [(0,0), (0,-1), (0,-2), (0,-3)], #straight up
    [(0,0), (0,1), (0,2), (0,3)], #straight down
    [(0,0), (1,1), (2,2), (3,3)], #down right
    [(0,0), (-1,1), (-2,2), (-3,3)], #down left
    [(0,0), (-1,-1), (-2,-2), (-3,-3)], #up left
    [(0,0), (1,-1), (2,-2), (3,-3)], #up right
]
grid = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip().upper())

count = 0
height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        for indiv_combo in xmas_combos:
            word = "".join([
                grid[y + delta[1]][x + delta[0]] if in_range(x + delta[0], y + delta[1]) else ""
                for delta in indiv_combo
            ])
            if word == "XMAS":
                count += 1

print("Day 4, Part 1 Answer: " + str(count))


## Part 2 Solution ##

match = ['M', 'S']
count_x_mas = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] != 'A':
            continue
        t2b_diag = sorted((
            grid[y+1][x+1] if in_range(y+1, x+1) else "",
            grid[y-1][x-1] if in_range(y-1, x-1) else ""
        ))
        b2t_diag = sorted((
            grid[y-1][x+1] if in_range(y-1, x+1) else "",
            grid[y+1][x-1] if in_range(y+1, x-1) else ""
        ))
        if t2b_diag == match and b2t_diag == match:
            count_x_mas += 1

print("Day 4, Part 2 Answer: " + str(count_x_mas))

one_line_count_x_mas = sum([1 if (grid[y][x] == 'A' and (sorted((grid[y+1][x+1] if in_range(y+1, x+1) else "", grid[y-1][x-1] if in_range(y-1, x-1) else "")) == match) and (sorted((grid[y-1][x+1] if in_range(y-1, x+1) else "", grid[y+1][x-1] if in_range(y+1, x-1) else "")) == match)) else 0 for y in range(height) for x in range(width)])
print("Day 4, Part 2 Answer (One line): " + str(one_line_count_x_mas))
