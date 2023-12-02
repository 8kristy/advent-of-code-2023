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

def is_round_possible(red, green, blue):
    red_cubes = 12
    green_cubes = 13 
    blue_cubes = 14

    return red <= red_cubes and green <= green_cubes and blue <= blue_cubes

sum_game_ids = 0

with open("input", 'r') as f:
    for line in f.readlines():
        game_id = int(line.split(":")[0].split(" ")[1])
        rounds = [x.split(",") for x in line.split(":")[1].split(";")]

        is_game_possible = True

        for round in rounds:
            round = [x.strip() for x in round]
            red, green, blue = get_cube_counts(round)
            if not is_round_possible(red, green, blue):
                is_game_possible = False

        if (is_game_possible):
            sum_game_ids += game_id

print(sum_game_ids)

        




