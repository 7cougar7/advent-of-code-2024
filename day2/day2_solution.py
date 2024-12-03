import numpy as np

## Part 1 Solutions ##
safe_levels = 0
with open('inputs.txt', 'r') as f:
    for line in f.readlines():
        report = list(map(int, line.split()))
        report_incr = sorted(report)
        report_desc = sorted(report, reverse=True)
        difference_lst = [abs(report[i+1] - report[i]) for i in range(len(report)-1)]
        # print(
        #     difference_lst, 
        #     max(difference_lst), 
        #     report == report_incr, 
        #     report == report_desc
        # )
        if max(difference_lst) < 4 and min(difference_lst) >= 1 and(
            report == report_incr or report == report_desc
        ):
             safe_levels += 1

print("Day 2, Part 1 Answer: " + str(safe_levels))
