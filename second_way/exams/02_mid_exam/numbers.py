class Numbers:

    def __init__(self, current_numbers):
        self.current_numbers = current_numbers
        self.average_number = sum(self.current_numbers) / len(self.current_numbers)

    def greater_numbers(self):
        greater_numbers = []
        for number in self.current_numbers:
            if number > self.average_number:
                greater_numbers.append(number)

        return greater_numbers

    def __repr__(self):
        sorted_result = sorted(self.greater_numbers(), reverse=True)
        if sorted_result:
            return ' '.join(str(sorted_result[index]) for index in range(len(sorted_result)) if index < 5)
        else:
            return "No"


numbers = list(map(int, input().split()))
print(Numbers(numbers))
