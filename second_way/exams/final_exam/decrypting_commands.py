def replace(current_text, current_char, new_char):
    current_text = current_text.replace(current_char, new_char)
    print(current_text)
    return current_text


def cut(current_text, start_index, end_index):
    if start_index in range(len(current_text)) and end_index in range(len(current_text)):
        current_text = current_text[:start_index] + current_text[end_index + 1:]
        print(current_text)
    else:
        print("Invalid indices!")

    return current_text


def make(current_text, upper_lower):
    if upper_lower == "Upper":
        current_text = current_text.upper()
    else:
        current_text = current_text.lower()

    print(current_text)
    return current_text


def check(current_text, string):
    if string in current_text:
        print(f"Message contains {string}")
    else:
        print(f"Message doesn't contain {string}")


def sum(current_text, start_index, end_index):
    if start_index in range(len(current_text)) and end_index in range(len(current_text)):
        total_sum = 0
        for symbol in current_text[start_index:end_index + 1]:
            total_sum += ord(symbol)

        print(total_sum)

    else:
        print("Invalid indices!")


text = input()

while True:
    command = input()

    if command == "Finish":
        break

    current_command, *data = command.split()

    if current_command == "Replace":
        current_char, new_char = data
        text = replace(text, current_char, new_char)

    elif current_command == "Cut":
        start_index, end_index = int(data[0]), int(data[1])
        text = cut(text, start_index, end_index)

    elif current_command == "Make":
        upper_lower = data[0]
        text = make(text, upper_lower)

    elif current_command == "Check":
        string = data[0]
        check(text, string)

    elif current_command == "Sum":
        start_index, end_index = int(data[0]), int(data[1])
        sum(text, start_index, end_index)
