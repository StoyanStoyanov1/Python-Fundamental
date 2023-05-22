def perfect_number(current_number):
    sum_of_divisors = sum([number for number in range(1, current_number // 2 + 1) if current_number % number == 0])
    if sum_of_divisors == current_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))