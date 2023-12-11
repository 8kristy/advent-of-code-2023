pipes = []
distances = []

with open("input", 'r') as f:
    pipes = [list(x.strip()) for x in f.readlines()]

distances = [[0 for x in range(len(pipes[0]))] for y in range(len(pipes))]
visited = [[False for x in range(len(pipes[0]))] for y in range(len(pipes))]
connections = [[None for x in range(len(pipes[0]))] for y in range(len(pipes))]

for i, row in enumerate(pipes):
    for j, pipe in enumerate(row):
        up = i - 1 if i - 1 >= 0 else None
        down = i + 1 if i + 1 < len(pipes) else None
        left = j - 1 if j - 1 >= 0 else None
        right = j + 1 if j + 1 < len(pipes[0]) else None
        if pipe == "|":
            connections[i][j] = [(up, j), (down, j)]
        if pipe == "-":
            connections[i][j] = [(i, left), (i, right)]
        if pipe == "L":
            connections[i][j] = [(up, j), (i, right)]
        if pipe == "J":
            connections[i][j] = [(up, j), (i, left)]
        if pipe == "7":
            connections[i][j] = [(i, left), (down, j)]
        if pipe == "F":
            connections[i][j] = [(i, right), (down, j)]

start_position = None
for index, lst in enumerate(pipes):
    if "S" in lst:
        start_position = (index, lst.index("S"))

def get_distances(node, distance):
    global distances

    if visited[node[0]][node[1]] or node == None or None in node:
        return
    
    visited[node[0]][node[1]] = True
    distances[node[0]][node[1]] = distance if distance > distances[node[0]][node[1]] else distances[node[0]][node[1]]

    i = node[0]
    j = node[1]
    if (i > 0 and connections[i - 1][j] != None and node in connections[i - 1][j]):
        if (node == start_position):
            distances = [[0 for x in range(len(pipes[0]))] for y in range(len(pipes))]
        get_distances((i - 1, j), distance + 1)
    if (i < len(pipes) - 1 and connections[i + 1][j] != None and node in connections[i + 1][j]):
        if (node == start_position):
            distances = [[0 for x in range(len(pipes[0]))] for y in range(len(pipes))]
        get_distances((i + 1, j), distance + 1)
    if (j > 0 and connections[i][j - 1] != None and node in connections[i][j - 1]):
        if (node == start_position):
            distances = [[0 for x in range(len(pipes[0]))] for y in range(len(pipes))]
        get_distances((i, j - 1), distance + 1)
    if (j < len(pipes[0]) - 1 and connections[i][j + 1] != None and node in connections[i][j + 1]):
        if (node == start_position):
            distances = [[0 for x in range(len(pipes[0]))] for y in range(len(pipes))]
        get_distances((i, j + 1), distance + 1)
    return

get_distances(start_position, 0)

for row in distances:
    print(row)