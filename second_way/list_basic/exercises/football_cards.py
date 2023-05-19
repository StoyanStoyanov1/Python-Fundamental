teams = {"A": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
         "B": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]}
red_cards = input().split()
for card in red_cards:
    team, number = card.split("-")
    if number in teams[team]:
        teams[team].remove(number)
        if len(teams[team]) < 7:
            break

print(f"Team A - {len(teams['A'])}; Team B - {len(teams['B'])}")
if len(teams["A"]) < 7 or len(teams["B"]) < 7:
    print("Game was terminated")
