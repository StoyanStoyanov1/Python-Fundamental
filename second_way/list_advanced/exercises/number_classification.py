def positive(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) >= 0])


def negative(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) < 0])


def even(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) % 2 == 0])


def odd(current_numbers):
    return ", ".join([number for number in current_numbers if int(number) % 2 != 0])


numbers = input().split(", ")

print(f"Positive: {positive(numbers)}\nNegative: {negative(numbers)}"
      f"\nEven: {even(numbers)}\nOdd: {odd(numbers)}")