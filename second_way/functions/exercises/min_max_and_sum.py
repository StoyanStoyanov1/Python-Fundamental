def min_max_and_sum(number):
    return f"The minimum number is {min(number)}\nThe maximum number is {max(number)}\nThe sum number is: {sum(number)}"


numbers = list(map(int, input().split()))
print(min_max_and_sum(numbers))