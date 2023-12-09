#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   9   00:09:44    1174      0   00:14:34   1410      0

import os
import re
from collections import Counter, defaultdict
import math

file_name = os.path.join(os.path.dirname(__file__), "9.txt")
# file_name = os.path.join(os.path.dirname(__file__), "9t.txt")

def is_all_zeros(li):
    for l in li:
        if l != 0:
            return False
    return True

with open(file_name, "r") as f:
    lines = f.read().strip().split('\n')

    total_levels = []
    for line in lines:
        nums = list(map(int, line.split(' ')))

        levels = []

        levels.append(nums)
        while not is_all_zeros(levels[-1]):
            new_level = []
            nums = levels[-1]
            prev = nums[0]
            for i in range(1, len(nums)):
                new_level.append(nums[i] - prev)
                prev = nums[i]
            
            levels.append(new_level)
        
        total_levels.append(levels)

    res = 0 
    for level in total_levels:
        r = 0
        for sub in level:
            r += sub[-1]
        res += r

    print(res)

    p2 = 0
    for level in total_levels:
        r = 0
        for i in range(len(level) - 2, -1, -1):
            r = level[i][0] - r

        p2 += r
        
    print(p2)