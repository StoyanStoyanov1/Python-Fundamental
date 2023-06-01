from math import floor


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line = abs(x1) + abs(y1)
    second_line = abs(x2) + abs(y2)
    three_line = abs(x3) + abs(y3)
    fourth_line = abs(x4) + abs(y4)

    first_longer_line = first_line + second_line
    second_longer_line = three_line + fourth_line

    if first_longer_line >= second_longer_line:
        if first_line <= second_line:
            return f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})'
        else:
            return f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})'

    else:
        if three_line <= fourth_line:
            return f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})'
        else:
            return f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})'


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
