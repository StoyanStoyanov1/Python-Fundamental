numbers = input().split()
text = [symbol for symbol in input()]

for number in numbers:
    list_of_number = map(lambda digit: int(digit), number)
    letter = text.pop(sum(list_of_number) - len(text))
    print(letter, end="")
