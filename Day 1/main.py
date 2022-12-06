from pathlib import Path
from operator import attrgetter

elf_list = []

class Elf:
    def __init__(self, foods: list):
        self.foods = foods
    
    def calculate_total_calories(self):
        total_calories = 0
        for food in self.foods:
            total_calories += food
        return total_calories
    
    total_calories = property(calculate_total_calories)


file_path = Path(__file__).with_name('names.txt')
with open(file_path) as puzzle_input:
    elf_data = []
    for line in puzzle_input:
        if line == "\n":
            elf_list.append(Elf(elf_data.copy()))
            elf_data.clear()
        else:
            elf_data.append(int(line.strip()))

elf_list.sort(key=attrgetter("total_calories"), reverse=True)
print(sum([elf.total_calories for elf in elf_list[:3]]))
max_calories = max(elf_list, key=attrgetter("total_calories")).total_calories
print(max_calories)







    