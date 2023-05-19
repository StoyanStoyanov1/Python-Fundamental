def out_of_stock(gifts, gift):
    """Find the gifts with this name in your collection, if any, and change their values to "None"."""

    for index in range(len(gifts)):
        if gifts[index] == gift:
            gifts[index] = "None"


def required(gifts, gift, index):
    """If the index is valid, replace the gift on the given index with the given gift."""
    if index in range(len(gifts)):
        gifts[index] = gift


def just_in_case(gifts, gift):
    gifts[-1] = gift
    """Replace the value of your last gift with this one."""


def logic(gifts):
    while True:
        command = input()
        if command == "No Money":
            return ' '.join([item for item in gifts if item != "None"])

        command = command.split()

        if command[0] == "OutOfStock":
            gift = command[1]
            out_of_stock(gifts, gift)

        elif command[0] == "Required":
            gift, index = command[1], int(command[2])
            required(gifts, gift, index)

        elif command[0] == "JustInCase":
            gift = command[1]
            just_in_case(gifts, gift)


gifts = input().split()
print(logic(gifts))
