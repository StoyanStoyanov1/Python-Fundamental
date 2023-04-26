dwarfs = {}
colors = {}

while True:
    command = input().split(" <:> ")
    if command[0] == "Once upon a time":
        break

    name = f"({command[1]}) " + command[0]
    color = command[1]
    physics = int(command[2])

    if name not in dwarfs:
        dwarfs[name] = [physics, color]

        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1

    dwarfs[name][0] = max([dwarfs[name][0], physics])

sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True)
print(colors)
for dwarf, value in sorted_dwarfs:
    print(f"{dwarf} <-> {value[0]}")
