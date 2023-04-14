def zeros_to_back (list_numbers):
    """finds all the zeros, and moves them to the back"""
    result = list(filter(lambda digit: digit != 0, list_numbers))
    for digit in list_numbers:
        if digit == 0:
            result.append(digit)

    return result


list_whit_numbers = list(map(int, input().split(", ")))
print(zeros_to_back(list_whit_numbers))
