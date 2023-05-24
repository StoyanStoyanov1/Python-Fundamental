def electron_distribution(current_number_of_electrons):
    result = []
    position = 1
    while True:
        number = 2 * (position ** 2)
        if sum(result) + number <= current_number_of_electrons:
            result.append(number)
            if sum(result) == current_number_of_electrons:
                return result

        else:
            last_number = current_number_of_electrons - sum(result)
            result.append(last_number)
            return result

        position += 1


number_of_electrons = int(input())
print(electron_distribution(number_of_electrons))
