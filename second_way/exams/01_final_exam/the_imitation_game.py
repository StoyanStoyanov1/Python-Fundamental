class TheImitationGame:

    def __init__(self, message, commands):
        self.message = message
        self.commands = commands
        self.logic()

    def logic(self):

        for command in self.commands:
            if command[0] == "Move":
                self.move(int(command[1]))

            elif command[0] == "Insert":
                self.insert(int(command[1]), command[2])

            elif command[0] == "ChangeAll":
                self.change_all(command[1], command[2])

    def move(self, number_of_letters):
        self.message = self.message[number_of_letters:] + self.message[:number_of_letters]

    def insert(self, index, value):
        self.message = self.message[:index] + value + self.message[index:]

    def change_all(self, substring, replacement):
        self.message = self.message.replace(substring, replacement)

    def __repr__(self):
        return f"The decrypted message is: {self.message}"


message = input()
commands = []

while True:
    current_input = input()

    if current_input == "Decode":
        break

    commands.append(current_input.split("|"))

print(TheImitationGame(message, commands))
