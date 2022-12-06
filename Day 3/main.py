from pathlib import Path

def convert_character_to_value(char: str):
    if char.islower(): return ord(char) - 96
    if char.isupper(): return ord(char) - 38

def main_part_1():
    result_total = 0
    file_path = Path(__file__).with_name("input.txt")
    with open(file_path) as f:
        for line in f:
            formated_line = line.strip()
            compartment_one, compartment_two = set(formated_line[:int(len(formated_line) / 2)]), set(formated_line[int(len(formated_line) / 2):])
            duplicate = "".join(compartment_one.intersection(compartment_two))
            result_total += convert_character_to_value(duplicate)
    print(f"The anwser to part 1 is: {result_total}")


def main_part_2():
    result_total = 0
    file_path = Path(__file__).with_name("input.txt")
    current_group = ""
    with open(file_path) as f:
        count = 1
        for line in f:
            current_group += line
            if count == 3:
                compartment_one, compartment_two, compartment_three = current_group.rstrip().split("\n")
                duplicates = "".join(set(compartment_one).intersection(set(compartment_two), set(compartment_three)))
                result_total += convert_character_to_value(duplicates)
                count = 0
                current_group = ""
            count+= 1
        print(f"The anwser to part 2 is: {result_total}")

main_part_1()
main_part_2()



