import re

number_of_cards = {}

with open("input", 'r') as f:        
    for line in f.readlines():
        card_id = int(re.sub(' +', ' ', line.split(":")[0]).split(" ")[1])

        if card_id not in number_of_cards:
            number_of_cards[card_id] = 1

        winning_numbers, card_numbers = [x.strip().replace("  ", " ").split(" ") for x in line.split(":")[1].split("|")]
        overlap = list(set(winning_numbers).intersection(set(card_numbers)))

        for i in range(card_id + 1, card_id + len(overlap) + 1):
            if i not in number_of_cards:
                number_of_cards[i] = 1
            number_of_cards[i] += number_of_cards[card_id]

print(sum(number_of_cards.values()))