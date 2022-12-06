from pathlib import Path
import re

def get_puzzle_input():
    file_path = Path(__file__).with_name("input.txt")
    with open(file_path) as f:
        return f.readlines()

# Generates the stack table and instructions 
def build_tables(puzzle):
    number_of_headers = int(len(puzzle[0]) / 4)
    crates = {}
    instructions = []

    # Create headers for the crates
    for i in range(1, number_of_headers + 1):
        crates[i] = list()

    # Generates starting stack layout
    for line in puzzle:
        # Each stack occurs every 4 characters
        data = line[1::4]
        for i in range(0, len(data)):
            # Stacks only use uppercase letters
            if data[i].isupper():
                crates[i + 1].insert(0, data[i])
        # Generates moving instructions
        # Can't figure out regex, had to leave words in. [1] is amount [3] is from [5] is to
        if line[0] == "m":
            instructions.append(re.sub("^[ 0-9]+$", "", line).strip().split(" "))
    return (crates, instructions)

if __name__ == "__main__":
    puzzle = get_puzzle_input()
    crates, instructions = build_tables(puzzle)
    result = ""

    # 1 is amount, 3 is initial location, 5 is final location
    for instruction in instructions:
        items_to_move = crates[int(instruction[3])][-int(instruction[1]):]

        # Remove reverse to solve part 2
        items_to_move.reverse()
        del crates[int(instruction[3])][-int(instruction[1]):]
        for item in items_to_move:
            crates[int(instruction[5])].append(item)

    for key in crates:
        result += str(crates[key][-1])
    print(result)

