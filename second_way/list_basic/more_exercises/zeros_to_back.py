numbers = list(map(int, input().split(", ")))

zeros_to_back = list(filter(lambda digit: digit != 0, numbers))
[zeros_to_back.append(zero) for zero in numbers if zero == 0]

print(zeros_to_back)