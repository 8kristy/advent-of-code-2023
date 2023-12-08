instructions = []
mappings = { }

with open("input", 'r') as f:
    instructions = list(f.readline().strip())
    f.readline()

    for line in f.readlines():
        origin = line.split("=")[0].strip()
        l, r = line.split("=")[1].strip().replace("(", "").replace(")", "").replace(", ", ",").split(",")
        mappings[origin] = (l, r)

current_node = "AAA"
instruction_index = 0
number_of_steps = 0

while current_node != "ZZZ":
    current_node = mappings[current_node][0 if instructions[instruction_index] == "L" else 1]
    number_of_steps += 1
    instruction_index = (instruction_index + 1) % len(instructions)

print(number_of_steps)