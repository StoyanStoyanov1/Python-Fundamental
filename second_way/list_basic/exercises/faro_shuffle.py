cards = input().split()
count_if_shuffles = int(input())

half_deck = len(cards) // 2

for _ in range(count_if_shuffles):
    shuffles_deck = []
    for card in range(half_deck):
        first_deck = cards[:half_deck]
        second_deck = cards[half_deck:]
        shuffles_deck.append(first_deck[card])
        shuffles_deck.append(second_deck[card])
    cards = shuffles_deck
print(cards)
