from math import floor


def first_closed_to_zero(current_x1, current_y1):
    return abs(current_x1) + abs(current_y1)


def second_closed_to_zero(current_x2, current_y2):
    return abs(current_x2) + abs(current_y2)


def result(x1, y1, x2, y2):
    if first_closed_to_zero(x1, y1) < second_closed_to_zero(x2, y2):
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(result(x1, y1, x2, y2))
