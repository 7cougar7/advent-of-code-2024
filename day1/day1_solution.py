import numpy as np


## Part 1 Solution ##
left_list = []
right_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        contents = line.split()
        left_list.append(int(contents[0]))
        right_list.append(int(contents[1]))


left_list.sort()
right_list.sort()
distance = np.subtract(left_list, right_list)
distance_abs = np.abs(distance)

print("Part 1 Answer:", str(sum(distance_abs)))


## Part 2 Solution ##

uniqueness_score = 0
l_unique_values = np.unique(left_list)

for value in l_unique_values:
    uniqueness_score += (value * right_list.count(value))

print("Part 1 Answer:", str(uniqueness_score))
