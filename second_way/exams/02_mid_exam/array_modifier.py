class ArrayModifier:

    def __init__(self, numbers, commands):
        self.numbers = numbers
        self.commands = commands
        self.array_modifier()

    def swap(self, first_index, second_index):
        self.numbers[first_index], self.numbers[second_index] = self.numbers[second_index], self.numbers[first_index]

    def multiply(self, first_index, second_index):
        self.numbers[first_index] *= self.numbers[second_index]

    def decrease(self):
        for index in range(len(self.numbers)):
            self.numbers[index] -= 1

    def array_modifier(self):

        for command in self.commands:

            command = command.split()

            if len(command) > 1:
                first_index = int(command[1])
                second_index = int(command[2])
                if command[0] == "swap":
                    self.swap(first_index, second_index)
                elif command[0] == "multiply":
                    self.multiply(first_index, second_index)

            else:
                self.decrease()

    def __repr__(self):
        return ", ".join(str(number) for number in self.numbers)


numbers = list(map(int, input().split()))
commands = []

while True:
    command = input()
    if command == "end":
        break
    commands.append(command)

print(ArrayModifier(numbers, commands))
