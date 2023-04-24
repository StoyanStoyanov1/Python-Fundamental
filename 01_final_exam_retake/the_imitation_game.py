text = input()

move = lambda index: text[index:] + text[:index]
insert = lambda index, letter: text[:index] + letter + text[index:]
change_all = lambda substring, replacement: text.replace(substring, replacement)

while True:
    command = input().split("|")
    if command[0] == "Decode":
        print(f"The decrypted message is: {text}")
        break

    elif command[0] == "Move":
        index = int(command[1])
        text = move(index)
    elif command[0] == "Insert":
        index, letter = int(command[1]), command[2]
        text = insert(index, letter)
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        text = change_all(substring, replacement)
