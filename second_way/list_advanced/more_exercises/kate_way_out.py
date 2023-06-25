def find_k_position(matrix):
    for row in range(len(matrix)):
        if "k" in matrix[row]:
            return [row, matrix[row].index('k')]


def find_k_way(row, col, steps=0):
    if row not in range(len(matrix)) or col not in range(len(matrix[0])):
        return steps

    if matrix[row][col] == "#":
        return 0

    matrix[row][col] = "#"

    first_result = find_k_way(row + 1, col, steps + 1)
    second_result = find_k_way(row, col + 1, steps + 1)
    third_result = find_k_way(row - 1, col, steps + 1)
    fourth_result = find_k_way(row, col - 1, steps + 1)

    return max(first_result, second_result, third_result, fourth_result)


matrix = [list(input()) for _ in range(int(input()))]
kate_position = find_k_position(matrix)

found_k_way = find_k_way(kate_position[0], kate_position[1])

if found_k_way:
    print(f"Kate got out in {found_k_way} moves")

else:
    print("Kate cannot get out")
