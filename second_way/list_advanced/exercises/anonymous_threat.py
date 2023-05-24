def merge(current_text, start_index, end_index):
    start, end = start_index, end_index
    new_text = []

    if start_index < 0:
        start = 0

    if end_index >= len(current_text):
        end = len(current_text) - 1
    new_words = ""

    for index, word in enumerate(current_text):
        if index in range(start, end + 1):
            new_words += word
            if index == len(current_text) - 1:
                new_text.append(new_words)
        else:
            if new_words:
                new_text.append(new_words)
                new_words = ""

            new_text.append(word)

    if new_text:
        return new_text
    else:
        return current_text


def divide(current_text, current_index, partitions):
    new_text = []

    for index, word in enumerate(current_text):
        if current_index != index:
            new_text.append(word)
        else:
            if partitions > len(word):
                step = 1
            else:
                step = len(word) // partitions
            start = 0

            for parts in range(partitions):
                if parts == partitions - 1:
                    new_text.append(word[start:])
                    break
                else:
                    new_text.append(word[start: start + step])
                start += step

    return new_text


def anonymous_threat():
    text = input().split()
    while True:
        command = input().split()
        if command[0] == "3:1":
            return " ".join(text)

        the_command, first_number, second_number = command[0], int(command[1]), int(command[2])

        if the_command == "merge":
            text = merge(text, first_number, second_number)

        elif the_command == "divide":
            text = divide(text, first_number, second_number)


print(anonymous_threat())
