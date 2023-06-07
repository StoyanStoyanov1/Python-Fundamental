import re
names = input().split(', ')

players = {}
while True:
    text = input()
    if text == "end of race":
        break
    found_name = ''.join(re.findall(r"[A-Za-z]", text))
    fount_distance = sum([int(digit) for digit in re.findall(r"\d", text)])
    if found_name in names:
        if found_name not in players:
            players[found_name] = fount_distance
        else:
            players[found_name] += fount_distance

wins_players = [player for player in dict(sorted(players.items(), key=lambda player: player[1], reverse=True)).keys()]

print(f"1st place: {wins_players[0]}\n2nd place: {wins_players[1]}\n3rd place: {wins_players[2]}")



