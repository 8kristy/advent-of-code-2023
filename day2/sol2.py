def get_cube_counts(round):
    red = 0
    green = 0
    blue = 0
        
    for cubes in round:
        amount = int(cubes.split(" ")[0])
        colour = cubes.split(" ")[1]

        if colour == "red":
            red += amount
        elif colour == "green":
            green += amount
        else:
            blue += amount

    return red, green, blue

sum_of_powers = 0

with open("input", 'r') as f:
    for line in f.readlines():
        game_id = int(line.split(":")[0].split(" ")[1])
        rounds = [x.split(",") for x in line.split(":")[1].split(";")]

        min_red = 0
        min_green = 0
        min_blue = 0

        for round in rounds:
            round = [x.strip() for x in round]
            red, green, blue = get_cube_counts(round)
            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)

        sum_of_powers += min_red * min_green * min_blue

print(sum_of_powers)