#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#  10       >24h   50334      0       >24h  36254      0

import os
import re
from collections import Counter, defaultdict
import math
import heapq

file_name = os.path.join(os.path.dirname(__file__), "10.txt")
# file_name = os.path.join(os.path.dirname(__file__), "10t.txt")
# file_name = os.path.join(os.path.dirname(__file__), "10t2.txt")

right = (1, 0)
left = (-1, 0)
up = (0, -1)
down = (0, 1)

neighbor_map = {
    'F': [right, down],
    'L': [right, up],
    'J': [left, up],
    '7': [left, down],
    '|': [up, down],
    '-': [left, right],
    '.': [],
    # 'S': [right, down]  # replace with values for whatever is 'under' the S
    'S': [left, down]
}

with open(file_name) as f:
    lines = f.read().strip().split("\n")

    def getCharByPos(pos):
        return lines[pos[1]][pos[0]]
    
    def nextPos(prev, cur):
        dirs = neighbor_map[getCharByPos(cur)]
        neighbors = [(cur[0] + d[0], cur[1] + d[1]) for d in dirs]
        if prev in neighbors:
            neighbors.remove(prev)
        return neighbors[0]
    
    start = None
    for i, line in enumerate(lines):
        if start: break
        for j, c in enumerate(line):
            if c == 'S':
                start = (j, i)
                break
    
    prev = start
    cur = nextPos(prev, start)
    dist = 1
    path = [start]  # part 2
    while cur != start:
        path.append(cur)    # part 2
        tmp = cur
        cur = nextPos(prev, cur)
        prev = tmp
        dist += 1
    
    print(dist / 2)

    # shoelace formula to find area within the path
    area = 0
    n = len(path)
    for i in range(n):
        x1, y1 = path[i]
        x2, y2 = path[(i+1)%n]
        area += x2 * y1 - x1 * y2

    area = round((area/2) - n/2 + 1)
    print(area)
