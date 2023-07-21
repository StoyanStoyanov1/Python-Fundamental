class WorldTour:

    def __init__(self, current_text, commands):
        self.current_text = current_text
        self.commands = commands
        self.logic()

    def add_stop(self, index, string):
        if index in range(len(self.current_text)):
            self.current_text = self.current_text[:index] + string + self.current_text[index:]

    def remove_stop(self, start_index, end_index):
        if start_index in range(len(self.current_text)) and end_index in range(len(self.current_text)):
            self.current_text = self.current_text[:start_index] + self.current_text[end_index + 1:]

    def switch(self, old_string, new_string):
        self.current_text = self.current_text.replace(old_string, new_string)

    def logic(self):
        for command in self.commands:
            current_command, first_data, second_data = command.split(":")

            if current_command == "Add Stop":
                self.add_stop(int(first_data), second_data)

            elif current_command == "Remove Stop":
                self.remove_stop(int(first_data), int(second_data))

            elif current_command == "Switch":
                self.switch(first_data, second_data)

            print(self.current_text)

    def __repr__(self):
        return f"Ready for world tour! Planned stops: {self.current_text}"


text = input()
commands = []
command = input()

while command != "Travel":
    commands.append(command)
    command = input()

print(WorldTour(text, commands))