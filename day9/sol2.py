def get_next_number(sequence):
    if all([x == 0 for x in sequence]):
        return 0
    else:
        pairs = list(zip(sequence, sequence[1:]))
        diff_sequence = [x[1] - x[0] for x in pairs]
        return sequence[0] - get_next_number(diff_sequence)
    
sum = 0

with open("input", 'r') as f:
    for line in f.readlines():
        sequence = [int(x) for x in line.strip().split(" ")]
        sum += get_next_number(sequence)
        
print(sum)