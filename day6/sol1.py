with open("input", 'r') as f:
    times = [int(x.strip()) for x in f.readline().split(":")[1].split(" ") if x != ""]
    record_distances = [int(x.strip()) for x in f.readline().split(":")[1].split(" ") if x != ""]

races = list(zip(times, record_distances))

product = 1

for time, record_distance in races:
    ways_to_win = 0
    for i in range(time):
        distnace = i * (time - i)
        if (distnace > record_distance):
            ways_to_win += 1
    product *= ways_to_win

print(product)


