from itertools import cycle
from math import lcm

instructions = []
mappings = { }

with open("input", 'r') as f:
    instructions = list(f.readline().strip())
    f.readline()

    for line in f.readlines():
        origin = line.split("=")[0].strip()
        l, r = line.split("=")[1].strip().replace("(", "").replace(")", "").replace(", ", ",").split(",")
        mappings[origin] = (l, r)

nodes = [x for x in mappings.keys() if x[2] == "A"]
totals = [0] * len(nodes)

for i, pos in enumerate(nodes):
    c = cycle(int(d == 'R') for d in instructions)
    while not pos.endswith('Z'):
        totals[i] += 1
        pos = mappings[pos][next(c)]

print(lcm(*totals))
