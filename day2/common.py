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