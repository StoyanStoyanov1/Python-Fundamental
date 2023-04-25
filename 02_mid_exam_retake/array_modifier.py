numbers = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        break

    elif command[0] == "decrease":
        numbers = [num - 1 for num in numbers]

    elif command[0] == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        first_number = numbers[first_index]
        second_number = numbers[second_index]
        numbers[first_index] = first_number * second_number

    elif command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

result = [str(element) for element in numbers]

print(*result, sep=", ")

