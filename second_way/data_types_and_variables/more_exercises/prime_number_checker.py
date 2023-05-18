number = int(input())
result = filter(lambda x: number % x == 0, list(range(2, number)))

print(not any(result))
