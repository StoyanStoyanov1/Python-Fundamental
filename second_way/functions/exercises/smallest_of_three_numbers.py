def smallest_number(numbers):
    return min(numbers)


three_numbers = [int(input()) for _ in range(3)]
print(smallest_number(three_numbers))