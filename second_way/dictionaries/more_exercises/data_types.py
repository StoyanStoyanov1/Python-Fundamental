def command_int(number):
    return int(number) * 2


def command_real(number):
    return f"{float(number) * 1.5:.2f}"


def command_string(text):
    return f"${text}$"


def data_types(first_current_command, second_current_command):
    if first_current_command == "int":
        return command_int(second_current_command)

    elif first_current_command == "real":
        return command_real(second_current_command)

    elif first_current_command == "string":
        return command_string(second_current_command)


first_command, second_command = input(), input()
print(data_types(first_command, second_command))