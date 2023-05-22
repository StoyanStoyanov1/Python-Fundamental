def the_first_factorial(number):
    factorial = 1
    for digit in range(number, 1, -1):
        factorial *= digit
    return factorial


def the_second_factorial(number):
    factorial = 1
    for digit in range(number, 1, -1):
        factorial *= digit
    return factorial


def factorial_divisions(first_current_number, second_current_number):
    first_factorial = the_first_factorial(first_current_number)
    second_factorial = the_second_factorial(second_current_number)

    return f"{first_factorial / second_factorial:.2f}"


first_number, second_number = int(input()), int(input())
print(factorial_divisions(first_number, second_number))
