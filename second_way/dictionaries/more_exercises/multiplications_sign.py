def multiplication_sign():
    first_number, second_number, three_number = int(input()), int(input()), int(input())
    result = first_number * second_number * three_number

    if result > 0:
        return "positive"
    elif result < 0:
        return "negative"
    else:
        return "zero"


print(multiplication_sign())

