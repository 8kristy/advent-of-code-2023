seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

with open("input", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    map_index = 0
    line_index = 1
    while line_index < len(lines):
        line_index += 2
        while line_index < len(lines) and lines[line_index] != "":
            maps[map_index].append([int(x) for x in lines[line_index].split(" ")])
            line_index += 1
        map_index += 1

for i in range(len(seeds)):
    for mapping in maps:
        for range in mapping:
            seed = seeds[i]
            if seed >= range[1] and seed <= range[1] + range[2]:
                diff = seed - range[1]
                seeds[i] = range[0] + diff
                break

print(min(seeds))

