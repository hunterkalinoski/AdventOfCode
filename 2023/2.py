import os
import re

file_name = os.path.join(os.path.dirname(__file__), "2.txt")
with open(file_name, "r") as f:
    contents = f.read()
    p1 = 0
    p2 = 0
    for i,line in enumerate(contents.split("\n")):
        maxes = {"red": 0, "green": 0, "blue": 0}
        line = line[line.find(":")+1:]
        words = re.findall("\w+", line)
        for j in range(0, len(words), 2):
            w = words[j+1]
            maxes[w] = max(maxes[w], int(words[j]))
        if maxes['red'] <= 12 and maxes['green'] <= 13 and maxes['blue'] <= 14:
            p1 += i+1
        p2 += maxes['red'] * maxes['green'] * maxes['blue']
    print(p1)
    print(p2)