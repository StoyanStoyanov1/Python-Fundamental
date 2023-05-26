def battle_ship():
    ships = [list(map(int, input().split())) for _ in range(int(input()))]
    attacks = [attack.split("-") for attack in input().split()]

    destroyed = 0

    for attack in attacks:
        row, column = int(attack[0]), int(attack[1])
        if ships[row][column] > 0:
            ships[row][column] -= 1
            if ships[row][column] == 0:
                destroyed += 1

    return destroyed


print(battle_ship())
