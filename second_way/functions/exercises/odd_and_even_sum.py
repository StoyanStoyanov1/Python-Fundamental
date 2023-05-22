def even_and_odd_sum(digits):
    odd_sum = [int(digit) for digit in digits if int(digit) % 2 != 0]
    even_sum = [int(digit) for digit in digits if int(digit) % 2 == 0]
    return f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}"


print(even_and_odd_sum(input()))