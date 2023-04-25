numbers = list(map(int, input().split()))

average_value = sum(numbers) / len(numbers)

result = sorted([number for number in numbers if number > average_value], reverse=True)
result = result[:5]

if len(result) != 0:
    print(*result, sep=" ")
else:
    print("No")
