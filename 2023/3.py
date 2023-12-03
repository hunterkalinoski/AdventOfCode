#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   3   00:22:11    1809      0   00:33:33   1785      0

import os
import re

file_name = os.path.join(os.path.dirname(__file__), "3.txt")
total = 0
with open(file_name, "r") as f:
    contents = f.read()
    lines = contents.split('\n')
    for i,line in enumerate(lines):
        for num in re.finditer('\d+', line):
            for j in range(-1, 2):
                s,e = num.start(), num.end()
                for c in lines[max(0, min(i+j, len(lines)-1))][max(0,s-1):min(len(lines),e+1)]:
                    if c != '.' and not c.isdigit():
                        total += int(line[s:e])
                        break

print(total)

p2 = 0
with open(file_name, "r") as f:
    contents = f.read()
    lines = contents.split('\n')
    for i,line in enumerate(lines):
        for gear in re.finditer(r'\*', line):
            neighbors = []
            for j in range(-1, 2):
                index = gear.start()
                for num in re.finditer('\d+', lines[max(0, min(i+j, len(lines)-1))]):
                    if index >= num.start()-1 and index <= num.end():
                        num = lines[max(0, min(i+j, len(lines)-1))][num.start():num.end()]
                        neighbors.append(num)
            if len(neighbors) == 2:
                p2 += int(neighbors[0]) * int(neighbors[1])
print(p2)
    