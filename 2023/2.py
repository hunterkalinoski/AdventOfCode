import os
import re

file_name = os.path.join(os.path.dirname(__file__), "2.txt")
with open(file_name, "r") as f:
    contents = f.read()
    p1, p2 = 0, 0
    for i,line in enumerate(contents.split("\n")):
        maxes = {"r": 0, "g": 0, "b": 0}
        for num, c in re.findall(r'(\d+) (\w)', line):
            maxes[c] = max(maxes[c], int(num))
        if maxes['r'] <= 12 and maxes['g'] <= 13 and maxes['b'] <= 14:
            p1 += i+1
        p2 += maxes['r'] * maxes['g'] * maxes['b']
    print(p1)
    print(p2)