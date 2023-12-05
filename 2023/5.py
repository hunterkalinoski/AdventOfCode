#       --------Part 1---------   --------Part 2--------
# Day       Time    Rank  Score       Time   Rank  Score
#   5   00:23:11    1841      0          -      -      -

# Could not get part 2 working :(
# The test input works, but not the actual input
# I don't know what is going wrong

import os
import re

# file_name = os.path.join(os.path.dirname(__file__), "5t.txt")
file_name = os.path.join(os.path.dirname(__file__), "5.txt")
res = 0
with open(file_name, "r") as f:
    contents = f.read()
    lines = contents.split(':')
    seeds = re.findall('\d+', lines[1])
    seeds = list(map(int, seeds))

    # part 2
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i],seeds[i+1]))
    
    for i in range(2, len(lines)):
        new_seeds = [-1] * len(seeds)
        for data in re.findall(r'(\d+) (\d+) (\d+)', lines[i]):
            dest, src, rng = int(data[0]), int(data[1]), int(data[2])
            for j,seed in enumerate(seeds):
                if seed >= src and seed < (src + rng):
                    new_seeds[j] = dest + (seeds[j] - src)
        
        for j,n in enumerate(new_seeds):
            if n == -1:
                new_seeds[j] = seeds[j]
        
        seeds = new_seeds

        # START part2 region
        new_seed_ranges = []
        unused_ranges = seed_ranges.copy()
        for data in re.findall(r'(\d+) (\d+) (\d+)', lines[i]):
            dest, src, rng = int(data[0]), int(data[1]), int(data[2])
            for j, sd_data in enumerate(seed_ranges):
                sd_start, sd_range = sd_data[0], sd_data[1]
                sd_end = sd_start + sd_range - 1

                # if sd_start is within the current looking at data range
                if src <= sd_start < src+rng:
                    dif = sd_start - src
                    remaining_rng = rng - dif

                    # case seed range is entirely within the found data range
                    if sd_range <= remaining_rng:
                        new_seed_ranges.append((dest+dif, sd_range))
                        seed_ranges[j] = [-1,0]
                    
                    # case seed range starts in data range, but get cut off
                    else:
                        new_seed_ranges.append((dest+dif, remaining_rng))
                        seed_ranges[j] = ((src+rng, sd_range - remaining_rng))

                # if sd_end within the data range, but sd_start not
                elif src <= sd_end < src+rng:
                    new_sd_rng = sd_end - src + 1
                    new_seed_ranges.append((dest, new_sd_rng))
                    
                    seed_ranges[j] = ((sd_start, sd_range - new_sd_rng))
                
                # if data range inside seed range
                elif sd_start < src and sd_end > src+rng:
                    seed_ranges[j] = ((sd_start, rng))
                    new_seed_ranges.append((dest, rng))
                    seed_ranges.insert(j+1, (src+rng, sd_range - rng - (src-sd_start)))

        # seed_ranges that did not match anything (value should persist)
        for sd_start, sd_range in seed_ranges:
            if sd_start != -1:
                new_seed_ranges.append((sd_start, sd_range))
        seed_ranges = new_seed_ranges
        # print(seed_ranges)
        # END part2 region


    
    print(min(seeds))

    # part 2
    sd_ranges_min = float('inf')
    for d in seed_ranges:
        sd_ranges_min = min(sd_ranges_min, d[0])
    print(sd_ranges_min)
