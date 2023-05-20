numbers = list(map(int, input().split()))
current_index = int(input())
new_numbers = []
counter = 0
index = 0

while len(numbers) > 0:
    counter += 1
    if counter % current_index == 0:
        new_numbers.append(numbers.pop(index))

    else:
        index += 1

    if index >= len(numbers):
        index = 0

print(str(new_numbers).replace(" ", ""))
