#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   6   00:12:43    3984      0   00:18:08   3924      0

import os
import re

file_name = os.path.join(os.path.dirname(__file__), "6t.txt")
file_name = os.path.join(os.path.dirname(__file__), "6.txt")

res = 1
with open(file_name, "r") as f:
    lines = f.read().strip().split('\n')
    t = list(map(int, re.findall('\d+', lines[0])))
    d = list(map(int, re.findall('\d+', lines[1])))

    for i, time in enumerate(t):
        distances = [0] * (time + 1)
        for j in range(time+1):
            distances[j] = j * (time - j)

        cnt = 0
        for dist in distances:
            if dist > d[i]:
                cnt += 1
        
        if cnt != 0:
            res *= cnt
    print(res)

    p2t = int("".join(re.findall(r'\d+', lines[0])))
    p2d = int("".join(re.findall(r'\d+', lines[1])))
    
    distances = [0] * (p2t + 1)
    for j in range(p2t+1):
        distances[j] = j * (p2t - j)

    cnt = 0
    for dist in distances:
        if dist > p2d:
            cnt += 1
    print(cnt)

