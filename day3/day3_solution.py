import re


## Part 1 Solution ##
mul_pattern = r"mul\(\d+,\d+\)"

mul_sum = 0
with open('input.txt', 'r') as f:
    contents = f.read()
    matches = re.findall(mul_pattern, contents)
    for match in matches:
        match = match[4:-1]
        values = list(map(int, match.split(',')))
        mul_sum += (values[0] * values[1])

print("Day 3, Part 1 Answer: " + str(mul_sum))


## Part 2 Solution ##
pattern_with_conditional = r"do\(\).+?don't\(\)"

mul_sum_toggle = 0
with open('input.txt', 'r') as f:
    contents = "do()%sdon't()" % f.read()
    one_line_contents = re.sub("\t|\r|\n", "", contents)
    valid_contents = "".join(re.findall(pattern_with_conditional, one_line_contents))

    matches = re.findall(mul_pattern, valid_contents)
    for match in matches:
        match = match[4:-1]
        values = list(map(int, match.split(',')))
        mul_sum_toggle += (values[0] * values[1])

print("Day 3, Part 2 Answer: " + str(mul_sum_toggle))
