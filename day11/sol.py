from itertools import combinations

def get_expansion_indexes(arr):
    indexes = []
    for i, row in enumerate(arr):
        if all([x == "." for x in row]):
            indexes.append(i)
    return indexes

def get_sum(multiplier, pairs, expansion_row_indexes, expansion_col_indexes):
    sum = 0

    for g1, g2 in pairs:
        expansions_x = [x for x in expansion_row_indexes if (x < g1[0] and x > g2[0]) or (x > g1[0] and x < g2[0])]
        expansions_y = [x for x in expansion_col_indexes if (x < g1[1] and x > g2[1]) or (x > g1[1] and x < g2[1])]
        sum += (abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]) + len(expansions_x) * (multiplier - 1) + len(expansions_y) * (multiplier - 1))

    return sum

with open("input", 'r') as f:
    galaxy = [list(x.strip()) for x in f.readlines()]

expansion_row_indexes = get_expansion_indexes(galaxy)
expansion_col_indexes = get_expansion_indexes([list(i) for i in zip(*galaxy)])

positions = []

for i, row in enumerate(galaxy):
    for j, column in enumerate(row):
        if column == "#":
            positions.append((i, j))

pairs = list(combinations(positions, 2))

print("Part 1:", get_sum(2, pairs, expansion_row_indexes, expansion_col_indexes))
print("Part 2:", get_sum(1000000, pairs, expansion_row_indexes, expansion_col_indexes))