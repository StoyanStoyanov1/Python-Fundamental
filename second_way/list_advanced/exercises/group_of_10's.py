def group_of_10_s(current_numbers):
    group = 10
    result = []

    while len(current_numbers) > 0:
        for_group = [current_numbers.pop(index) for index in range(len(current_numbers) - 1, -1, -1)
                     if current_numbers[index] in range(group + 1)]

        result.append(f"Group of {group}'s: {for_group[::-1]}")
        group += 10

    return "\n".join(result)


numbers = list(map(int, input().split(", ")))
print(group_of_10_s(numbers))
