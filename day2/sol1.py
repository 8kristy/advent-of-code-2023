import common

def is_round_possible(red, green, blue):
    return red <= 12 and green <= 13 and blue <= 14

sum_game_ids = 0

with open("input", 'r') as f:
    for line in f.readlines():
        game_id = int(line.split(":")[0].split(" ")[1])
        rounds = [x.split(",") for x in line.split(":")[1].split(";")]

        is_game_possible = True

        for round in rounds:
            round = [x.strip() for x in round]
            red, green, blue = common.get_cube_counts(round)
            if not is_round_possible(red, green, blue):
                is_game_possible = False

        if (is_game_possible):
            sum_game_ids += game_id

print(sum_game_ids)

        




