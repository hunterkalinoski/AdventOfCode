#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   7   00:18:48     788      0   01:06:54   4395      0

# Spend like 40 minutes trying different things for part 2
# This solution is the first thing I tried.
# But, the first time,  I did chars['J'] == 0, instead of assigning it (one equal) on line 32
# I would've solved part 2 in like 00:21:00 if I typed it correctly, and saved 40 minutes and thousands of ranks.
# So infuriating

import os
import re

from collections import Counter

file_name = os.path.join(os.path.dirname(__file__), "7.txt")
file_name = os.path.join(os.path.dirname(__file__), "7t.txt")


def char_val(c):
    if c == 'A': return 99
    if c == 'K': return 88
    if c == 'Q': return 77
    # if c == 'J': return 66 # part 1
    if c == 'J': return 10  # part 2
    if c == 'T': return 55
    return 10 + int(c)

def hand_strength(hand: str):
    res = ""
    chars = Counter(hand)
    j = chars['J'] # part 2
    chars['J'] == 0 # part 2
    v = sorted(chars.values(), reverse=True)
    v[0] += j # part 2

    if v[0] == 5:
        res = "9"
    elif v[0] == 4:
        res = "8"
    elif v[0] == 3 and v[1] == 2:
        res = "7"
    elif v[0] == 3:
        res = "6"
    elif v[0] == 2 and v[1] == 2:
        res = "5"
    elif v[0] == 2:
        res = "4"
    else:
        res = "3"

    for i,c in enumerate(hand):
        res += str(char_val(c))
        
    return res


res = 0
with open(file_name, "r") as f:
    lines = f.read().strip().split('\n')
    hands = []
    for line in lines:
        d = line.strip().split()
        hands.append([d[0], d[1]])
    
    for hand in hands:
        hand.insert(0, hand_strength(hand[0]))

    hands = sorted(hands)

    for i, hand in enumerate(hands):
        res += int(hand[2]) * (i+1)
    print(res)