def even_numbers(numbers):
    return list(filter(lambda digit: digit % 2 == 0, numbers))


numbers = list(map(int, input().split()))
print(even_numbers(numbers))
