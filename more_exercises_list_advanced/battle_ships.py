n = int(input())

ships = []

for ship in range(n):
    the_ship = list(map(int, input().split()))
    ships.append(the_ship)

attacks = list(map(str, input().split()))

destroyed = 0

for attack in attacks:
    the_attack = attack.split("-")
    row = int(the_attack[0])
    col = int(the_attack[1])
    ships[row][col] -= 1
    if ships[row][col] == 0:
        destroyed += 1

print(destroyed)


