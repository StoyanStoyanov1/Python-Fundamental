hidden_message = input()

numbers_list = [number for number in hidden_message if number.isdigit()]
non_numbers_list = [symbol for symbol in hidden_message if not symbol.isdigit()]

take_list = [int(numbers_list[index]) for index in range(0, len(numbers_list), 2)]
skip_list = [int(numbers_list[index]) for index in range(1, len(numbers_list), 2)]

taken_string = []
skipped_string = []
the_index = 0
remove_string = []
while the_index != len(take_list):

    for index in range(take_list[the_index]):
        if len(non_numbers_list) == 0:
            break
        symbol = non_numbers_list[index]
        taken_string.append(symbol)
        remove_string.append(symbol)

    for symbol in range(len(remove_string) - 1, -1, -1):
        if non_numbers_list[symbol] in remove_string:
            non_numbers_list.pop(symbol)
            remove_string.pop(symbol)

    for index in range(skip_list[the_index]):
        if len(non_numbers_list) == 0:
            break
        symbol = non_numbers_list[index]
        skipped_string.append(symbol)
        remove_string.append(symbol)

    for symbol in range(len(remove_string) - 1, -1, -1):
        if non_numbers_list[symbol] in remove_string:
            non_numbers_list.pop(symbol)
            remove_string.pop(symbol)

    the_index += 1
print(*taken_string, sep="")





