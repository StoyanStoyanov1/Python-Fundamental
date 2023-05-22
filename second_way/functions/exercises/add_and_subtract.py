def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(numbers):
    three_number = numbers[2]
    return sum_numbers(numbers[0], numbers[1]) - three_number


numbers = [int(input()) for _ in range(3)]
print(subtract(numbers))