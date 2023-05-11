text = input()
command = input().split(":")
while command[0] != "Travel":

    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if index in range(len(text)):
            text = text[:index] + string + text[index:]

    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[:start_index] + text[end_index + 1:]

    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)
    command = input().split(":")


print(f"Ready for world tour! Planned stops: {text}")
