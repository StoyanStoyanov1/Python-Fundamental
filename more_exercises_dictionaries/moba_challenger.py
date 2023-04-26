players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if " -> " in command:
        command = command.split(" -> ")

        player, position, skill = command[0], command[1], int(command[2])

        if player not in players:
            players[player] = {position: skill}
        elif position not in players[player]:
            players[player][position] = skill
        elif skill > players[player][position]:
            players[player][position] = skill

    else:
        first_player, second_player = command = command.split(" vs ")

        if (first_player and second_player) in players:
            for the_position in players[first_player]:
                if the_position in players[second_player]:
                    first_total_points = sum(players[first_player].values())
                    second_total_points = sum(players[second_player].values())
                    if first_total_points > second_total_points:
                        del players[second_player]
                    elif first_total_points < second_total_points:
                        del players[first_player]
                    break

best_player = {}

for name, position in players.items():
    best_player[name] = sum(position.values())


sorted_best_player = sorted(best_player.items(), key=lambda player: (-player[1], player[0]))

for player in sorted_best_player:
    skills = {}
    print(f"{player[0]}: {player[1]} skill")
    for skill in players[player[0]].items():
        skills[skill[0]] = skill[1]
    sorted_skills =sorted(skills.items(), key=lambda item: (-item[1], item[0]))
    for skill in sorted_skills:
        print(f'- {skill[0]} <::> {skill[1]}')

