with open("input", 'r') as f:
    time = int(f.readline().split(":")[1].replace(" ", ""))
    record_distance = int(f.readline().split(":")[1].replace(" ", ""))

start = 0
for i in range(time):
    distnace = i * (time - i)
    if (distnace > record_distance):
        start = i
        break

print(time - 2 * start + 1)