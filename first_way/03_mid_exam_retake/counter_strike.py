energy = int(input())
won_battle = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battle}. Energy left: {energy}")
        break

    if energy - int(command) < 0:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {energy} energy")
        break

    energy -= int(command)
    won_battle += 1

    if won_battle % 3 == 0:
        energy += won_battle
