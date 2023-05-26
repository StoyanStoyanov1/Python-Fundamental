def take_or_skip(text):
    numbers_list = [digit for digit in text if digit.isdigit()]
    non_numbers = [symbol for symbol in text if not symbol.isdigit()]
    result = []

    for index, digit in enumerate(numbers_list):
        if index % 2 == 0:
            if int(digit) != 0:
                for _ in range(int(digit)):
                    if len(non_numbers) == 0:
                        break
                    result.append(non_numbers.pop(0))

        else:
            if int(digit) != 0:
                for _ in range(int(digit)):
                    if len(non_numbers) == 0:
                        break
                    non_numbers.pop(0)

    return "".join(result)


text = input()
print(take_or_skip(text))
