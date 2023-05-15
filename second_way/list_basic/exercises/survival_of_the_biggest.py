numbers = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

result = [numbers.remove(min(numbers)) for _ in range(count_of_numbers_to_remove)]
print(*numbers, sep=", ")

