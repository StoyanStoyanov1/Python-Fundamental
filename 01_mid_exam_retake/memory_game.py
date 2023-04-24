elements = input().split()
command = input().split()
turns = 0
won = False

while command[0] != "end":
    turns += 1
    first_index = int(command[0])
    second_index = int(command[1])

    if first_index not in range(len(elements)) or second_index \
            not in range(len(elements)) or first_index == second_index:
        elements.insert(int(len(elements)/ 2), f"-{turns}a")
        elements.insert(int(len(elements) / 2), f"-{turns}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        found_element = elements[first_index]
        elements.remove(found_element), elements.remove(found_element)
        print(f"Congrats! You have found matching elements - {found_element}!")

    else:
        print(f"Try again!")

    if len(elements) == 0:
        won = True
        print(f'You have won in {turns} turns!')
        break

    command = input().split()

if not won:
    print(f'Sorry you lose :(\n{" ".join(elements)}')