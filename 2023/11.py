#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#  11       >24h   43482      0       >24h  41535      0

import os
import re
from collections import Counter, defaultdict
import math
import heapq

file_name = os.path.join(os.path.dirname(__file__), "11.txt")
# file_name = os.path.join(os.path.dirname(__file__), "11t.txt")


with open(file_name) as f:
    lines = f.read().strip().split("\n")

    # find all empty row locations
    empty_rows = []
    for i,line in enumerate(lines):
        empty = True
        for c in line:
            if c != ".":
                empty = False
        if empty:
            empty_rows.append(i)
    
    # find all empty col locations
    empty_cols = []
    for i in range(len(lines[0])):
        empty = True
        for j in range(len(lines)):
            if lines[j][i] != '.':
                empty = False
        if empty:
            empty_cols.append(i)

    # find all galaxy locations
    galaxies = []
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c != ".":
                galaxies.append((j,i))

    # find dists from galaxy i to all other galaxies j where j > i
    total_dist = 0
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            dist = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
            
            # for each empty row between the galaxies, increase dist by expansion amount (1 part 1, 999,999 part 2)
            a = min(galaxies[i][1], galaxies[j][1])
            b = max(galaxies[i][1], galaxies[j][1])
            for r in empty_rows:
                if a < r < b:
                    # dist += 1
                    dist += 999_999 # part 2
            
            # repeat for empty cols
            a = min(galaxies[i][0], galaxies[j][0])
            b = max(galaxies[i][0], galaxies[j][0])
            for c in empty_cols:
                if a < c < b:
                    # dist += 1
                    dist += 999_999 # part 2

            
            total_dist += dist

    print(total_dist)