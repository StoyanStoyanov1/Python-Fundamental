def all_dragons(n):
    the_dragons = {}
    for _ in range(n):
        command = input().split()
        the_type, name = command[0], command[1]

        damage = int(command[2].replace("null", "45"))
        health = int(command[3].replace("null", "250"))
        armor = int(command[4].replace("null", "10"))

        if the_type not in the_dragons:
            the_dragons[the_type] = {name: [damage, health, armor]}
        else:
            the_dragons[the_type][name] = [damage, health, armor]

    return the_dragons


def sorted_dragons(dragons):
    for color, dragon in dragons.items():
        damage = [value[1][0] for value in dragon.items()]
        average_damage = sum(damage) / len(damage)
        health = [value[1][1] for value in dragon.items()]
        average_health = sum(health) / len(health)
        armor = [value[1][2] for value in dragon.items()]
        average_armor = sum(armor) / len(armor)
        print(f"{color}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

        for name, value in sorted(dragon.items()):
            print(f"-{name} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}")

n = int(input())
dragons = all_dragons(n)
sorted_dragons(dragons)
