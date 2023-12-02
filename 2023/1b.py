# alternate solution to day 1
# inspired by Johnathan Paulson on YouTube
import os

file_name = os.path.join(os.path.dirname(__file__), "1.txt")
with open(file_name, "r") as f:
    contents = f.read()
    p1_total, p2_total = 0, 0
    for line in contents.split("\n"):
        p1_digits, p2_digits = [], []
        for i,c in enumerate(line):
            if c.isdigit():
                p1_digits += c
                p2_digits += c
            for j, spelling in enumerate(['one', 'two','three','four','five','six','seven','eight','nine']):
                if line[i:].startswith(spelling):
                    p2_digits.append(str(j+1))
        p1_total += int(p1_digits[0] + p1_digits[-1])
        p2_total += int(p2_digits[0] + p2_digits[-1])

    print("part one:", p1_total)
    print("part two:", p2_total)