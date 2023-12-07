import functools


cards = []

def process_hand(hand):
    mappings = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return [mappings[x] if x in mappings.keys() else int(x) for x in list(hand)]    

def get_ranking(hand):
    minimised_length = len(list(set(hand)))
    if minimised_length == 1:
        return 7
    elif minimised_length == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            return 6
        else:
            return 5
    elif minimised_length == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            return 4
        else:
            return 3
    elif minimised_length == 4:
        return 2
    else:
        return 1    
    
def compare_hands(hand1, hand2):
    ranking1 = get_ranking(hand1[0])
    ranking2 = get_ranking(hand2[0])
    if ranking1 > ranking2:
        return 1
    if ranking1 < ranking2:
        return -1
    if ranking1 == ranking2:
        for x, y in zip(hand1[0], hand2[0]):
            if x > y:
                return 1
            elif x < y:
                return -1
    return 0

with open("input", 'r') as f:
    for line in f.readlines():
        hand = line.split(" ")[0]
        bid = int(line.split(" ")[1])
        hand = process_hand(hand)
        cards.append((hand, bid))

cards = sorted(cards, key=functools.cmp_to_key(compare_hands))

sum = 0
winnings = [(i + 1, x[1]) for i, x in enumerate(cards)]
for x in winnings:
    sum += x[0] * x[1]

print(sum)
