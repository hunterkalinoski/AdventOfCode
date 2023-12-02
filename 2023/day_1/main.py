import os

# read a file and return each line, with newline stripped
def extract_lines_from_file(path: str) -> list[str]:
    file_name = os.path.join(os.path.dirname(__file__), path)
    lines = []
    with open(file_name) as f:
        lines = [line.rstrip('\n') for line in f]
        f.close()
    return lines


# find the earliest occurrence of an item from items in line, and return that item
def find_earliest_occurrence(line: str, items: list) -> str:
    earliest_index = float('inf')
    earliest_val = ""
    for item in items:
        i = line.find(item)
        if i != -1 and i < earliest_index:
            earliest_index = i
            earliest_val = item
    return earliest_val


# get the leftmost and rightmost digits and return a concatenated int
def get_calibration_value(line: str, accept_num_spellings = False) -> int:
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spellings = {
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine' :'9'
    }
    if accept_num_spellings:
        items.extend(spellings.keys())
    
    lVal = find_earliest_occurrence(line, items)
    # search string backwards, with spellings backwards, to find last occurrence
    rVal = find_earliest_occurrence(line[::-1], [item[::-1] for item in items])
    rVal = rVal[::-1] # make sure to un-reverse the found spelling

    # convert spelling to numeric string (eg. 'one' to '1')
    if lVal in spellings:
        lVal = spellings[lVal]
    if rVal in spellings:
        rVal = spellings[rVal]

    # concat numeric strings and cast to int
    return int(lVal + rVal)


def part_one(path: str) -> int:
    lines = extract_lines_from_file(path)
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total


def part_two(path: str) -> int:
    lines = extract_lines_from_file(path)
    total = 0
    for line in lines:
        total += get_calibration_value(line, accept_num_spellings = True)
    return total


if __name__ == "__main__":
    # print("part one test:", part_one("test_input.txt"))
    # print("part two test:", part_two("test_input2.txt"))

    print("part one:", part_one("input.txt"))
    print("part two:", part_two("input.txt"))
