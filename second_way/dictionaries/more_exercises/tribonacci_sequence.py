def sum_of_the_previous_3(long_line):
    result = [1]
    for _ in range(long_line - 1):
        if len(result) > 3:
            result.append(sum(result[len(result) - 1: len(result) - 4:-1]))
        else:
            result.append(sum(result))

    return result


number = int(input())
print(*sum_of_the_previous_3(number), sep=" ")
