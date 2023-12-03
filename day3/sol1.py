import re

def is_special_character(character):
    return not character.isnumeric() and character != "."

schematic = []

with open("input", 'r+') as f:
    for line in f.readlines():
        schematic.append(line.strip())

sum_of_parts = 0
        
for line_index, line in enumerate(schematic):
    numbers = list(dict.fromkeys(re.findall(r'\d+', line)))

    for number in numbers:
        has_symbol_adjacent = False
        starting_indexes = [m.start() + 1 for m in re.finditer(r'(^|\D)' + re.escape(number) + r'($|\D)', line)]

        for starting_index in starting_indexes:

            # Left and right of number
            if ((starting_index > 0 and is_special_character(line[starting_index - 1]))
                or (starting_index + len(number) < len(line) and is_special_character(line[starting_index + len(number)]))):
                has_symbol_adjacent = True

            # Above and below of number + diagonals
            for i in range(starting_index - 1, starting_index + len(number) + 1):                
                if ((line_index > 0 and i < len(line) and is_special_character(schematic[line_index - 1][i])) 
                    or (line_index < len(schematic) - 1 and i < len(line) and is_special_character(schematic[line_index + 1][i]))):
                    has_symbol_adjacent = True

            if has_symbol_adjacent:
                sum_of_parts += int(number)

print(sum_of_parts)



