class MovingTarget:

    def __init__(self, targets, commands):
        self.targets = targets
        self.commands = commands
        self.current_commands()

    def shoot(self, index, power):
        if index in range(len(self.targets)):
            self.targets[index] -= power
            if not self.targets[index] > 0:
                self.targets.pop(index)

    def add(self, index, value):
        if index in range(len(self.targets)):
            self.targets.insert(index, value)
        else:
            print("Invalid placement!")

    def strike(self, index, radius):

        if index + radius in range(len(self.targets)) and index - radius in range(len(self.targets)):
            self.targets.pop(index + radius)
            self.targets.pop(index)
            self.targets.pop(index - radius)
        else:
            print("Strike missed!")

    def current_commands(self):
        for command in self.commands:
            current_command, current_index, current_number = command.split()
            if current_command == "Shoot":
                self.shoot(int(current_index), int(current_number))

            elif current_command == "Add":
                self.add(int(current_index), int(current_number))

            elif current_command == "Strike":
                self.strike(int(current_index), int(current_number))

    def __repr__(self):
        return "|".join(str(target) for target in self.targets)


targets = list(map(int, input().split()))
commands = []

while True:
    command = input()
    if command == "End":
        break

    commands.append(command)



print(MovingTarget(targets, commands))