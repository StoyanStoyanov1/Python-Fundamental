def the_result(the_number, the_index):
    result = []
    counter = 0
    index = 0

    while len(the_number) > 0:
        counter += 1

        if counter % the_index == 0:
            result.append(the_number.pop(index))
        else:
            index += 1

        if index >= len(the_number):
            index = 0

    return str(result).replace(" ", "").replace('\'', '')

number = input().split()
index = int(input())
print(the_result(number, index))