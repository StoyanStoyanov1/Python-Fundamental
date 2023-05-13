first_string = input()
second_string = input()

for index in range(len(first_string)):
    if first_string[index] != second_string[index]:
        first_string = first_string[:index] + second_string[index] + first_string[index + 1:]
        print(first_string)