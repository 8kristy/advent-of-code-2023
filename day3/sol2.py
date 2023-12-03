import re

schematic = []

with open("input", 'r+') as f:
    for line in f.readlines():
        schematic.append(line.strip())

def get_adjacent_numbers(line_index, gear_index):
    indexes = [(line_index - 1, gear_index - 1), (line_index - 1, gear_index), (line_index - 1, gear_index + 1), 
        (line_index, gear_index - 1), (line_index, gear_index + 1), 
        (line_index + 1, gear_index - 1), (line_index + 1, gear_index), (line_index + 1, gear_index + 1)]
    directions = [(schematic[index[0]][index[1]], index) for index in indexes if schematic[index[0]][index[1]] != "."]

    adjacent_numbers = []

    for direction in directions:
        numbers = [int(m.group(0)) for m in re.finditer(r'\d+', schematic[direction[1][0]]) if direction[1][1] >= m.start(0) and direction[1][1] <= m.end(0)]
        adjacent_numbers = adjacent_numbers + numbers

    return list(set(adjacent_numbers))

sum_of_gear_ratios = 0
        
for line_index, line in enumerate(schematic):
    gear_indexes = [i for i in range(len(line)) if line.startswith('*', i)]

    for gear_index in gear_indexes:
        adjacent_numbers = get_adjacent_numbers(line_index, gear_index)
        if len(adjacent_numbers) == 2:
            sum_of_gear_ratios += adjacent_numbers[0] * adjacent_numbers[1]

print(sum_of_gear_ratios)