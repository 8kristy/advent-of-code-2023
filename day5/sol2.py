import math
import sys

seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

maps = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

min_location = sys.maxsize
min_seed_number_start = 0
min_seed_number_end = 0

def get_min_location(seed_range):
    global min_location, min_seed_number_start, min_seed_number_end
    for seed in seed_range:
        original_value = seed
        for mapping in maps:
            for map_range in mapping:
                if seed >= map_range[1] and seed <= map_range[1] + map_range[2]:
                    diff = seed - map_range[1]
                    mapped_value = map_range[0] + diff
                    seed = mapped_value
                    break
        if (seed < min_location):
            min_location = seed
            min_seed_number_start = original_value - math.sqrt(y)
            min_seed_number_end = original_value + math.sqrt(y)

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

pairs = list(zip(seeds, seeds[1:]))
del pairs[1::2]
for x, y in pairs:
    get_min_location(range(x, x + y, int(math.sqrt(y))))

get_min_location(range(int(min_seed_number_start), int(min_seed_number_end)))

print(min_location)
