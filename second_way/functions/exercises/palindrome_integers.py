def palindrome_integers(current_numbers):
    return list(map(lambda number: number == number[::-1], current_numbers))


numbers = input().split(", ")
print(*palindrome_integers(numbers), sep="\n")