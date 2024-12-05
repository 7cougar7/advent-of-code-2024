## Part 1 Solution ##

combos = [
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
xmas_constant = "XMAS"
height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        for indiv_combo in combos:
            word = "".join([
                grid[y + delta[1]][x + delta[0]]
                if x + delta[0] >= 0 and x + delta[0] < width and y + delta[1] >= 0 and y + delta[1] < height
                else ""
                for delta in indiv_combo
            ])
            if word == xmas_constant:
                count += 1

print("Day 4, Part 1 Answer: " + str(count))
