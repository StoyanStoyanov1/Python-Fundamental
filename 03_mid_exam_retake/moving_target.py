def shoot(index, power):
    """we have targets from the number and if we get a "Shoot"
    command then on the given index (if it exists) we subtract the
    power and if the given index becomes 0 or less then we remove it from the sheet."""

    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)

    return targets


def add(index, value):
    """If the command is "Add" we insert a value of a given index. (if exists)
    If no such index exists, then we print "Invalid placement!"."""

    if index in range(len(targets)):
        targets.insert(index, value)
        return targets
    else:
        return print("Invalid placement!")


def strike(index, radius):
    """With a "Strike" command, we remove the given index and in the given radius before and after the given index.
     If any index does not exist then we print "Strike missed!"""

    if index in range(radius, len(targets) - radius):
        targets.pop(index + radius)
        targets.pop(index)
        targets.pop(index - radius)
        return targets
    else:
        return print("Strike missed!")


targets = list(map(int, input().split()))
command = input()

while command != "End":

    """With the "End" command, the program ends and we print out the final result!"""

    command = command.split()
    index = int(command[1])
    power_radius_value = int(command[2])

    if command[0] == "Shoot":
        shoot(index, power_radius_value)
    elif command[0] == "Add":
        add(index, power_radius_value)
    elif command[0] == "Strike":
        strike(index, power_radius_value)

    command = input()

targets = [str(target) for target in targets]
print("|".join(targets))
