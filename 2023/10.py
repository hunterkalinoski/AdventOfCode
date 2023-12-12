import os
import re
from collections import Counter, defaultdict
import math
import heapq

file_name = os.path.join(os.path.dirname(__file__), "10.txt")
# file_name = os.path.join(os.path.dirname(__file__), "10t.txt")

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
    while cur != start:
        tmp = cur
        cur = nextPos(prev, cur)
        prev = tmp
        dist += 1
    
    print(dist / 2)