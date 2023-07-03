rows = int(input())
matrix = [input().split() for _ in range(rows)]
cols = len(matrix[0])

count_steps = 0


def find_the_len_dots(row, col):
    global count_steps
    if col not in range(cols):
        return count_steps

    if row not in range(rows):
        return count_steps

    if matrix[row][col] != ".":
        return count_steps

    matrix[row][col] = "-"
    count_steps += 1

    right_step = find_the_len_dots(row, col + 1)
    left_step = find_the_len_dots(row, col - 1)
    up_step = find_the_len_dots(row - 1, col)
    down_step = find_the_len_dots(row + 1, col)

    return count_steps


def find_max_steps():
    global count_steps
    steps = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == ".":
                count_steps = 0
                steps.append(find_the_len_dots(r, c))
    if steps:
        return max(steps)
    return 0


print(find_max_steps())
