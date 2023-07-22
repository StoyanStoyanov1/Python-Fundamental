class SecretChat:

    def __init__(self, current_text, commands):
        self.current_text = current_text
        self.commands = commands
        self.logic()

    def insert_space(self, index):
        if index in range(len(self.current_text)):
            self.current_text = self.current_text[:index] + " " + self.current_text[index:]
            print(self.current_text)

    def reverse(self, symbol):
        if symbol in self.current_text:
            self.current_text = self.current_text.replace(symbol, "", 1)
            self.current_text += symbol[::-1]
            print(self.current_text)
        else:
            print("error")

    def change_all(self, substring, replacement):
        self.current_text = self.current_text.replace(substring, replacement)
        print(self.current_text)

    def logic(self):
        for command in self.commands:
            current_command = command.split(":|:")

            if current_command[0] == "InsertSpace":
                index = int(current_command[1])
                self.insert_space(index)

            elif current_command[0] == "Reverse":
                symbol = current_command[1]
                self.reverse(symbol)

            elif current_command[0] == "ChangeAll":
                substring, replacement = current_command[1], current_command[2]
                self.change_all(substring, replacement)

    def __repr__(self):
        return f"You have a new text message: {self.current_text}"


text = input()
commands = []

while True:
    command = input()
    if command == "Reveal":
        break
    commands.append(command)

print(SecretChat(text, commands))
