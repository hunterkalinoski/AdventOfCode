#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   4   00:03:58     340      0   00:17:31   1678      0

import os
import re

file_name = os.path.join(os.path.dirname(__file__), "4.txt")
res = 0
copies = {}  #part2
with open(file_name, "r") as f:
    contents = f.read()
    lines = contents.split('\n')
    for i,line in enumerate(lines):
        line = line[line.find(':'):]
        parts = line.split("|")
        score = 0
        # print(parts[0])
        p1 = re.findall(r'\d+', parts[0])
        p2 = re.findall(r'\d+', parts[1])
        count = 0  #part2
        for num in p1:
            if num in p2:
                count += 1  #part2
                if score == 0:
                    score = 1
                else:
                    score *= 2
        copies[i] = copies.get(i, 0) + 1  #part2
        for j in range(1, count+1):  #part2
            copies[i+j] = copies.get(i+j, 0) + copies.get(i,0)  #part2
        res += score 
    print(res)
    # print(copies)
    s = 0  #part2
    for v in copies.values():  #part2
        s += v  #part2
    print(s)  #part2
