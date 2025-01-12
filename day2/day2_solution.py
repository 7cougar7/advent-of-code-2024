import numpy as np

## Part 1 Solution ##
safe_levels = 0
with open('inputs.txt', 'r') as f:
    for line in f.readlines():
        report = list(map(int, line.split()))
        difference_lst = [(report[i+1] - report[i]) for i in range(len(report)-1)]
        difference_abs_lst = [abs(report[i+1] - report[i]) for i in range(len(report)-1)]
        # print(
        #     difference_lst, 
        #     max(difference_lst), 
        #     report == report_incr, 
        #     report == report_desc,
        #     max(difference_lst) < 4 and min(difference_lst) >= 1 and (all(level_diff > 0 for level_diff in difference_lst) or all(level_diff < 0 for level_diff in difference_lst))
        # )
        if max(difference_abs_lst) < 4 and min(difference_abs_lst) >= 1 and(
            all(level_diff > 0 for level_diff in difference_lst) or all(level_diff < 0 for level_diff in difference_lst)
        ):
             safe_levels += 1

print("Day 2, Part 1 Answer:", str(safe_levels))


## Part 2 Solution ##

def determine_difference_and_direction(report):
        difference_lst = [(report[i+1] - report[i]) for i in range(len(report)-1)]
        difference_abs_lst = [abs(report[i+1] - report[i]) for i in range(len(report)-1)]

        directions = [(difference_lst[i]/difference_abs_lst[i]) if difference_abs_lst[i] != 0 else 0 for i in range(len(difference_lst))]
        direction_values, direction_counts = np.unique(directions, return_counts=True)
        return difference_lst, difference_abs_lst, direction_values, direction_counts

safe_levels_with_dampener = 0
with open('inputs.txt', 'r') as f:
    for line in f.readlines():
        report = list(map(int, line.split()))
        for index_to_omit in range(len(report)):
            omitted_report = [x for i, x in enumerate(report) if i != index_to_omit]
            difference_lst, difference_abs_lst, direction_values, direction_counts = determine_difference_and_direction(omitted_report)
            valid_under_standard_conditions = (
                max(difference_abs_lst) < 4
                and min(difference_abs_lst) >= 1
                and (
                    all(level_diff > 0 for level_diff in difference_lst)
                    or all(level_diff < 0 for level_diff in difference_lst)
                )
            )
            if valid_under_standard_conditions:
                safe_levels_with_dampener += 1
                break

print("Day 2, Part 2 Answer:", str(safe_levels_with_dampener))
