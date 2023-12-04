cards_worth = 0

with open("input", 'r') as f:
    for line in f.readlines():
        winning_numbers, card_numbers = [x.strip().replace("  ", " ").split(" ") for x in line.split(":")[1].split("|")]
        overlap = list(set(winning_numbers).intersection(set(card_numbers)))
        if (len(overlap) == 1):
            cards_worth += 1
        elif(len(overlap) > 1):
            cards_worth += 2 ** (len(overlap) - 1)

print(cards_worth)