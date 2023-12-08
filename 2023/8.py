#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   8   00:11:16    2792      0   00:26:00   1277      0


# Would have taken like 2 minutes off part 1 if I realized it started at 'AAA' instead of the first src thing...
# I tried brute force for part 2, and realized it wasn't working
# I had no clue how else to do it, so I went to reddit, and saw LCM suggested
# So, I made a list of all the times and LCM'd it in some online calculator, which worked


import os
import re
from collections import Counter, defaultdict
import math

file_name = os.path.join(os.path.dirname(__file__), "8.txt")
# file_name = os.path.join(os.path.dirname(__file__), "8t.txt")

# steps = 0
# with open(file_name, "r") as f:
#     lines = f.read().strip().split('\n')
#     hands = []
#     dirs = lines[0]

#     graph = {}

#     # build graph
#     for line in lines[2:]:
#         data = line.split()
#         src = data[0]
#         dest_l = data[2][1:-1]
#         dest_r = data[3][:-1]

#         graph[src] = (dest_l, dest_r)

#     start = 'AAA'

#     pos = 0
#     count = 0
#     while start != "ZZZ":
#         t = 0 if dirs[pos] == 'L' else 1
#         start = graph[start][t]
#         pos += 1
#         if pos == len(dirs):
#             pos = 0
#         count += 1
    
#     print(count)


steps = 0
with open(file_name, "r") as f:
    lines = f.read().strip().split('\n')
    hands = []
    dirs = lines[0]

    graph = {}

    # build graph
    for line in lines[2:]:
        data = line.split()
        src = data[0]
        dest_l = data[2][1:-1]
        dest_r = data[3][:-1]

        graph[src] = (dest_l, dest_r)
    
    starts = []
    for k in graph.keys():
        if k.endswith('A'):
            starts.append(k)


    times = []
    for start in starts:
        pos = 0
        count = 0
        while not start.endswith('Z'):
            t = 0 if dirs[pos] == 'L' else 1
            start = graph[start][t]
            pos += 1
            if pos == len(dirs):
                pos = 0
            count += 1
        times.append(count)
    print(times)
    print(math.lcm(*times))

    # while True:
    #     done = True
    #     for start in starts:
    #         if not start.endswith('Z'):
    #             done = False
    #             continue
    #     if done: break
    #     for i,start in enumerate(starts):
    #         t = 0 if dirs[pos] == 'L' else 1
    #         starts[i] = graph[start][t]


    #     pos += 1
    #     if pos == len(dirs):
    #         pos = 0
    #     count += 1
    
    # print(count)
