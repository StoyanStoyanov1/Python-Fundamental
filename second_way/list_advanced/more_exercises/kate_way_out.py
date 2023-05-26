def find_position(labyrinth):
    position = []
    for index in range(len(labyrinth)):
        for symbol in labyrinth[index]:
            if symbol == "k":
                position.append(index)
                position.append(labyrinth[index].find('k'))
                return position


def whitespace(labyrinth):
    whitespace_indexes = []

    for row_index in range(len(labyrinth)):
        for colum_index in range(len(labyrinth[row_index])):
            indexes = []
            if labyrinth[row_index][colum_index] == " ":
                indexes.append(row_index)
                indexes.append(colum_index)
                whitespace_indexes.insert(0, indexes)

    return whitespace_indexes


def find_away(labyrinth, position, indexes_whitespace):
    step = 0
    moves = 0

    while step < len(indexes_whitespace):
        x1 = indexes_whitespace[step][0]
        x2 = indexes_whitespace[step][1]
        temp = []
        temp.append(x1)
        temp.append(x2)

        if temp[0] == position[0] and position[1] - temp[1] == 1:
            position = temp
            moves += 1
            indexes_whitespace.pop(step)
            step = 0

        elif temp[0] == position[0] and temp[1] - position[1] == 1:
            position = temp
            moves += 1
            indexes_whitespace.pop(step)
            step = 0

        elif temp[0] - position[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            indexes_whitespace.pop(step)
            step = 0

        elif position[0] - temp[0] == 1 and position[1] == temp[1]:
            position = temp
            moves += 1
            indexes_whitespace.pop(step)
            step = 0

        else:
            step += 1

    if position[0] == 0 or position[0] == (len(labyrinth) - 1) or position[1] == 0 or position[1] == len(labyrinth[0]):
        return f"Kate got out in {moves + 1} moves"
    return f"Kate cannot get out"


count_rows = int(input())

moves = 0
free_space = True

labyrinth = []
for row in range(count_rows):
    labyrinth.append(input())

position = find_position(labyrinth)
indexes_whitespace = whitespace(labyrinth)
movement = find_away(labyrinth, position, indexes_whitespace)
print(movement)
